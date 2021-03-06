# Generated by Django 3.1.3 on 2021-09-14 09:32

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='LeaveApplication',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('appied_date', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('reason', models.CharField(max_length=500)),
                ('from_date', models.DateTimeField()),
                ('to_date', models.DateTimeField()),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='students.student_data')),
            ],
        ),
    ]
