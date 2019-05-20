from django.conf import settings
from django.contrib import messages
from django.core.mail import send_mail, EmailMessage
from .models import Profile, Verify
from posts.models import Post
from cycles.models import Cycle, Pickcycle, Dropcycle
from .forms import UserRegisterForm, ProfileUpdateForm, ProfileVerifyForm
from django.http import HttpResponse
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_text
from django.shortcuts import render, redirect
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from .tokens import account_activation_token
from django.template.loader import render_to_string
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.decorators import login_required

def hireHistory(user):
    pick_obj = Pickcycle.objects.filter(picked_by=user)
    hired_cycle = []
    for obj in pick_obj:
        data = {}
        data['pick'] = obj
        data['drop'] = Dropcycle.objects.get(pick_id=obj.id)
        hired_cycle.append(data)
    return hired_cycle


def rentHistory(user):
    cycle_obj = Cycle.objects.filter(owner=user)
    rented_cycle = []
    for cycle in cycle_obj:
        pick_obj = Pickcycle.objects.filter(cycle_id=cycle.id)
        for obj in pick_obj:
            data = {}
            data['pick'] = obj
            data['drop'] = Dropcycle.objects.get(pick_id=obj.id)
            rented_cycle.append(data)
    return rented_cycle


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False
            user.save()
            current_site = get_current_site(request)
            username = form.cleaned_data.get('username')
            email = form.cleaned_data.get('email')
            subject = 'Dear {},Thank you for joining us.Please activate your account.'.format(username)
            message = message = render_to_string('users/acc_active_email.html', {
                'user': user,
                'domain': current_site.domain,
                'uid':urlsafe_base64_encode(force_bytes(user.pk)).decode(),
                'token':account_activation_token.make_token(user),
            })
            from_email = settings.DEFAULT_FROM_EMAIL
            to_email = [email]
            email = EmailMessage(
                        subject, message, to=[to_email]
            )
            send_mail(subject, message, from_email , to_email, fail_silently=True)
            messages.success(request, f'Please confirm your email address to complete the registration')
            email.send()
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
            'my_posts' : my_posts,
            'hired_cycle': hireHistory(request.user),
            'rented_cycle': rentHistory(request.user) 
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
            # send_mail(subject, message, from_email , to_email, fail_silently=True)                ###This method can be use to send any information to user email
            messages.success(request, f'Your account verification request has been submitted!')
            return redirect('profile')


"""
This method is used to activate user account. As there are other backends which are currently for other functionalities to perform 
the activation task in more efficient way 'django.contrib.auth.backends.ModelBackend' was defiened explicitly. Without activating via this confirmation url user cannot login 
to our site.
"""
def activate(request, uidb64, token,  backend='django.contrib.auth.backends.ModelBackend'):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        login(request, user, backend='django.contrib.auth.backends.ModelBackend')
        messages.success(request, f'Your account has been created! You will now able to setup your profile')
    else:
        messages.success(request, f'Activation link is invalid!')
    return redirect('home')
