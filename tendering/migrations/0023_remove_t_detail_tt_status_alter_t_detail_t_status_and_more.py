# Generated by Django 4.1.1 on 2023-02-05 20:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tendering', '0022_tender_status_t_detail_tt_status_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='t_detail',
            name='tt_status',
        ),
        migrations.AlterField(
            model_name='t_detail',
            name='t_status',
            field=models.CharField(blank=True, choices=[('جارية', 'جارية'), ('تم التقديم', 'تم التقديم'), ('منتهية', 'منتهية'), ('ملغية', 'ملغية')], max_length=250, null=True),
        ),
        migrations.DeleteModel(
            name='tender_status',
        ),
    ]
