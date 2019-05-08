from django.shortcuts import render
from cycles.models import Cycle, Pickcycle, Dropcycle
from payments.models import Payment
from django.utils import timezone

def payment(request):

#     t1 = Pickcycle.objects.get(Picker_id = request.user.id ).pick_date
#     # Pickcycle.objects.get(Picker_id = request.user.id ).delete()
#     t2 = Dropcycle.objects.get(droper_id = request.user.id ).drop_date
#     res = (t2 - t1).total_seconds() / 60.0
    
#     #print(t1,'-',t2,'=',res)
#     pickcycletime = res

#     Balance = Payment.objects.get(balanceOwner_id = request.user.id ).balance
#     #print(Balance)
    



    return render(request, 'payments/payment.html'
    # , {'pickcycletime':pickcycletime}, {'Balance':Balance}
    )
    

def cash(request):
    return render(request, 'payments/cash.html')


def balance(request):
    return render(request, 'payments/balance.html')
