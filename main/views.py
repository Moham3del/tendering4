from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect
from django.contrib import messages
from django.contrib.auth import authenticate, logout
from django.contrib.auth import login as myLogin
from django.contrib.auth.decorators import login_required
from .decorators import *
# Create your views here.

from .forms import *

@login_required(login_url='login')
@allowedUsers(allowedGroups=['allowedlogin'])
def index(request):
    if request.user.is_staff:
        return render(request, 'main/index.html')
    else:
        return redirect('user_profile')


@login_required(login_url='login')
@allowedUsers(allowedGroups=['allowedlogin'])
def about(request):
    return render(request, 'main/about.html')


@notLoggedUser
def register(request):
    form = CreateNewUser()
    if request.method == 'POST':
        form = CreateNewUser(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, user + ' Created Successfully !')
            return redirect('login')

    context ={'form':form}
    return render(request, 'main/register.html', context)


@notLoggedUser
def register_ar(request):
    form = CreateNewUser()
    if request.method == 'POST':
        form = CreateNewUser(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, user + ' Created Successfully !')
            return redirect('login_ar')

    context ={'form':form}
    return render(request, 'main/register_ar.html', context)


@notLoggedUser
def userLogin(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            myLogin(request, user)
            if request.user.is_staff:
                return redirect('tender_details')
            else:
                return redirect('user_profile')
        else:
            messages.info(request, 'User Name or Password not Valid')

    context ={}
    return render(request, 'main/login.html', context)

@notLoggedUser
def userLogin_ar(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            myLogin(request, user)
            return redirect('index')
        else:
            messages.info(request, 'User Name or Password not Valid')

    context ={}
    return render(request, 'main/login_ar.html', context)


def userLogout(request):
    logout(request)
    return redirect('login')


@login_required(login_url='login')
def userProfile(request):
    context = {}
    return render(request, 'main/profile.html', context)



