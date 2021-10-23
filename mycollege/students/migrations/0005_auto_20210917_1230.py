# Generated by Django 3.1.3 on 2021-09-17 07:00

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0004_studentfeedback'),
    ]

    operations = [
        migrations.AddField(
            model_name='studentfeedback',
            name='course',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.DO_NOTHING, to='students.course'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='studentfeedback',
            name='appied_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime),
        ),
        migrations.AlterField(
            model_name='studentfeedback',
            name='student',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='students.student_data'),
        ),
    ]
