# Generated by Django 3.1.4 on 2021-01-04 08:27

from django.db import migrations, models
import django_countries.fields


class Migration(migrations.Migration):

    dependencies = [
        ('employee_details_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employeedetails',
            name='country',
            field=django_countries.fields.CountryField(max_length=2, null=True),
        ),
        migrations.AlterField(
            model_name='employeedetails',
            name='email_id',
            field=models.EmailField(max_length=256, null=True),
        ),
        migrations.AlterField(
            model_name='employeedetails',
            name='first_name',
            field=models.CharField(max_length=256, null=True),
        ),
        migrations.AlterField(
            model_name='employeedetails',
            name='last_name',
            field=models.CharField(max_length=256, null=True),
        ),
        migrations.AlterField(
            model_name='employeedetails',
            name='mobile_number',
            field=models.CharField(max_length=10, null=True),
        ),
    ]
