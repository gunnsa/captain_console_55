from django.contrib.auth.forms import UserCreationForm
from user.forms.profile_form import ProfileForm
from django.shortcuts import render, redirect
from user.models import Profile


def register(request):
    """ Adds new user to database """
    if request.method == 'POST':
        form = UserCreationForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')

    return render(request, 'user/register.html', {
        'form': UserCreationForm()
    })


def profile(request):
    """ Returns view of current users profile """
    user_profile = Profile.objects.filter(user=request.user).first()
    if request.method == 'POST':
        form = ProfileForm(instance=user_profile, data=request.POST)
        if form.is_valid():
            user_profile = form.save(commit=False)
            user_profile.user = request.user
            user_profile.save()
            return redirect('profile')

    return render(request, 'user/profile.html', {
        'form': ProfileForm(instance=user_profile)
    })
