# Generated by Django 2.2.17 on 2021-06-14 12:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('src_code', '0021_detail_message'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='detail',
            name='message',
        ),
    ]
