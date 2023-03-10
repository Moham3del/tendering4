from django.db import models
from datetime import date

# Create your models here.
class Mngmnt_category(models.Model):
    name = models.CharField(max_length=250)
    def __str__(self):
        return self.name
    class Meta:
        verbose_name="Management"





class required(models.Model):
    name = models.CharField(max_length=250)
    def __str__(self):
        return self.name
    class Meta:
        verbose_name="required"

class required1(models.Model):
    name = models.CharField(max_length=250)
    def __str__(self):
        return self.name
    class Meta:
        verbose_name="required1"


class owner_list(models.Model):
    name = models.CharField(max_length=250)
    def __str__(self):
        return self.name
    class Meta:
        verbose_name="owner"


class T_detail(models.Model):

    tender_status = [
        ('جارية', 'جارية'),
        ('تم التقديم', 'تم التقديم'),
        ('منتهية', 'منتهية'),
        ('ملغية', 'ملغية'),
    ]


    no = models.IntegerField(null=False, blank=False)
    
    local_content_percentage = models.IntegerField(null=True, blank=True)
    title = models.CharField(max_length=250)
    submitting_offers_method = models.CharField(max_length=250, null=True, blank=True)
    photo_tender = models.ImageField(upload_to='photos', null=True, blank=True)
    photo_author = models.ImageField(upload_to='photos', null=True, blank=True)
    rfp_no = models.IntegerField(null=True, blank=True)
    starting_date = models.DateField(null=True, blank=True)
    participation_confirmation_letter_due_date = models.DateField(null=True, blank=True)
    receiving_inquiries_Deadline = models.DateField(null=True, blank=True)
    insurance_letter_date = models.DateField(null=True, blank=True)
    business_services_commencement_Date = models.DateField(null=True, blank=True)

    
    t_status = models.CharField(max_length=250, choices=tender_status, null=True, blank=True)
    
    management = models.ForeignKey(Mngmnt_category, on_delete=models.PROTECT, null=True, blank=True)
    insurance_Required = models.ForeignKey(required, on_delete=models.PROTECT, null=True, blank=True)
    initial_guarantee_required = models.ForeignKey(required1, on_delete=models.PROTECT, null=True, blank=True)
    owner = models.ForeignKey(owner_list, on_delete=models.PROTECT, null=True, blank=True)

    contract_duration = models.IntegerField(null=True, blank=True)

    submit_date = models.DateField(null=True, blank=True)

   

    def __str__(self):
        return self.title
    class Meta:
        verbose_name="Tender"
        ordering = ['no']

    @property
    def Days_till(self):
        today = date.today()
        
        days_till = self.submit_date - today
        days_till_stripped = str(days_till).split(",", 1)[0]
        return days_till_stripped


