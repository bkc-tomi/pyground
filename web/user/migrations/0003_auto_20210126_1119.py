# Generated by Django 3.1.5 on 2021-01-26 02:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_auto_20210125_1554'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='create_at',
        ),
        migrations.RemoveField(
            model_name='user',
            name='update_at',
        ),
        migrations.AddField(
            model_name='user',
            name='udpate_at',
            field=models.DateTimeField(auto_now=True, verbose_name='更新日'),
        ),
    ]
