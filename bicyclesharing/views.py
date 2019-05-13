from django.shortcuts import render
from cycles.models import Cycle

def home(request):
    content = {'cycles': Cycle.objects.all()}
    return render(request, 'home.html', content)


def faq(request):
    return render(request, 'faq.html')


def about(request):
    return render(request, 'about.html')
