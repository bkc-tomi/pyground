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

        ** 入力値 **
        user_id
        ** 期待値 **
        user_id      : user.id
        bookmark_list: "{'id': 1, 'question': <Question: 1>}", "{'id': 2, 'question': <Question: 2>}"
        ----------------------------------------------------------------
        """
        # データ作成 ------------------------------------------------
        user = self.make_user("usr1", "aa@bb.jp", "1234")
        q1 = self.make_question(1, user.id)
        q2 = self.make_question(2, user.id)

        self.make_login_user(user.id, user.username)

        self.make_bookmark(user.id, q1.id)
        self.make_bookmark(user.id, q2.id)

        # 実行 -----------------------------------------------------
        response = self.client.get(reverse('bookmark:index', args=(user.id, )))

        # テスト ---------------------------------------------------
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

        ** 入力値 **
        user_id
        ** 期待値 **
        user_id      : user.id, bookmark_list: []
        ----------------------------------------------------------------
        """
        # データ作成 ------------------------------------------------
        user = self.make_user("usr1", "aa@bb.jp", "1234")
        q1 = self.make_question(1, user.id)
        q2 = self.make_question(2, user.id)

        self.make_login_user(user.id, user.username)

        # 実行 -----------------------------------------------------
        response = self.client.get(reverse('bookmark:index', args=(user.id, )))

        # テスト ---------------------------------------------------
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

        ** 入力値 **
        login_user
        ** 期待値 **
        リダイレクト先: top:top
        ----------------------------------------------------------------
        """
        # データ作成 ------------------------------------------------
        user = self.make_user("usr1", "aa@bb.jp", "1234")

        # 実行 -----------------------------------------------------
        response = self.client.get(reverse('bookmark:index', args=(user.id, )))

        # テスト ---------------------------------------------------
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

        ** 入力値 **
        login_user
        ** 期待値 **
        リダイレクト先: top:top
        ----------------------------------------------------------------
        """
        # データ作成 ------------------------------------------------
        user = self.make_user("usr1", "aa@bb.jp", "1234")
        q = self.make_question(1, user.id)

        # 実行 -----------------------------------------------------
        response = self.client.get(reverse('bookmark:run_bookmark', args=(q.id, )))

        # テスト ---------------------------------------------------
        self.assertRedirects(
            response,
            expected_url=reverse('top:top'),
            status_code=302,
            target_status_code=200,
        )
    
    def test_bookmark(self):
        """
        ----------------------------------------------------------------
        ** テスト内容 **
        ブックマークをする

        ** 入力値 **
        user_id, question_id
        ** 期待値 **
        該当するquestion_idのbookmarkレコードの数が一つ
        ----------------------------------------------------------------
        """
        # データの作成 --------------------------------------------
        user = self.make_user('usr1', 'aa@bb.jp', '0000')
        self.make_login_user(user.id, user.username)

        q = self.make_question(1, user.id)

        # 実行 --------------------------------------------------
        url = reverse('bookmark:run_bookmark', args=(q.id,))
        response = self.client.get(url)
        b_count = Bookmark.objects.filter(target_question_id = q.id).count()

        # テスト -------------------------------------------------
        self.assertEqual(response.status_code, 302)
        self.assertIs(b_count, 1)

    def test_bookmark_with_no_question(self):
        """
        ----------------------------------------------------------------
        ** テスト内容 **
        存在しないquestion_idでのブックマーク

        ** 入力値 **
        存在しないquestion_id
        ** 期待値 **
        bookmarkレコードが作成されないこと, エラーページへリダイレクト
        ----------------------------------------------------------------
        """
        # データの作成 --------------------------------------------
        user = self.make_user('usr1', 'aa@bb.jp', '0000')
        self.make_login_user(user.id, user.username)

        q = self.make_question(1, user.id)

        # 実行 --------------------------------------------------
        url = reverse('bookmark:run_bookmark', args=(q.id + 1,))
        response = self.client.get(url)
        b_count = Bookmark.objects.all().count()

        # テスト -------------------------------------------------
        self.assertRedirects(
            response,
            expected_url=reverse('errors:errors'),
            status_code=302,
            target_status_code=200,
        )
        self.assertIs(b_count, 0)



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

        ** 入力値 **
        login_user
        ** 期待値 **
        リダイレクト先: top:top
        ----------------------------------------------------------------
        """
        # データ作成 ------------------------------------------------
        u = self.make_user("usr1", "aa@bb.jp", "1234")
        q = self.make_question(1, u.id)
        b = self.make_bookmark(u.id, q.id)

        # 実行 -----------------------------------------------------
        response = self.client.get(reverse('bookmark:release', args=(b.id, )))

        # テスト ---------------------------------------------------
        self.assertRedirects(
            response,
            expected_url=reverse('top:top'),
            status_code=302,
            target_status_code=200,
        )

    def test_release(self):
        """
        ----------------------------------------------------------------
        ** テスト内容 **
        ブックマーク解除処理のテスト

        ** 入力値 **
        bookmark_id, login_user
        ** 期待値 **
        該当のbookmark_idのレコード数が0
        ----------------------------------------------------------------
        """
        # データ作成 ------------------------------------------------
        user = self.make_user('usr', 'aa@bb.jp', '0000')
        q = self.make_question(1, user.id)

        b = self.make_bookmark(user.id, q.id)

        # 実行 -----------------------------------------------------
        url = reverse('bookmark:release', args=(b.id, ))
        response = self.client.get(url)
        b_count = Question.objects.filter(id=b.id).count()

        # テスト ---------------------------------------------------
        self.assertIs(b_count, 0)


    # テスト失敗　未実装
    def test_release_with_no_bookamrk(self):
        """
        ----------------------------------------------------------------
        ** テスト内容 **
        該当のブックマークがない状態でのブックマーク解除

        ** 入力値 **
        bookmark_id
        ** 期待値 **
        リダイレクト先：errors:errors
        ----------------------------------------------------------------
        """
        # データ作成 ------------------------------------------------
        user = self.make_user('usr', 'aa@bb.jp', '0000')
        q = self.make_question(1, user.id)

        b = self.make_bookmark(user.id, q.id)

        # 実行 -----------------------------------------------------
        url = reverse('bookmark:release', args=(b.id + 2, ))
        response = self.client.get(url)

        # テスト ---------------------------------------------------
        self.assertRedirects(
            response,
            expected_url=reverse('errors:errors'),
            status_code=302,
            target_status_code=200,
        )