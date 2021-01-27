import datetime

from django.db    import models
from django.utils import timezone

# ユーザーモデル
from user.models     import User
# 質問モデル
from question.models import Question

"""
--------------------------------------------------------------------------
テーブル:ブックマークテーブル
--------------------------------------------------------------------------
"""
class Bookmark(models.Model):
    """
    ----------------------------------------------------------------------
    インスタンス変数
    ----------------------------------------------------------------------
    テーブルカラムのモデルを定義
    target_user    : 対象ユーザー
    target_question: 対象問題
    update_at      : 更新日
    ----------------------------------------------------------------------
    """
    target_user     = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="対象ユーザー")
    target_question = models.ForeignKey(Question, on_delete=models.CASCADE, verbose_name="対象問題")
    update_at       = models.DateTimeField(auto_now=True, null=False, verbose_name="更新日")

    """
    ----------------------------------------------------------------------
    出力文定義関数
    ----------------------------------------------------------------------
    
    出力：ユーザーID、問題ID

    ----------------------------------------------------------------------
    """
    def __str__(self):
        return str(self.target_user) + " is bookmark " + str(self.target_question) 
