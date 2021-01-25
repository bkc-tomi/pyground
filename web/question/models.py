import datetime

from django.db    import models
from django.utils import timezone

# ユーザーモデル
from user.models import User

"""
--------------------------------------------------------------------------
テーブル:質問テーブル
--------------------------------------------------------------------------
"""
class Question(models.Model):
    """
    ----------------------------------------------------------------------
    インスタンス変数
    ----------------------------------------------------------------------
    テーブルカラムのモデルを定義
    target_user    : 対象ユーザー
    name           : 問題名
    question_text  : 問題文
    question_input : 入力
    question_output: 出力
    default_code   : コード
    create_at      : 作成日
    udpate_at      : 更新日
    ----------------------------------------------------------------------
    """
    target_user     = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="対象ユーザー")
    name            = models.CharField(max_length=255, null=False, verbose_name="問題名")
    question_text   = models.TextField(verbose_name="問題文")
    question_input  = models.TextField(default="", verbose_name="入力")
    question_output = models.TextField(default="", verbose_name="出力")
    default_code    = models.TextField(default="", verbose_name="コード")
    create_at       = models.DateTimeField(auto_now=True, null=False, verbose_name="作成日")
    update_at       = models.DateTimeField(auto_now_add=True, null=False, verbose_name="更新日")

    """
    ----------------------------------------------------------------------
    出力文定義関数
    ----------------------------------------------------------------------

    出力：問題名

    ----------------------------------------------------------------------
    """
    def __str__(self):
        return self.name

"""
--------------------------------------------------------------------------
テーブル:正解者テーブル
--------------------------------------------------------------------------
"""
class Correcter(models.Model):
    """
    ----------------------------------------------------------------------
    インスタンス変数
    ----------------------------------------------------------------------
    テーブルカラムのモデルを定義
    target_question : 対象問題
    correct_user    : 対象ユーザー
    create_at       : 作成日
    ----------------------------------------------------------------------
    """
    target_question = models.ForeignKey(Question, on_delete=models.CASCADE, verbose_name="対象問題")
    correct_user    = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="対象ユーザー")
    create_at       = models.DateTimeField(auto_now=True, null=False, verbose_name="作成日")

    """
    ----------------------------------------------------------------------
    出力文定義関数
    ----------------------------------------------------------------------

    出力：問題ID、正解者ID
    
    ----------------------------------------------------------------------
    """
    def __str__(self):
        return str(self.correct_user) + " is correct question:" + str(self.target_question)