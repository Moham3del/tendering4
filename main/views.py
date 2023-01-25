from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect
from django.contrib import messages
from django.contrib.auth import authenticate, logout
from django.contrib.auth import login as myLogin
# Create your views here.

from .forms import *

def index(request):
    return render(request, 'main/index.html')
def about(request):
    return render(request, 'main/about.html')



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



def userLogin(request):

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
    return render(request, 'main/login.html', context)

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
