# Generated by Django 3.2 on 2021-04-25 23:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0019_alter_accrual_student_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='types_of_scholarship',
            name='scholarship_type_name',
            field=models.CharField(choices=[('Обычная', 'common'), ('Повышенная', 'increased'), ('Именная', 'nominal'), ('Социальная', 'social')], default='Обычная', max_length=25, verbose_name='Код вида стипендии'),
        ),
    ]
