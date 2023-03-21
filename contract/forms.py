from django import forms
from django.forms import ModelForm

from .models import *


class Contract_Detail_Form(ModelForm):
    class Meta:
        model = Contract_Detail
        fields = "__all__"
