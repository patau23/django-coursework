# Generated by Django 3.2 on 2021-04-25 21:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0012_alter_types_of_education_education_type_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fellow',
            name='student_code',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='main.student', verbose_name='Код студента'),
        ),
    ]
