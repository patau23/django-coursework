# Generated by Django 3.2 on 2021-04-25 16:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0010_auto_20210424_0629'),
    ]

    operations = [
        migrations.AlterField(
            model_name='scholarship_fund',
            name='scholarship_amount',
            field=models.PositiveIntegerField(blank=True, null=True, verbose_name='Сумма стипендий'),
        ),
    ]
