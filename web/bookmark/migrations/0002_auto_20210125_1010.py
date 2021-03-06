# Generated by Django 3.1.5 on 2021-01-25 01:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('question', '0001_initial'),
        ('bookmark', '0001_initial'),
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='bookmark',
            name='target_question',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='question.question', verbose_name='対象問題'),
        ),
        migrations.AddField(
            model_name='bookmark',
            name='target_user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.user', verbose_name='対象ユーザー'),
        ),
    ]
