# Generated by Django 2.2.17 on 2021-06-09 12:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('src_code', '0011_auto_20210608_1211'),
    ]

    operations = [
        migrations.AddField(
            model_name='detail',
            name='tag',
            field=models.ManyToManyField(blank=True, related_name='tags', to='src_code.Post'),
        ),
    ]