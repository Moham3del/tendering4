# Generated by Django 4.1.7 on 2023-03-19 17:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contract', '0037_assignmnt_action_contract_no_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contract_detail',
            old_name='sgnlsectorManager_note',
            new_name='sgnlsectorManager_action_note',
        ),
    ]