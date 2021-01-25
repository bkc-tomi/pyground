import datetime

from django.db    import models
from django.utils import timezone

# ユーザーモデル
from user.models import User

"""
--------------------------------------------------------------------------
テーブル:コードテーブル
--------------------------------------------------------------------------
"""
class Code(models.Model):
    """
    ----------------------------------------------------------------------
    インスタンス変数
    ----------------------------------------------------------------------
    テーブルカラムのモデルを定義
    target_user : 対象ユーザー
    code        : 対象コード
    create_at   : 作成日
    update_at   : 更新日
    ----------------------------------------------------------------------
    """
    target_user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="対象ユーザー")
    code        = models.TextField(verbose_name="対象コード")
    create_at   = models.DateTimeField(auto_now=True, null=False, verbose_name="作成日")
    update_at   = models.DateTimeField(auto_now_add=True, null=False, verbose_name="更新日")

    """
    ----------------------------------------------------------------------
    出力文定義関数
    ----------------------------------------------------------------------

    出力：コード

    ----------------------------------------------------------------------
    """
    def __str__(self):
        return self.code