# Generated by Django 2.2.17 on 2021-06-11 11:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('src_code', '0017_auto_20210611_1121'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='message',
            name='connection',
        ),
    ]
