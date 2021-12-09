# Generated by Django 2.0.5 on 2021-04-04 01:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20210402_0143'),
    ]

    operations = [
        migrations.CreateModel(
            name='Accrual',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_of_scholarship_accrual', models.DateField(blank=True, null=True)),
                ('amount_of_money', models.DecimalField(blank=True, decimal_places=10, max_digits=10, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Fellow',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('beginning_of_the_accrual_period', models.DateField(blank=True, null=True)),
                ('ending_of_the_accrual_period', models.DateField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('student_code', models.IntegerField(primary_key=True, serialize=False)),
                ('student_name', models.CharField(max_length=200)),
                ('personal_reckoning_number', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Types_of_Scholarship',
            fields=[
                ('scholarship_type_code', models.IntegerField(primary_key=True, serialize=False)),
                ('scholarship_type_name', models.CharField(max_length=25)),
                ('amount_of_money', models.DecimalField(decimal_places=10, max_digits=10)),
            ],
        ),
        migrations.DeleteModel(
            name='Accruals',
        ),
        migrations.DeleteModel(
            name='Fellows',
        ),
        migrations.DeleteModel(
            name='Students',
        ),
        migrations.DeleteModel(
            name='Types_of_Scholarships',
        ),
        migrations.RemoveField(
            model_name='bank',
            name='id',
        ),
        migrations.RemoveField(
            model_name='department',
            name='id',
        ),
        migrations.RemoveField(
            model_name='faculty',
            name='id',
        ),
        migrations.RemoveField(
            model_name='group',
            name='id',
        ),
        migrations.RemoveField(
            model_name='scholarship_fund',
            name='id',
        ),
        migrations.RemoveField(
            model_name='staff',
            name='id',
        ),
        migrations.RemoveField(
            model_name='types_of_education',
            name='id',
        ),
        migrations.AlterField(
            model_name='bank',
            name='bank_code',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='department',
            name='department_code',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='department',
            name='department_head_code',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='main.Staff'),
        ),
        migrations.AlterField(
            model_name='department',
            name='faculty_code',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Faculty'),
        ),
        migrations.AlterField(
            model_name='faculty',
            name='deanery_employee_code',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='main.Staff'),
        ),
        migrations.AlterField(
            model_name='faculty',
            name='faculty_code',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='group',
            name='group_code',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='group',
            name='issuing_department_code',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Department'),
        ),
        migrations.AlterField(
            model_name='group',
            name='сurator_code',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='main.Staff'),
        ),
        migrations.AlterField(
            model_name='scholarship_fund',
            name='faculty_code',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='main.Faculty'),
        ),
        migrations.AlterField(
            model_name='staff',
            name='сurator_code',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='types_of_education',
            name='education_type_code',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
        migrations.AddField(
            model_name='student',
            name='bank_code',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='main.Bank'),
        ),
        migrations.AddField(
            model_name='student',
            name='education_type_code',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Types_of_Education'),
        ),
        migrations.AddField(
            model_name='student',
            name='group_code',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Group'),
        ),
        migrations.AddField(
            model_name='fellow',
            name='scholarship_type_code',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='main.Types_of_Scholarship'),
        ),
        migrations.AddField(
            model_name='fellow',
            name='student_code',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Student'),
        ),
        migrations.AddField(
            model_name='accrual',
            name='student_code',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Student'),
        ),
    ]