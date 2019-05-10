from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm, ProfileUpdateForm

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
    if request.method == 'POST':
        try:
            form = ProfileUpdateForm(
                request.POST, request.FILES, instance=request.user.profile)
        except:
            form = ProfileUpdateForm(
                request.POST, request.FILES)
        if form.is_valid():
            data = form.save(commit=False)
            data.user = request.user
            data.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('profile')
    else:
        try:
            form = ProfileUpdateForm(instance=request.user.profile)
        except:
            form = ProfileUpdateForm()
    context = {
        'form': form
    }
    return render(request, 'users/profile.html', context)
