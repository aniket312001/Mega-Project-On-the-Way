# Generated by Django 3.1.3 on 2021-10-10 04:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('admins', '0004_adminnotification'),
    ]

    operations = [
        migrations.RenameField(
            model_name='adminnotification',
            old_name='staff',
            new_name='admin',
        ),
    ]
