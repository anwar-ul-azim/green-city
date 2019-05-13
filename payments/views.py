from django.shortcuts import render, redirect
from cycles.models import Cycle, Pickcycle, Dropcycle
from payments.models import Payment, Transition, CashInOrOut
from django.contrib.auth.decorators import login_required
from .forms import CashForm, TransitionForm
from django.utils import timezone
from django.contrib import messages

@login_required
def balance(request):
    balance, created = Payment.objects.get_or_create(owner=request.user)
    cash = CashForm()
    cash.fields["client"].initial = request.user
    transition = TransitionForm()
    transition.fields["sender"].initial = request.user
    if created:
        balance.balance = 100
        balance.save()
        messages.success(request, f'You Got 100 BDT SignUp Bonus!!')
    content = {
        'balance': balance,
        'form_c' : cash,
        'form_t' : transition
        }
    return render(request, 'payments/balance.html', content)


@login_required
def transition(request):
    if request.method == 'POST':
        transition = TransitionForm(request.POST)
        if transition.is_valid():
            transition = transition.save()
            balance_sender = Payment.objects.get(owner=transition.sender)
            balance_sender.balance -= transition.amount
            balance_sender.save()
            balance_receiver, created = Payment.objects.get_or_create(
                owner=transition.receiver)
            balance_receiver.balance += transition.amount
            balance_receiver.save()
    return redirect('balance')
    

@login_required
def cash(request):
    if request.method == 'POST':
        cash = CashForm(request.POST)
        if cash.is_valid():
            cash = cash.save()
            client = Payment.objects.get(owner=cash.client)
            if cash.cash_in > 0 :
                client.balance += cash.cash_in
            if cash.cash_out > 0:
                client.balance -= cash.cash_out
            client.save()
    return redirect('balance')


