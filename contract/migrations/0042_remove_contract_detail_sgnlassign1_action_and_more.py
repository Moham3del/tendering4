# Generated by Django 4.1.7 on 2023-03-20 15:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contract', '0041_alter_assignmnt_action_action_no_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contract_detail',
            name='sgnlassign1_action',
        ),
        migrations.RemoveField(
            model_name='contract_detail',
            name='sgnlassign1_actionFile',
        ),
        migrations.RemoveField(
            model_name='contract_detail',
            name='sgnlassign1_action_creator',
        ),
        migrations.RemoveField(
            model_name='contract_detail',
            name='sgnlassign1_action_date',
        ),
    ]