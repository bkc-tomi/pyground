# Generated by Django 3.1.5 on 2021-01-26 02:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('question', '0003_question_default_code'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='correcter',
            name='create_at',
        ),
        migrations.RemoveField(
            model_name='question',
            name='create_at',
        ),
        migrations.AddField(
            model_name='correcter',
            name='update_at',
            field=models.DateTimeField(auto_now=True, verbose_name='更新日'),
        ),
        migrations.AlterField(
            model_name='question',
            name='update_at',
            field=models.DateTimeField(auto_now=True, verbose_name='更新日'),
        ),
    ]
