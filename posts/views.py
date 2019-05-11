from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist
from .models import Post
from .forms import NewPostForm


@login_required
def createPost(request):
    if request.method == 'POST':
        new_post = NewPostForm(request.POST, request.FILES)
        if new_post.is_valid():
            new_post = new_post.save(commit=False)
            new_post.author = request.user
            new_post.save()
        return redirect('post')
    else:
        content = {'form': NewPostForm()}
        return render(request, 'posts/create.html', content)


@login_required
def detail(request, id):
    try:
        post = Post.objects.get(pk=id)
    except ObjectDoesNotExist:
        post = None
    content = {'post': post}
    return render(request, 'posts/detail.html', content)


def posts(request):
    content = {'posts': Post.objects.all()}
    return render(request, 'posts/post.html', content)
