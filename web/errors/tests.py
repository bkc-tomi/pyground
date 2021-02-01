from pyground.tests import CommonTestCase
from django.urls    import reverse


# モデル
from bookmark.models   import Bookmark
from friend.models     import Follow, Permit
from playground.models import Code
from question.models   import Question, Correcter
from user.models       import User, Profile

# templateのあるviewのみテスト
# POST処理等は取りあえすしない

class IndexViewTest(CommonTestCase):
    """
    ----------------------------------------------------------------------
    エラーページ
    ----------------------------------------------------------------------
    """
    def test_show_errors(self):
        """
        ----------------------------------------------------------------
        ** テスト内容 **
        作成したエラーを表示する

        ** 入力値と期待値 **
        errors: [
            
        ]
        ----------------------------------------------------------------
        """
        # データ作成 ------------------------------------------------

        # 実行 -----------------------------------------------------

        # テスト ---------------------------------------------------