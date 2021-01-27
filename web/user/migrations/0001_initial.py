# Generated by Django 3.1.5 on 2021-01-25 01:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=100, verbose_name='ユーザー名')),
                ('email', models.EmailField(max_length=254, verbose_name='メールアドレス')),
                ('password', models.CharField(max_length=255, verbose_name='パスワード')),
                ('image_icon', models.ImageField(blank=True, default='user_icon/user_icon.png', null=True, upload_to='user_icon/', verbose_name='ユーザーアイコン')),
                ('create_at', models.DateTimeField(auto_now=True, verbose_name='作成日')),
                ('update_at', models.DateTimeField(auto_now_add=True, verbose_name='更新日')),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profile_text', models.CharField(max_length=255, verbose_name='プロフィール文')),
                ('publish', models.BooleanField(default=False, verbose_name='公開設定')),
                ('target_user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='user.user', verbose_name='対象ユーザー')),
            ],
        ),
    ]