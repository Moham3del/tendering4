


from django.db import models

from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


# Create your models here.


class User_Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.IntegerField(null=True, blank=True)
    full_name = models.CharField(max_length=50, null=True, blank=True)
    project_number = models.CharField(max_length=15, null=True, blank=True)
    project_name = models.CharField(max_length=50, null=True, blank=True)
    sector_name = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return str(self.user)
    class Meta:
        verbose_name="profile"
        ordering = ['user']

@receiver(post_save, sender=User)
def creat_level(sender, instance, created, **kwargs):
    if created:
        User_Profile.objects.create(user=instance)



class L_1(models.Model):
    name = models.CharField(max_length=250)
    def __str__(self):
        return self.name
    class Meta:
        verbose_name="L_1"


class L_2(models.Model):
    name = models.CharField(max_length=250)
    def __str__(self):
        return self.name
    class Meta:
        verbose_name="L_2"


class L_3(models.Model):
    name = models.CharField(max_length=250)
    def __str__(self):
        return self.name
    class Meta:
        verbose_name="L_3"


class L_4(models.Model):
    name = models.CharField(max_length=250)
    def __str__(self):
        return self.name
    class Meta:
        verbose_name="L_4"


class L_5(models.Model):
    name = models.CharField(max_length=250)
    def __str__(self):
        return self.name
    class Meta:
        verbose_name="L_5"


class User_Level(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    l_1 = models.ForeignKey(L_1, on_delete=models.PROTECT, null=True, blank=True)
    l_2 = models.ForeignKey(L_2, on_delete=models.PROTECT, null=True, blank=True)
    l_3 = models.ForeignKey(L_3, on_delete=models.PROTECT, null=True, blank=True)
    l_4 = models.ForeignKey(L_4, on_delete=models.PROTECT, null=True, blank=True)
    l_5 = models.ForeignKey(L_5, on_delete=models.PROTECT, null=True, blank=True)

    def __str__(self):
        return str(self.user)
    class Meta:
        verbose_name="User_Level"


@receiver(post_save, sender=User)
def creat_level(sender, instance, created, **kwargs):
    if created:
        User_Level.objects.create(user=instance)


class User_ContractPermission(models.Model):

    choice = [
        ('Yes', 'Yes'),
        ('NO', 'No'),
    ]
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    contract_app = models.CharField(max_length=250, choices=choice, null=True, blank=True)
    add_new_contract = models.CharField(max_length=250, choices=choice, null=True, blank=True)
    update_contract_step_1 = models.CharField(max_length=250, choices=choice, null=True, blank=True)
    check_contract_step_2 = models.CharField(max_length=250, choices=choice, null=True, blank=True)
    cs_check_contract_step_3 = models.CharField(max_length=250, choices=choice, null=True, blank=True)
    tcta_check_contract_step_4 = models.CharField(max_length=250, choices=choice, null=True, blank=True)
    evp_check_contract_step_5 = models.CharField(max_length=250, choices=choice, null=True, blank=True)
    ceo_check_contract_step_6 = models.CharField(max_length=250, choices=choice, null=True, blank=True)
    print_contract_step_7 = models.CharField(max_length=250, choices=choice, null=True, blank=True)
    cs_check_contract_step_8 = models.CharField(max_length=250, choices=choice, null=True, blank=True)
    final_preview_contract_step_9 = models.CharField(max_length=250, choices=choice, null=True, blank=True)
    final_assignment_contract_step_10 = models.CharField(max_length=250, choices=choice, null=True, blank=True)
    contract_detail = models.CharField(max_length=250, choices=choice, null=True, blank=True)
    contract_report = models.CharField(max_length=250, choices=choice, null=True, blank=True)

    def __str__(self):
        return str(self.user)
    class Meta:
        verbose_name="User_ContractPermission"


@receiver(post_save, sender=User)
def creat_ContractPermission(sender, instance, created, **kwargs):
    if created:
        User_ContractPermission.objects.create(user=instance)


class User_TenderPermission(models.Model):

    choice = [
        ('Yes', 'Yes'),
        ('NO', 'No'),
    ]
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    tender_app = models.CharField(max_length=250, choices=choice, null=True, blank=True)
    add_new_tender = models.CharField(max_length=250, choices=choice, null=True, blank=True)
    update_tender_detail = models.CharField(max_length=250, choices=choice, null=True, blank=True)
    tender_detail = models.CharField(max_length=250, choices=choice, null=True, blank=True)
    tender_report = models.CharField(max_length=250, choices=choice, null=True, blank=True)

    def __str__(self):
        return str(self.user)
    class Meta:
        verbose_name="User_TenderPermission"


@receiver(post_save, sender=User)
def creat_TenderPermission(sender, instance, created, **kwargs):
    if created:
        User_TenderPermission.objects.create(user=instance)


class User_ProjectPermission(models.Model):

    choice = [
        ('Yes', 'Yes'),
        ('NO', 'No'),
    ]
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    project_app = models.CharField(max_length=250, choices=choice, null=True, blank=True)
    add_new_project = models.CharField(max_length=250, choices=choice, null=True, blank=True)
    update_project_detail = models.CharField(max_length=250, choices=choice, null=True, blank=True)
    project_detail = models.CharField(max_length=250, choices=choice, null=True, blank=True)
    project_report = models.CharField(max_length=250, choices=choice, null=True, blank=True)

    def __str__(self):
        return str(self.user)
    class Meta:
        verbose_name="User_ProjectPermission"


@receiver(post_save, sender=User)
def creat_ProjectPermission(sender, instance, created, **kwargs):
    if created:
        User_ProjectPermission.objects.create(user=instance)