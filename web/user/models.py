import datetime

from django.db    import models
from django.utils import timezone

"""
--------------------------------------------------------------------------
テーブル:ユーザーテーブル
--------------------------------------------------------------------------
"""
class User(models.Model):
    """
    ----------------------------------------------------------------------
    インスタンス変数
    ----------------------------------------------------------------------
    テーブルカラムのモデルを定義
    username   : ユーザー名
    email      : メールアドレス
    password   : パスワード
    image_icon : ユーザーアイコン
    create_at  : 作成日
    update_at  : 更新日
    ----------------------------------------------------------------------
    """
    username  = models.CharField(max_length=100,blank=False, verbose_name="ユーザー名")
    email     = models.EmailField(blank=False, verbose_name="メールアドレス")
    password  = models.CharField(max_length=255, blank=False, verbose_name="パスワード")
    image_icon   = models.ImageField(
        upload_to='user_icon/',
        default='user_icon/user_icon.png',
        blank=True,
        verbose_name="ユーザーアイコン",
    )
    create_at = models.DateTimeField(auto_now=True, verbose_name="作成日")
    update_at = models.DateTimeField(auto_now_add=True, verbose_name="更新日")

    """
    ----------------------------------------------------------------------
    出力文定義関数
    ----------------------------------------------------------------------
    
    出力：ユーザー名

    ----------------------------------------------------------------------
    """
    def __str__(self):
        return self.username


"""
--------------------------------------------------------------------------
テーブル:プロフィールテーブル
--------------------------------------------------------------------------
"""
class Profile(models.Model):
    """
    ----------------------------------------------------------------------
    インスタンス変数
    ----------------------------------------------------------------------
    テーブルカラムのモデルを定義
    target_user  : 対象ユーザー
    profile_text : プロフィール文
    publish      : 公開設定
    ----------------------------------------------------------------------
    """
    target_user  = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name="対象ユーザー")
    profile_text = models.CharField(max_length=255, verbose_name="プロフィール文")
    publish      = models.BooleanField(default=False, verbose_name='公開設定')

    """
    ----------------------------------------------------------------------
    出力文定義関数
    ----------------------------------------------------------------------
    
    出力：プロフィール文

    ----------------------------------------------------------------------
    """
    def __str__(self):
        return self.profile_text
