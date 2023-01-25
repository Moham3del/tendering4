from django.shortcuts import render
from .models import *
# Create your views here.
def add_new_tender(request):
    return render(request, 'tendering/add_new_tender.html')
def tender_details(request):
    context = {
        'T_details': T_detail.objects.all(),
    }
    return render(request, 'tendering/tender_details.html', context)

def tender_details_details(request, id):
    t_d = T_detail.objects.get(id=id)
    context = {'mm': t_d}
    return render(request, 'tendering/tender_details_details.html', context)


# def tender_details_details(request):

#     return render(request, 'tendering/tender_details_details.html')


def tender_report(request):
    return render(request, 'tendering/tender_report.html')