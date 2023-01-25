from django.db import models

# Create your models here.
class T_detail(models.Model):
    tender_status = [
        ('جارية', 'جارية'),
        ('تم التقديم', 'تم التقديم'),
        ('منتهية', 'منتهية'),
        ('ملغية', 'ملغية'),
    ]
    insur_required = [
        ('نعم', 'نعم'),
        ('لا', 'لا'),
    ]
    owner_list = [
        ('NEOM', 'NEOM'),
        ('الشركة للوطنية للاسكان', 'الشركة للوطنية للاسكان'),
    ]
    no = models.IntegerField(null=False, blank=False)
    title = models.CharField(max_length=250)
    photo_tender = models.ImageField(upload_to='photos', null=True, blank=True)
    photo_author = models.ImageField(upload_to='photos', null=True, blank=True)
    rfp_no = models.IntegerField(null=True, blank=True)
    publication_date = models.DateField(null=True, blank=True)
    documents_value = models.DecimalField(max_digits=15, decimal_places=2, null=True, blank=True)
    t_status = models.CharField(max_length=250, choices=tender_status, null=True, blank=True)
    contract_duration = models.IntegerField(null=True, blank=True)
    insurance_Required = models.CharField(max_length=250, choices=insur_required, null=True, blank=True)
    submit_date = models.DateField(null=True, blank=True)
    owner = models.CharField(max_length=250, choices=owner_list, null=True, blank=True)
    management = models.CharField(max_length=250, null=True, blank=True)

    def __str__(self):
        return self.title
    class Meta:
        verbose_name="Tender"
        ordering = ['no']