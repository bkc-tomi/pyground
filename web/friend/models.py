import datetime

from django.db    import models
from django.utils import timezone

# ユーザーモデル
from user.models import User

"""
--------------------------------------------------------------------------
テーブル:フォローテーブル
--------------------------------------------------------------------------
"""
class Follow(models.Model):
    """
    ----------------------------------------------------------------------
    インスタンス変数
    ----------------------------------------------------------------------
    テーブルカラムのモデルを定義
    follow_user   : フォローしたユーザー
    followed_user : フォローされたユーザー
    create_at     : 作成日
    ----------------------------------------------------------------------
    """
    follow_user   = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="follow_user",
        verbose_name="フォローしたユーザー",
    )
    followed_user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="followed_user",
        verbose_name="フォローされたユーザー"
    )
    create_at     = models.DateTimeField(auto_now=True, null=False, verbose_name="作成日")

    """
    ----------------------------------------------------------------------
    出力文定義関数
    ----------------------------------------------------------------------

    出力：フォローユーザーID、フォローされたユーザーID

    ----------------------------------------------------------------------
    """
    def __str__(self):
        return str(self.follow_user) + "is following " + str(self.followed_user)


"""
--------------------------------------------------------------------------
テーブル:申請テーブル
--------------------------------------------------------------------------
"""
class Permit(models.Model):
    """
    ----------------------------------------------------------------------
    インスタンス変数
    ----------------------------------------------------------------------
    テーブルカラムのモデルを定義
    request_user : 申請ユーザー
    target_user  : 対象ユーザー
    create_at    : 作成日
    ----------------------------------------------------------------------
    """
    request_user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="request_user",
        verbose_name="申請ユーザー",
    )
    target_user  = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="target_user",
        verbose_name="対象ユーザー",
    )
    create_at    = models.DateTimeField(auto_now=True, null=False, verbose_name="作成日")

    """
    ----------------------------------------------------------------------
    出力文定義関数
    ----------------------------------------------------------------------
    
    出力：申請ユーザーID、申請されたユーザーID
    
    ----------------------------------------------------------------------
    """
    def __str__(self):
        return str(self.request_user) + " request following " + str(self.target_user)
