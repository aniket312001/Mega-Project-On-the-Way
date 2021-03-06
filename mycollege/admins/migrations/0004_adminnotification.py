# Generated by Django 3.1.3 on 2021-10-10 04:11

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('admins', '0003_delete_adminnotification'),
    ]

    operations = [
        migrations.CreateModel(
            name='AdminNotification',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('notification', models.CharField(max_length=100000)),
                ('date', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('staff', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='admins.admindata')),
            ],
        ),
    ]
