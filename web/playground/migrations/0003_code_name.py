# Generated by Django 3.1.5 on 2021-01-27 01:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('playground', '0002_auto_20210126_1119'),
    ]

    operations = [
        migrations.AddField(
            model_name='code',
            name='name',
            field=models.CharField(max_length=255, null=True, verbose_name='コード名'),
        ),
    ]
