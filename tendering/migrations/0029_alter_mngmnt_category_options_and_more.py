# Generated by Django 4.1.6 on 2023-02-26 04:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tendering', '0028_remove_task_task_user_task_task_user'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='mngmnt_category',
            options={'ordering': ['name'], 'verbose_name': 'Management'},
        ),
        migrations.AlterModelOptions(
            name='owner_list',
            options={'ordering': ['name'], 'verbose_name': 'owner'},
        ),
        migrations.DeleteModel(
            name='Task',
        ),
    ]
