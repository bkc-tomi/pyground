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

class RegisterViewTest(CommonTestCase):
    """
    ----------------------------------------------------------------------
    ユーザー／登録ページ
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

class RegisterCompleteViewTest(CommonTestCase):
    """
    ----------------------------------------------------------------------
    ユーザー／登録完了ページ
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

class RunRegisterViewTest(CommonTestCase):
    """
    ----------------------------------------------------------------------
    ユーザー／登録処理
    ----------------------------------------------------------------------
    """

class LoginViewTest(CommonTestCase):
    """
    ----------------------------------------------------------------------
    ユーザー／ログインページ
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

class RunLoginViewTest(CommonTestCase):
    """
    ----------------------------------------------------------------------
    ユーザー／ログイン処理
    ----------------------------------------------------------------------
    """

class RunLogoutViewTest(CommonTestCase):
    """
    ----------------------------------------------------------------------
    ユーザー／ログアウト処理
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

class WithdrawalViewTest(CommonTestCase):
    """
    ----------------------------------------------------------------------
    ユーザー／退会ページ
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

class RunWithdrawalViewTest(CommonTestCase):
    """
    ----------------------------------------------------------------------
    ユーザー／退会処理
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
    ユーザー／プロフィール詳細ページ
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
    ユーザー／プロフィール新規作成ページ
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
    ユーザー／プロフィール新規作成処理
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
    ユーザー／プロフィール編集ページ
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
    ユーザー／プロフィール編集処理
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

class IndexViewTest(CommonTestCase):
    """
    ----------------------------------------------------------------------
    ユーザー／ユーザー一覧ページ
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
