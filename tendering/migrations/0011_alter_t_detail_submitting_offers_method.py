# Generated by Django 4.1.1 on 2023-01-27 17:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tendering', '0010_alter_t_detail_rmnng_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='t_detail',
            name='submitting_offers_method',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
    ]
