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
    プレイグランド／プレイグランド
    ----------------------------------------------------------------------
    """

    def test_redirect(self):
        """
        ----------------------------------------------------------------
        ** テスト内容 **
        ユーザーがログインしてない状態でのリダイレクト

        ** 入力値と期待値 **
        リダイレクト先: top:top
        ----------------------------------------------------------------
        """
        # データ作成
        user = self.make_user("usr1", "aa@bb.jp", "1234")

        # テスト実行
        response = self.client.get(reverse('bookmark:index', args=(user.id, )))
        self.assertRedirects(
            response,
            expected_url=reverse('top:top'),
            status_code=302,
            target_status_code=200,
        )

class RunViewTest(CommonTestCase):
    """
    ----------------------------------------------------------------------
    プレイグランド／実行処理
    ----------------------------------------------------------------------
    """

    def test_redirect(self):
        """
        ----------------------------------------------------------------
        ** テスト内容 **
        ユーザーがログインしてない状態でのリダイレクト

        ** 入力値と期待値 **
        リダイレクト先: top:top
        ----------------------------------------------------------------
        """
        # データ作成
        user = self.make_user("usr1", "aa@bb.jp", "1234")

        # テスト実行
        response = self.client.get(reverse('bookmark:index', args=(user.id, )))
        self.assertRedirects(
            response,
            expected_url=reverse('top:top'),
            status_code=302,
            target_status_code=200,
        )

class EditViewTest(CommonTestCase):
    """
    ----------------------------------------------------------------------
    プレイグランド／コード編集
    ----------------------------------------------------------------------
    """

    def test_redirect(self):
        """
        ----------------------------------------------------------------
        ** テスト内容 **
        ユーザーがログインしてない状態でのリダイレクト

        ** 入力値と期待値 **
        リダイレクト先: top:top
        ----------------------------------------------------------------
        """
        # データ作成
        user = self.make_user("usr1", "aa@bb.jp", "1234")

        # テスト実行
        response = self.client.get(reverse('bookmark:index', args=(user.id, )))
        self.assertRedirects(
            response,
            expected_url=reverse('top:top'),
            status_code=302,
            target_status_code=200,
        )

class RunEditViewTest(CommonTestCase):
    """
    ----------------------------------------------------------------------
    プレイグランド／編集実行処理
    ----------------------------------------------------------------------
    """

    def test_redirect(self):
        """
        ----------------------------------------------------------------
        ** テスト内容 **
        ユーザーがログインしてない状態でのリダイレクト

        ** 入力値と期待値 **
        リダイレクト先: top:top
        ----------------------------------------------------------------
        """
        # データ作成
        user = self.make_user("usr1", "aa@bb.jp", "1234")

        # テスト実行
        response = self.client.get(reverse('bookmark:index', args=(user.id, )))
        self.assertRedirects(
            response,
            expected_url=reverse('top:top'),
            status_code=302,
            target_status_code=200,
        )

class QuestionViewTest(CommonTestCase):
    """
    ----------------------------------------------------------------------
    プレイグランド／問題ページ
    ----------------------------------------------------------------------
    """

    def test_redirect(self):
        """
        ----------------------------------------------------------------
        ** テスト内容 **
        ユーザーがログインしてない状態でのリダイレクト

        ** 入力値と期待値 **
        リダイレクト先: top:top
        ----------------------------------------------------------------
        """
        # データ作成
        user = self.make_user("usr1", "aa@bb.jp", "1234")

        # テスト実行
        response = self.client.get(reverse('bookmark:index', args=(user.id, )))
        self.assertRedirects(
            response,
            expected_url=reverse('top:top'),
            status_code=302,
            target_status_code=200,
        )

class RunQuestionViewTest(CommonTestCase):
    """
    ----------------------------------------------------------------------
    プレイグランド／問題処理
    ----------------------------------------------------------------------
    """

    def test_redirect(self):
        """
        ----------------------------------------------------------------
        ** テスト内容 **
        ユーザーがログインしてない状態でのリダイレクト

        ** 入力値と期待値 **
        リダイレクト先: top:top
        ----------------------------------------------------------------
        """
        # データ作成
        user = self.make_user("usr1", "aa@bb.jp", "1234")

        # テスト実行
        response = self.client.get(reverse('bookmark:index', args=(user.id, )))
        self.assertRedirects(
            response,
            expected_url=reverse('top:top'),
            status_code=302,
            target_status_code=200,
        )

class SaveViewTest(CommonTestCase):
    """
    ----------------------------------------------------------------------
    プレイグランド／保存処理
    ----------------------------------------------------------------------
    """

    def test_redirect(self):
        """
        ----------------------------------------------------------------
        ** テスト内容 **
        ユーザーがログインしてない状態でのリダイレクト

        ** 入力値と期待値 **
        リダイレクト先: top:top
        ----------------------------------------------------------------
        """
        # データ作成
        user = self.make_user("usr1", "aa@bb.jp", "1234")

        # テスト実行
        response = self.client.get(reverse('bookmark:index', args=(user.id, )))
        self.assertRedirects(
            response,
            expected_url=reverse('top:top'),
            status_code=302,
            target_status_code=200,
        )

class UpdateViewTest(CommonTestCase):
    """
    ----------------------------------------------------------------------
    プレイグランド／更新処理
    ----------------------------------------------------------------------
    """

    def test_redirect(self):
        """
        ----------------------------------------------------------------
        ** テスト内容 **
        ユーザーがログインしてない状態でのリダイレクト

        ** 入力値と期待値 **
        リダイレクト先: top:top
        ----------------------------------------------------------------
        """
        # データ作成
        user = self.make_user("usr1", "aa@bb.jp", "1234")

        # テスト実行
        response = self.client.get(reverse('bookmark:index', args=(user.id, )))
        self.assertRedirects(
            response,
            expected_url=reverse('top:top'),
            status_code=302,
            target_status_code=200,
        )