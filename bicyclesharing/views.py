from django.core.paginator import Paginator
from django.shortcuts import render
from cycles.models import Cycle

def home(request):
    cycles_list = Cycle.objects.all()
    paginator = Paginator(cycles_list, 5)  # Show 5 items per page
    page = request.GET.get('page')
    cycles = paginator.get_page(page)
    content = {
        'cycles': cycles
        }
    return render(request, 'home.html', content)


def faq(request):
    return render(request, 'faq.html')


def about(request):
    return render(request, 'about.html')
