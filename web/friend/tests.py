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

class FollowViewTest(CommonTestCase):
    """
    ----------------------------------------------------------------------
    フレンド／フォロー一覧
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


class FollowerViewTest(CommonTestCase):
    """
    ----------------------------------------------------------------------
    フレンド／フォロワー一覧
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


class RunFollowViewTest(CommonTestCase):
    """
    ----------------------------------------------------------------------
    フレンド／フォロー処理
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


class ReleaseViewTest(CommonTestCase):
    """
    ----------------------------------------------------------------------
    フレンド／フォロー解除処理
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


class PermitViewTest(CommonTestCase):
    """
    ----------------------------------------------------------------------
    フレンド／フォロー許可ページ
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


class RunPermitViewTest(CommonTestCase):
    """
    ----------------------------------------------------------------------
    フレンド／フォロー許可処理
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


class RunNoPermitViewTest(CommonTestCase):
    """
    ----------------------------------------------------------------------
    フレンド／フォロー不許可処理
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