# /accounts/views.py
from django.contrib.auth import login
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect
from django.shortcuts import render
from base.settings import LOGIN_VIEW


def guest_view(request):
    context = {}
    return render(request, 'accounts/guest.html', context)


@login_required(login_url="/accounts/login/")
def profile_view(request):
    context = {}
    return render(request, 'accounts/profile.html', context)


def register_view(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)

        if form.is_valid():
            user = form.save()
            # Log User in
            login(request, user)
            return redirect('accounts:profile_view')
        else:
            form = UserCreationForm()

    context = {'form': form}
    return render(request, 'accounts/register.html', context)


def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            # Log User in
            user = form.get_user()
            login(request, user)
            return redirect(LOGIN_VIEW)
    else:
        form = AuthenticationForm()

    context = {'form': form}
    return render(request, 'accounts/login.html', context)


def logout_view(request):
    if request.method == "POST":
        logout(request)
        return redirect('accounts:guest_view')
    return render(request, 'accounts/guest.html')
