# Generated by Django 3.1.3 on 2021-09-14 09:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0002_leaveapplication'),
    ]

    operations = [
        migrations.AlterField(
            model_name='leaveapplication',
            name='from_date',
            field=models.CharField(max_length=322),
        ),
        migrations.AlterField(
            model_name='leaveapplication',
            name='to_date',
            field=models.CharField(max_length=322),
        ),
    ]
