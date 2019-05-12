from django.shortcuts import render, redirect
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.decorators import login_required
from cycles.models import Cycle, Location, Pickcycle, Dropcycle
from payments.models import Payment
from django.contrib.auth.models import User
from .forms import NewCycleForm, LocationForm
from django.core.mail import send_mail
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
    content = {
        'cycle': cycle,
        'location': location,
        'form': form
        }
    return render(request, 'cycles/view.html', content)


@login_required
def dropcycle(request):
#     error = ""
#     cycle = []
#     locations = Location.objects.all()
#     pay = Payment.objects.get(balanceOwner_id=request.user.id)
#     picked_cycles = Pickcycle.objects.filter(Picker=request.user.id)
#     for picked_cycle in picked_cycles:
#         data = {}
#         data['pick_info'] = picked_cycle
#         data['cycle_info'] = Cycle.objects.get(id=picked_cycle.cycleid)
#         cycle.append(data)

#     if request.method == 'POST':
#         picked_cycle = Cycle.objects.get(id=request.POST['cycleid'])
#         picked = Pickcycle.objects.get(cycleid=request.POST['cycleid'])
#         due = (timezone.now() - picked.pick_date).total_seconds()//3600
#         due = due * 10  # let say hour rate 10 tk
#         if pay.balance > due:
#             if picked_cycle.isPicked == True and picked.Picker == request.user:
#                 if request.POST['cycleid'] and request.POST['locationid']:
#                     dropcycle = Dropcycle()
#                     dropcycle.cycleid = request.POST['cycleid']
#                     dropcycle.locationid = request.POST['locationid']
#                     dropcycle.droper = request.user
#                     dropcycle.save()
#                     picked_cycle.isPicked = False
#                     picked_cycle.save()
#                     pay.balance = pay.balance - due
#                     pay.save()
#                     picked.delete()

#                     message = 'Cycle Id:' + \
#                         request.POST['cycleid'] + ', Location Id:' + \
#                         request.POST['locationid']
#                     owner = Cycle.objects.get(
#                         id=request.POST['cycleid']).OwnerId.email
#                     send_mail(
#                         'Drop Cycle',
#                         message,
#                         settings.EMAIL_HOST_USER,
#                         ['mrahman111213@gmail.com', owner],
#                         fail_silently=False
#                     )
#                     return redirect('/')
#                 else:
#                     error = "cycleid and locationid both are required"
#             else:
#                 error = "give a valid cycle id"
#         else:
#             error = "you can not drop the cycle because of low balance"

    return render(request, 'cycles/dropcycle.html'
#       , {
#         'allcycle': cycle,
#         'error': error,
#         'locations': locations,
#         'balance': pay.balance
#     }
    )


@login_required
def pickcycle(request):
#     error = ""
#     availableCycle = Cycle.objects.filter(isPicked=False)
#     locations = Location.objects.all()
#     if request.method == 'POST':
#         balance = Payment.objects.get(balanceOwner_id=request.user.id).balance
#         picked_cycle = Cycle.objects.get(id=request.POST['cycleid'])
#         if balance >= 30:
#             if picked_cycle.isPicked == False:
#                 if request.POST['cycleid'] and request.POST['locationid']:
#                     pickcycle = Pickcycle()
#                     pickcycle.cycleid = request.POST['cycleid']
#                     pickcycle.locationid = request.POST['locationid']
#                     pickcycle.Picker = request.user
#                     pickcycle.save()
#                     picked_cycle.isPicked = True
#                     picked_cycle.save()

#                     message = 'Cycle Id:' + \
#                         request.POST['cycleid'] + ', Location Id:' + \
#                         request.POST['locationid']
#                     owner = Cycle.objects.get(
#                         id=request.POST['cycleid']).OwnerId.email
#                     send_mail(
#                         'Pick Cycle',
#                         message,
#                         settings.EMAIL_HOST_USER,
#                         ['mrahman111213@gmail.com', owner],
#                         fail_silently=False
#                     )
#                 else:
#                     error = "cycleid and locationid both are required"
#             else:
#                 error = "the cycle is already been picked"
#         else:
#             error = "you can not pick a cycle because of low balance minimum is 30"

    return render(request, 'cycles/pickcycle.html'
# , {'availableCycle': availableCycle, 'error':error,
#         'locations': locations}
    )
