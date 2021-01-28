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
    ----------------------------------------------------------------
    ブックマーク/一覧表示
    ----------------------------------------------------------------
    """

    def test_show_bookmark(self):
        """
        ----------------------------------------------------------------
        ** テスト内容 **
        ２つのブックマークを表示する

        ** 入力値と期待値 **
        user_id      : 1
        bookmark_list: "{'id': 1, 'question': <Question: 1>}", "{'id': 2, 'question': <Question: 2>}"
        ----------------------------------------------------------------
        """
        # データ作成
        user = self.make_user("usr1", "aa@bb.jp", "1234")
        q1 = self.make_question(1, user.id)
        q2 = self.make_question(2, user.id)

        self.make_login_user(user.id, user.username)

        self.make_bookmark(user.id, q1.id)
        self.make_bookmark(user.id, q2.id)

        # テスト実行
        response = self.client.get(reverse('bookmark:index', args=(user.id, )))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            response.context['user_id'],
            user.id,
        )
        self.assertQuerysetEqual(
            response.context['bookmark_list'],
            ["{'id': 1, 'question': <Question: 1>}", "{'id': 2, 'question': <Question: 2>}"],
        )

    def test_no_bookmark(self):
        """
        ----------------------------------------------------------------
        ** テスト内容 **
        ブックマークがない場合の処理

        ** 入力値と期待値 **
        user_id      : 1
        bookmark_list: []
        ----------------------------------------------------------------
        """
        # データ作成
        user = self.make_user("usr1", "aa@bb.jp", "1234")
        q1 = self.make_question(1, user.id)
        q2 = self.make_question(2, user.id)

        self.make_login_user(user.id, user.username)

        # テスト実行
        response = self.client.get(reverse('bookmark:index', args=(user.id, )))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            response.context['user_id'],
            user.id,
        )
        self.assertQuerysetEqual(
            response.context['bookmark_list'],
            [],
        )

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

class RunBookmarkViewTest(CommonTestCase):
    """
    ----------------------------------------------------------------------
    ブックマーク／ブックマーク処理
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
    ブックマーク／ブックマーク解除
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