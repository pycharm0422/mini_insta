# Generated by Django 2.2.17 on 2021-06-15 14:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('src_code', '0027_auto_20210615_1446'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='sender',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
    ]
