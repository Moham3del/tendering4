from django.shortcuts import render, redirect
from .models import *
from .forms import T_detail_Form
from .filters import TenderFilter
from django.contrib.auth.decorators import login_required
from main.decorators import *

# Create your views here.
@login_required(login_url='login')
@allowedUsers(allowedGroups=['add_new'])

def add_new_tender(request):
    form = T_detail_Form()
    if request.method == 'POST':
        form = T_detail_Form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('tender_details')
    context = {'form':form}
    if request.user.is_staff:
        return render(request, 'tendering/add_new_tender.html', context)
    else:
        return redirect('user_profile')

@login_required(login_url='login')
@allowedUsers(allowedGroups=['add_new'])

def update_tender(request,id):
    update_tender = T_detail.objects.get(id=id)
    form = T_detail_Form(instance=update_tender)
    if request.method == 'POST':
        form = T_detail_Form(request.POST, instance=update_tender)
        if form.is_valid():
            form.save()
            return redirect('tender_details')
    context = {'form':form}
    if request.user.is_staff:
        return render(request, 'tendering/update_tender.html', context)
    else:
        return redirect('user_profile')

@login_required(login_url='login')

def tender_details(request):
    detail = T_detail.objects.all()
    searchFilter = TenderFilter(request.GET, queryset=detail)
    detail = searchFilter.qs
    context = {
        'myFilter': searchFilter
    }
    if request.user.is_staff:
        return render(request, 'tendering/tender_details.html', context)
    else:
        return redirect('user_profile')

@login_required(login_url='login')
@allowedUsers(allowedGroups=['tasks'])
def tender_details_details(request, id):
    t_d = T_detail.objects.get(id=id)
    context = {'mm': t_d}
    if request.user.is_staff:
        return render(request, 'tendering/tender_details_details.html', context)
    else:
        return redirect('user_profile')




@login_required(login_url='login')

def tender_report(request):
    detail = T_detail.objects.all()
    searchFilter = TenderFilter(request.GET, queryset=detail.filter(t_status='جارية').order_by('submit_date'))
    detail = searchFilter.qs
    context = {
        'myFilter': searchFilter
    }
    if request.user.is_staff:
        return render(request, 'tendering/tender_report.html', context)
    else:
        return redirect('user_profile')