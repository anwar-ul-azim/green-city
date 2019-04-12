from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings
from cycles.models import Cycle
from .models import Dropcycle
from django.contrib.auth.models import User
from django.utils import timezone

# Create your views here.

def dropcycle(request):
    allcycle = Cycle.objects.all()
    #allpickcycle = Pickcycle.objects.all()
    drop = Dropcycle.objects.get(droper_id = request.user.id )
    owner = Cycle.objects.get(OwnerId_id = request.user.id)
    
    
    #print(drop)
    if request.method == 'POST':
        if request.POST['cycleid'] and request.POST['locationid']:
            dropcycle = Dropcycle()
            dropcycle.cycleid = request.POST['cycleid']
            dropcycle.locationid = request.POST['locationid']
            dropcycle.droper = request.user
            dropcycle.drop_date = timezone.datetime.now()
            dropcycle.save()
            #print(Picker)
            cycle = Cycle.objects.filter(isPicked=False)
            #print(cycle)



        # if request.method == 'POST':
            
            message = 'Cycle Id:' + request.POST['cycleid'] + ', Location Id:' + request.POST['locationid'] #+ ', Picker Name: ' + Pickcycle.objects.get(id = request.POST['cycleid'] ).Picker.username
            owner= Cycle.objects.get(id = request.POST['cycleid'] ).OwnerId.email
            send_mail('Drop Cycle',
            message,
            settings.EMAIL_HOST_USER,
            ['mrahman111213@gmail.com',owner],
            fail_silently=False
            )
    return render(request, 'dropcycles/dropcycle.html', {'allcycle':allcycle})


