from django.shortcuts import render
# from posts.models import Post

def home(request):
    posts = ""
    return render(request, 'home.html', {'posts':posts} )


def faq(request):
    return render(request, 'faq.html')


def about(request):
    return render(request, 'about.html')
