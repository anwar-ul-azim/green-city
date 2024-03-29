from django.core.paginator import Paginator
from django.shortcuts import render
from cycles.models import Cycle
from posts.models import Post

def home(request):
    cycles_list = []
    if request.method == 'POST':
        if request.POST['search'] != "":     
            for cycle in Cycle.objects.all():
                if request.POST['search'] in cycle.name:
                    cycles_list.append(cycle)
                if request.POST['search'] in cycle.model:
                    cycles_list.append(cycle)
    else:
        cycles_list = Cycle.objects.get_queryset().order_by('id')  
    paginator = Paginator(cycles_list, 5)  # Show 5 items per page
    page = request.GET.get('page')
    cycles = paginator.get_page(page)
    posts_list = Post.objects.all()[:2]
    content = {
        'cycles': cycles,
        'posts': posts_list
        }
    return render(request, 'home.html', content)


def faq(request):
    return render(request, 'faq.html')


def about(request):
    return render(request, 'about.html')
