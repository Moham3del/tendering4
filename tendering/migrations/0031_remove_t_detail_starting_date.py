# Generated by Django 4.1.7 on 2023-03-14 14:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tendering', '0030_t_detail_publication_date_alter_t_detail_no_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='t_detail',
            name='starting_date',
        ),
    ]
