# Generated by Django 4.1.7 on 2023-03-13 21:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_user_contractpermission_main_index'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='user_profile',
            options={'ordering': ['project_name'], 'verbose_name': 'profile'},
        ),
    ]