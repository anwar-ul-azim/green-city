import math
from datetime import datetime
from django.conf import settings
from django.utils import timezone
from django.contrib import messages
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from .forms import CashForm, TransitionForm
from .models import Payment, Transition, CashInOrOut
from cycles.models import Cycle, Pickcycle, Dropcycle
from cycles.forms import CycleRatingForm
from cycles.views import dropcycle

def getFair(cycles):
    fair = 0
    for cycle_obj in cycles:
        hour = (timezone.now()-cycle_obj['pick'].pick_date).seconds/3600
        hour_rate = cycle_obj['cycle'].rent/24
        fair += math.ceil(hour * hour_rate)
    return fair


def getRentedCycles(user):
    my_cycles = Cycle.objects.filter(owner=user, is_picked=True)
    cycles = []
    for cycle in my_cycles:
        data = {}
        data['cycle'] = cycle
        data['pick'] = Pickcycle.objects.get(id=cycle.pick_id)
        cycles.append(data)
    return cycles


def getHiredCycle(user):
    my_picked = Pickcycle.objects.filter(picked_by=user)
    cycles = []
    for pick in my_picked:
        cycle_obj = Cycle.objects.get(id=pick.cycle_id.id)
        if pick.id == cycle_obj.pick_id:
            data = {}
            data['cycle'] = cycle_obj
            data['pick'] = pick
            cycles.append(data)
    return cycles


@login_required
def balance(request):
    balance, created = Payment.objects.get_or_create(owner=request.user)
    if created:
        balance.balance = 100
        balance.save()
        messages.success(request, f'You Got 100 BDT SignUp Bonus!!')
    cycles_rent = getRentedCycles(request.user)
    cycles_hire = getHiredCycle(request.user)
    balance.earned = getFair(cycles_rent)
    if balance.earned <= 0:
        balance.earned = 0
    balance.due = getFair(cycles_hire)
    balance.save()
    cash = CashForm()
    cash.fields["client"].initial = request.user
    transition = TransitionForm()
    transition.fields["sender"].initial = request.user
    receiver = None
    for cycle_obj in cycles_hire:
        receiver = cycle_obj['cycle'].owner
    transition.fields["receiver"].initial = receiver
    transition.fields["amount"].initial = balance.due
    drop_btn = True
    if balance.due >= balance.balance:
        drop_btn = False
    rating = CycleRatingForm()
    content = {
        'balance': balance,
        'form_c': cash,
        'form_t': transition,
        'form_r': rating,
        'cycles_r': cycles_rent,
        'cycles_h': cycles_hire,
        'drop_btn': drop_btn,
        'transition_history': Transition.objects.filter(Q(sender=request.user) | Q(receiver=request.user)),
        'cash_history': CashInOrOut.objects.filter(client=request.user) 
    }
    return render(request, 'payments/balance.html', content)


@login_required
def transition(request, id):
    if request.method == 'POST':
        transition = TransitionForm(request.POST)
        rating = CycleRatingForm(request.POST)
        if transition.is_valid() and rating.is_valid():
            rating = rating.save(commit=False)
            transition = transition.save(commit=False)
            balance_sender = Payment.objects.get(owner=transition.sender)
            if balance_sender.balance >= transition.amount:
                balance_sender.balance -= transition.amount
                balance_sender.due -= transition.amount
                balance_sender.save()
                balance_receiver, created = Payment.objects.get_or_create(
                    owner=transition.receiver)
                balance_receiver.balance += transition.amount
                balance_receiver.earned -= transition.amount
                balance_receiver.save()
                transition.save()
                dropcycle(id, rating.rating)
                messages.success(request, f'Transition Successful!!')
                email_to = [request.user.email, transition.receiver.email]
                message = 'Hello \n'
                message += 'Amount of ' + str(transition.amount) + ' BDT successfully transfer from the account of '+ transition.sender.username +' to the account of ' + transition.receiver.username + '. \n' 
                message += 'If it seems specious to you, contact with us ASAP. \nRegards, \nGreen-city.'
                send_mail('Transition Notice', message, settings.EMAIL_HOST_USER, email_to, fail_silently=False) 
            else:
                messages.success(request, f'Transition Failed!!')
    return redirect('balance')


@login_required
def cash(request):
    if request.method == 'POST':
        cash = CashForm(request.POST)
        if cash.is_valid():
            cash = cash.save()
            client = Payment.objects.get(owner=cash.client)
            message = 'Hello' + request.user.username + ', \n'
            if cash.cash_in > 0:
                client.balance += cash.cash_in
                messages.success(request, f'Cash In Successful!!')
                message += 'Amount of' + str(cash.cash_in) + 'BDT successfully add to your Green-city Account. \n'
            if cash.cash_out > 0:
                client.balance -= cash.cash_out
                messages.success(request, f'Cash Out Successful!!')
                message += 'Amount of' + str(cash.cash_out) + 'BDT successfully reduced from your Green-city Account. \n'
            client.save()
            email_to = request.user.email
            message += 'If it seems specious to you, contact with us ASAP. \nRegards, \nGreen-city.'
            send_mail('Cash Transition Notice', message, settings.EMAIL_HOST_USER, [email_to], fail_silently=False)
    return redirect('balance')
