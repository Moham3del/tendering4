# Generated by Django 4.1.1 on 2023-02-05 20:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tendering', '0020_remove_t_detail_tt_status_alter_t_detail_t_status'),
    ]

    operations = [
        migrations.DeleteModel(
            name='tender_status',
        ),
    ]
