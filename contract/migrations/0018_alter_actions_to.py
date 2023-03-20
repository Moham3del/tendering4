# Generated by Django 4.1.7 on 2023-03-13 22:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0010_alter_user_profile_options'),
        ('contract', '0017_actions_extra_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='actions',
            name='to',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='Action_to', to='main.user_profile'),
            preserve_default=False,
        ),
    ]