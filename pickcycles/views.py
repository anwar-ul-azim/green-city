from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings
from cycles.models import Cycle
from payments.models import Payment
from .models import Pickcycle
from locations.models import Location

from django.contrib.auth.models import User
from django.utils import timezone

# Create your views here.

def pickcycle(request):
    error=""
    availableCycle = Cycle.objects.filter(isPicked=False)
    locations = Location.objects.all()
    if request.method == 'POST':
        balance = Payment.objects.get(balanceOwner_id = request.user.id ).balance
        picked_cycle = Cycle.objects.get(id=request.POST['cycleid'])
        if balance >= 30:
            if picked_cycle.isPicked == False:
                if request.POST['cycleid'] and request.POST['locationid']:
                    pickcycle = Pickcycle()
                    pickcycle.cycleid = request.POST['cycleid']
                    pickcycle.locationid = request.POST['locationid']
                    pickcycle.Picker = request.user
                    pickcycle.save()
                    picked_cycle.isPicked = True 
                    picked_cycle.save()

                    message = 'Cycle Id:' + request.POST['cycleid'] + ', Location Id:' + request.POST['locationid'] 
                    owner= Cycle.objects.get(id = request.POST['cycleid'] ).OwnerId.email
                    send_mail(
                        'Pick Cycle',
                        message,
                        settings.EMAIL_HOST_USER,
                        ['mrahman111213@gmail.com',owner],
                        fail_silently=False
                    )
                else:
                    error = "cycleid and locationid both are required"
            else:
                error = "the cycle is already been picked"
        else:
            error = "you can not pick a cycle because of low balance minimum is 30"

    return render(request, 'pickcycles/pickcycle.html', {'availableCycle':availableCycle, 'error':error,
        'locations':locations})


