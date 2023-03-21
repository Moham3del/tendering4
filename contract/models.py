from django.db import models
from django.conf import settings

from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from main.models import *



# Create your models here.



class Contract_Detail(models.Model):

    contract_type = [
        ('توريد + تنفيذ', 'توريد + تنفيذ'),
        ('توريد', 'توريد'),
        ('تنفيذ', 'تنفيذ'),
    ]

    cost_istimation = [
        ('إنشاءات (أ)', 'إنشاءات (أ)'),
        ('بنية تحتية (ج)', 'بنية تحتية (ج)'),
    ]
    # creator
    
    creator = models.CharField(max_length=250, null=True, blank=True)
    sector = models.CharField(max_length=250, null=True, blank=True)
    project = models.CharField(max_length=250, null=True, blank=True)

    # contract
    works_type = models.CharField(max_length=250, null=False, blank=False)
    contract_type =  models.CharField(max_length=250, choices=contract_type, null=False, blank=False)
    contract_value =  models.IntegerField(null=False, blank=False)
    contract_duration =  models.IntegerField(null=False, blank=False)
    cost_istimation =  models.CharField(max_length=250, choices=cost_istimation, null=False, blank=False)



    name = models.CharField(max_length=250, null=False, blank=False)
    bank_account =  models.IntegerField(null=False, blank=False)
    iban =  models.IntegerField(null=False, blank=False)
    tax_number =  models.IntegerField(null=False, blank=False)
    signature_authorization =  models.FileField(null=True, blank=False, upload_to='files')
    delegated_nam = models.CharField(max_length=250, null=False, blank=False)
    delegated_title = models.CharField(max_length=250, null=False, blank=False)
    gov_id_no = models.CharField(max_length=250, null=False, blank=False)
    second_party_representative = models.CharField(max_length=250, null=False, blank=False)
    phone_no = models.IntegerField(null=False, blank=False)
    email = models.EmailField(null=False, blank=False, max_length=50)
    postal_code = models.CharField(max_length=20, null=False, blank=False)
    address = models.CharField(max_length=250, null=False, blank=False)
    commercial_register =  models.FileField(null=True, blank=True, upload_to='files')
    commercial_register_date =  models.DateField(null=False, blank=False)
    manager_authorized_agent = models.CharField(max_length=250, null=False, blank=False)
    association_contract =  models.FileField(null=True, blank=True, upload_to='files')
    zakat_Income_certificate =  models.FileField(null=True, blank=True, upload_to='files')
    sub_contractor_profile =  models.FileField(null=True, blank=True, upload_to='files')
    special_conditions =  models.CharField(max_length=250, null=False, blank=False)
    payment_terms =  models.CharField(max_length=250, null=False, blank=False)



    def __str__(self):
        return str(self.project)
    class Meta:
        verbose_name="Contract_Detail"
        ordering = ['id']