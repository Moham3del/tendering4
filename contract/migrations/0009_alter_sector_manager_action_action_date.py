# Generated by Django 4.1.7 on 2023-03-08 19:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contract', '0008_check_contract_action_action_file'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sector_manager_action',
            name='action_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]