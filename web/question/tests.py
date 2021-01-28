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

class QuestionsViewTest(CommonTestCase):
    """
    ----------------------------------------------------------------------
    問題／一覧ページ
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

class ManageViewTest(CommonTestCase):
    """
    ----------------------------------------------------------------------
    問題／管理ページ
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

class DetailViewTest(CommonTestCase):
    """
    ----------------------------------------------------------------------
    問題／詳細ページ
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

class CreateViewTest(CommonTestCase):
    """
    ----------------------------------------------------------------------
    問題／新規作成ページ
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

class RunCreateViewTest(CommonTestCase):
    """
    ----------------------------------------------------------------------
    問題／新規作成処理
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
    問題／編集ページ
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
    問題／編集処理
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