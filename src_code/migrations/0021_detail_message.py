# Generated by Django 2.2.17 on 2021-06-11 11:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('src_code', '0020_auto_20210611_1125'),
    ]

    operations = [
        migrations.AddField(
            model_name='detail',
            name='message',
            field=models.ManyToManyField(blank=True, to='src_code.Message'),
        ),
    ]
