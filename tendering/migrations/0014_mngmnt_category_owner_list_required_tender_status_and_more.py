# Generated by Django 4.1.1 on 2023-02-05 13:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tendering', '0013_rename_bid_opening_date_t_detail_insurance_letter_date_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Mngmnt_category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='owner_list',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='required',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='tender_status',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
            ],
        ),
        migrations.RemoveField(
            model_name='t_detail',
            name='initial_guarantee_required',
        ),
        migrations.AlterField(
            model_name='t_detail',
            name='insurance_Required',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='tendering.required'),
        ),
        migrations.AlterField(
            model_name='t_detail',
            name='management',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='tendering.mngmnt_category'),
        ),
        migrations.AlterField(
            model_name='t_detail',
            name='owner',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='tendering.owner_list'),
        ),
        migrations.AlterField(
            model_name='t_detail',
            name='t_status',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='tendering.tender_status'),
        ),
    ]
