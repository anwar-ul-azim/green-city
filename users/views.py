from django.contrib import messages
from .models import Profile, Verify
from posts.models import Post
from cycles.models import Cycle
from .forms import UserRegisterForm, ProfileUpdateForm, ProfileVerifyForm
from django.shortcuts import render, redirect
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.decorators import login_required


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'{username} account has been created! You will now able to log in')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})


@login_required
def profile(request):
    try:
        profile = Profile.objects.get(user=request.user)
    except ObjectDoesNotExist:
        profile = None

    try:
        verify = Verify.objects.get(user=request.user)
    except ObjectDoesNotExist:
        verify = None
    
    my_cycles = Cycle.objects.filter(owner=request.user)
    my_posts = Post.objects.filter(author=request.user)

    if request.method == 'POST':
        form = ProfileUpdateForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            data = form.save(commit=False)
            data.user = request.user
            data.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('profile')
    else:
        context = {
            'profile'  : profile,
            'verify'   : verify,
            'form'     : ProfileUpdateForm(instance=profile),
            'form_v'   : ProfileVerifyForm(instance=verify),
            'my_cycles': my_cycles,
            'my_posts' : my_posts
        }
        return render(request, 'users/profile.html', context)


@login_required
def profileVerify(request):
    if request.method == 'POST':
        try:
            verify = Verify.objects.get(user=request.user)
        except ObjectDoesNotExist:
            verify = None
        form = ProfileVerifyForm(request.POST, request.FILES,  instance=verify)
        if form.is_valid():
            data = form.save(commit=False)
            data.user = request.user
            data.is_verify_submit = True
            data.save()
            messages.success(request, f'Your account verification request has been submitted!')
            return redirect('profile')
