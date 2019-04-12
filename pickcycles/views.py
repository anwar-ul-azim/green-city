from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings
from cycles.models import Cycle
from payments.models import Payment
from .models import Pickcycle
from django.contrib.auth.models import User
from django.utils import timezone

# Create your views here.

def pickcycle(request):
    allcycle = Cycle.objects.all()
    availableCycle = Cycle.objects.filter(isPicked=False)
    print(availableCycle)
    #allpickcycle = Pickcycle.objects.all()
    try:
        picked = Pickcycle.objects.get(Picker_id = request.user.id )
        owner = Cycle.objects.get(OwnerId_id = request.user.id)
        #cycle = Cycle.objects.get(id = request.user.id)
        
        cycle = Cycle.objects.filter(isPicked=True)
        #cycle.isPicked(True)
        print(owner)
        print(cycle)
        #print(picked)
 
    except Pickcycle.DoesNotExist:
        picked = None
    if(picked != None):
        error="already picked"
    else:
        error="" 
        if request.method == 'POST':
            balance = Payment.objects.get(balanceOwner_id = request.user.id ).balance
            if balance >= 30:
                if request.POST['cycleid'] and request.POST['locationid']:
                    pickcycle = Pickcycle()
                    pickcycle.cycleid = request.POST['cycleid']
                    pickcycle.locationid = request.POST['locationid']
                    pickcycle.Picker = request.user
                    pickcycle.pick_date = timezone.datetime.now()
                    pickcycle.save()
    
            message = 'Cycle Id:' + request.POST['cycleid'] + ', Location Id:' + request.POST['locationid'] #+ ', Picker Name: ' + Pickcycle.objects.get(id = request.POST['cycleid'] ).Picker.username
            owner= Cycle.objects.get(id = request.POST['cycleid'] ).OwnerId.email
            send_mail('Pick Cycle',
            message,
            settings.EMAIL_HOST_USER,
            ['mrahman111213@gmail.com',owner],
            fail_silently=False
            )

    return render(request, 'pickcycles/pickcycle.html', {'availableCycle':availableCycle, 'error':error})


