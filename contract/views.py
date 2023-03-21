from django.shortcuts import render, redirect
from .models import *
from main.models import *
from .forms import *
from .filters import *
from django.contrib.auth.decorators import login_required
from main.decorators import *

# Create your views here.


@login_required(login_url='login')
@contract_main_index

def contract_main_index(request):

    user_tender_permission = User_TenderPermission.objects.get(user=request.user)
    user_contract_permission = User_ContractPermission.objects.get(user=request.user)
    user_project_permission = User_ProjectPermission.objects.get(user=request.user)

    context = {

        'user_tender_permission':user_tender_permission,
        'user_contract_permission':user_contract_permission,
        'user_project_permission':user_project_permission,

    }
    if request.user.is_staff:
        return render(request, 'contract/contract_main_index.html', context)
    else:
        return redirect('no_permission')


@login_required(login_url='login')

@contract_user_index

def contract_user_index(request):

    user_tender_permission = User_TenderPermission.objects.get(user=request.user)
    user_contract_permission = User_ContractPermission.objects.get(user=request.user)
    user_project_permission = User_ProjectPermission.objects.get(user=request.user)

    context = {

        'user_tender_permission':user_tender_permission,
        'user_contract_permission':user_contract_permission,
        'user_project_permission':user_project_permission,

    }
    if request.user.is_staff:
        return render(request, 'contract/contract_user_index.html', context)
    else:
        return redirect('no_permission')


@login_required(login_url='login')

@add_new_contract

def add_new_contract(request):

    user_tender_permission = User_TenderPermission.objects.get(user=request.user)
    user_contract_permission = User_ContractPermission.objects.get(user=request.user)
    user_project_permission = User_ProjectPermission.objects.get(user=request.user)
    user_profile = User_Profile.objects.get(user=request.user)

    form = Contract_Detail_Form
    if request.method == 'POST':
        form = Contract_Detail_Form(request.POST, request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.creator = request.user
            instance.sector = user_profile.sector_name
            instance.project = user_profile.project_name
            instance.save()
            return redirect('contract_main_index')

    context = {

        'user_tender_permission':user_tender_permission,
        'user_contract_permission':user_contract_permission,
        'user_project_permission':user_project_permission,
        'form':form,
        'user_profile':user_profile,


    }
    if request.user.is_staff:
        return render(request, 'contract/add_new_contract.html', context)
    else:
        return redirect('no_permission')
    

