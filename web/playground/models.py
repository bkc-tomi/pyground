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
    name        : コード名
    code        : 対象コード
    update_at   : 更新日
    ----------------------------------------------------------------------
    """
    target_user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="対象ユーザー")
    name        = models.CharField(max_length=255, null=True, verbose_name="コード名")
    code        = models.TextField(verbose_name="対象コード")
    update_at   = models.DateTimeField(auto_now=True, null=False, verbose_name="更新日")

    """
    ----------------------------------------------------------------------
    出力文定義関数
    ----------------------------------------------------------------------

    出力：コード

    ----------------------------------------------------------------------
    """
    def __str__(self):
        return self.name