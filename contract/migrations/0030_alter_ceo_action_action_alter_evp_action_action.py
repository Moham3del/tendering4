# Generated by Django 4.1.7 on 2023-03-17 00:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contract', '0029_alter_assignmnt_action_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ceo_action',
            name='action',
            field=models.CharField(choices=[('قبول', 'قبول'), ('ملاحظات', 'ملاحظات')], max_length=250),
        ),
        migrations.AlterField(
            model_name='evp_action',
            name='action',
            field=models.CharField(choices=[('قبول', 'قبول'), ('ملاحظات', 'ملاحظات')], max_length=250),
        ),
    ]