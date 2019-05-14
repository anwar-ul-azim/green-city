from django.shortcuts import render, redirect
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.decorators import login_required
from cycles.models import Cycle, Location, Pickcycle, Dropcycle
from .forms import NewCycleForm, LocationForm, PickForm, DropForm
from django.contrib.auth.models import User
from django.core.mail import send_mail
from payments.models import Payment
from django.conf import settings
from django.utils import timezone
from django.contrib import messages


@login_required
def create(request):
    if request.method == 'POST':
        new_cycle = NewCycleForm(request.POST, request.FILES)
        if new_cycle.is_valid():
            new_cycle = new_cycle.save(commit=False)
            new_cycle.owner = request.user
            new_cycle.save()
            messages.success(request, f'new cycle created!')
        return redirect('profile')
    else:
        content = {'form': NewCycleForm()}
        return render(request, 'cycles/create.html', content)


@login_required
def cycleView(request, id):
    try:
        cycle = Cycle.objects.get(pk=id)
    except ObjectDoesNotExist:
        cycle = None
    try:
        location = Location.objects.get(cycle_id=cycle)
    except ObjectDoesNotExist:
        location = None
    if request.method == 'POST':
        new_location = LocationForm(request.POST, instance=location)
        if new_location.is_valid():
            new_location = new_location.save(commit=False)
            new_location.cycle_id = cycle
            new_location.save()
            messages.success(request, f'New Location Updated!')
        return redirect(request.path)
    if cycle.owner == request.user:
        form = LocationForm(instance=location)
    else:
        form = None
    pick = PickForm()
    pick.fields["cycle_id"].initial = cycle
    pick.fields["picked_by"].initial = request.user
    drop = DropForm()
    try:
        drop.fields["pick_id"].initial = Pickcycle.objects.get(
            pk=cycle.pick_id)
    except ObjectDoesNotExist:
        pass
    drop_btn = True
    if cycle.is_picked == True:
        pick_obj = Pickcycle.objects.get(id=cycle.pick_id)
        balance = Payment.objects.get(owner=pick_obj.picked_by)
        if balance.due > 0:
            drop_btn = False
            drop = None
    content = {
        'cycle'   : cycle,
        'location': location,
        'form'    : form,
        'form_p'  : pick,
        'form_d'  : drop,
        'drop_btn': drop_btn
        }
    return render(request, 'cycles/view.html', content)


@login_required
def dropcycle(request, id):
    if request.method == 'POST':
        drop = DropForm(request.POST)
        if drop.is_valid():
            drop.save()
            cycle = Cycle.objects.get(id=id)
            cycle.is_picked = False
            cycle.pick_id = 0
            cycle.save()
            return redirect('/cycles/' + str(id))


@login_required
def pickcycle(request, id):
    if request.method == 'POST':
        pick=PickForm(request.POST)
        if pick.is_valid():
            pick = pick.save()
            cycle = Cycle.objects.get(id=id)
            cycle.is_picked = True
            cycle.picked_times += 1
            cycle.pick_id = pick.id
            cycle.save()
            return redirect('/cycles/'+ str(id))

