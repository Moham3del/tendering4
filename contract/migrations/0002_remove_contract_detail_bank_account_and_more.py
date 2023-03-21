# Generated by Django 4.1.7 on 2023-03-06 20:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contract', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contract_detail',
            name='bank_account',
        ),
        migrations.AlterField(
            model_name='contract_detail',
            name='second_party_representative',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='contract_detail',
            name='tax_number',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='contract_detail',
            name='zakat_Income_certificate',
            field=models.FileField(default=0, upload_to='files'),
            preserve_default=False,
        ),
    ]
