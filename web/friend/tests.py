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
    def test_show_follow(self):
        """
        ----------------------------------------------------------------
        ** テスト内容 **
        - フォローしたユーザーの表示
        ----------------------------------------------------------------
        """
        # データ作成 ------------------------------------------------
        u1 = self.make_user('u1', 'a@b.jp', '0000')
        u2 = self.make_user('u2', 'b@b.jp', '0000')
        u3 = self.make_user('u3', 'c@b.jp', '0000')
        u4 = self.make_user('u4', 'd@b.jp', '0000')

        lu = self.make_login_user(u1.id, u1.username)

        f1 = self.make_relation(u1.id, u2.id)
        f2 = self.make_relation(u1.id, u3.id)

        # 実行 -----------------------------------------------------
        url = reverse('friend:follow', args=(u1.id, ))
        response = self.client.get(url)
        # テスト ---------------------------------------------------
        # テスト用文字列作成
        t1 = f"{{'id': { f1.id }, 'user': <User: { u2.username }>}}"
        t2 = f"{{'id': { f2.id }, 'user': <User: { u3.username }>}}"

        # レスポンス
        self.assertEqual(response.status_code, 200)
        # レスポンス(配列・構造体)
        self.assertQuerysetEqual(
            response.context['follow_list'],
            [t1, t2],
            ordered=False,
        )

    def test_show_no_follow(self):
        """
        ----------------------------------------------------------------
        ** テスト内容 **
        - フォローしたユーザーがいない場合
        ----------------------------------------------------------------
        """
        # データ作成 ------------------------------------------------
        u1 = self.make_user('u1', 'a@b.jp', '0000')
        u2 = self.make_user('u2', 'b@b.jp', '0000')
        u3 = self.make_user('u3', 'c@b.jp', '0000')
        u4 = self.make_user('u4', 'd@b.jp', '0000')

        lu = self.make_login_user(u1.id, u1.username)

        f1 = self.make_relation(u2.id, u3.id)
        f1 = self.make_relation(u3.id, u4.id)

        # 実行 -----------------------------------------------------
        url = reverse('friend:follow', args=(u1.id, ))
        response = self.client.get(url)
        # テスト ---------------------------------------------------
        # レスポンス
        self.assertEqual(response.status_code, 200)
        # レスポンス(配列・構造体)
        self.assertQuerysetEqual(
            response.context['follow_list'],
            [],
            ordered=False,
        )

    def test_redirect(self):
        """
        ----------------------------------------------------------------
        ** テスト内容 **
        - ユーザーがログインしてない状態でのリダイレクト
        ----------------------------------------------------------------
        """
        # データ作成 ------------------------------------------------
        user = self.make_user("usr1", "aa@bb.jp", "1234")

        # 実行 -----------------------------------------------------
        response = self.client.get(reverse('friend:follow', args=(user.id, )))

        # テスト ---------------------------------------------------
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
    def test_show_follower(self):
        """
        ----------------------------------------------------------------
        ** テスト内容 **
        - 自分をフォローしているユーザーの表示
        ----------------------------------------------------------------
        """
        # データ作成 ------------------------------------------------
        u1 = self.make_user('u1', 'a@b.jp', '0000')
        u2 = self.make_user('u2', 'b@b.jp', '0000')
        u3 = self.make_user('u3', 'c@b.jp', '0000')
        u4 = self.make_user('u4', 'd@b.jp', '0000')

        lu = self.make_login_user(u1.id, u1.username)

        f1 = self.make_relation(u1.id, u2.id)
        f2 = self.make_relation(u1.id, u3.id)
        f3 = self.make_relation(u2.id, u1.id)

        # 実行 -----------------------------------------------------
        url = reverse('friend:follower', args=(u1.id, ))
        response = self.client.get(url)
        # テスト ---------------------------------------------------
        # レスポンス
        self.assertEqual(response.status_code, 200)
        # レスポンス(配列・構造体)
        self.assertQuerysetEqual(
            response.context['follower_list'],
            ["{'user': <User: u2>, 'follower': <Follow: u2is following u1>}"],
            ordered=False,
        )
    
    def test_show_no_follower(self):
        """
        ----------------------------------------------------------------
        ** テスト内容 **
        - 自分をフォローしたユーザーがいない場合の表示
        ----------------------------------------------------------------
        """
        # データ作成 ------------------------------------------------
        u1 = self.make_user('u1', 'a@b.jp', '0000')
        u2 = self.make_user('u2', 'b@b.jp', '0000')
        u3 = self.make_user('u3', 'c@b.jp', '0000')
        u4 = self.make_user('u4', 'd@b.jp', '0000')

        lu = self.make_login_user(u1.id, u1.username)

        f1 = self.make_relation(u1.id, u2.id)
        f2 = self.make_relation(u1.id, u3.id)
        f3 = self.make_relation(u2.id, u3.id)

        # 実行 -----------------------------------------------------
        url = reverse('friend:follower', args=(u1.id, ))
        response = self.client.get(url)
        # テスト ---------------------------------------------------
        # テスト用文字列作成
        t1 = f"{{'id': { f1.id }, 'user': <User: { u2.username }>}}"
        
        # レスポンス
        self.assertEqual(response.status_code, 200)
        # レスポンス(配列・構造体)
        self.assertQuerysetEqual(
            response.context['follower_list'],
            [],
            ordered=False,
        )
        

    def test_redirect(self):
        """
        ----------------------------------------------------------------
        ** テスト内容 **
        - ユーザーがログインしてない状態でのリダイレクト
        ----------------------------------------------------------------
        """
        # データ作成 ------------------------------------------------
        user = self.make_user("usr1", "aa@bb.jp", "1234")

        # 実行 -----------------------------------------------------
        response = self.client.get(reverse('friend:follower', args=(user.id, )))

        # テスト ---------------------------------------------------
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
    def test_follow(self):
        """
        ----------------------------------------------------------------
        ** テスト内容 **
        - 公開されているユーザーをフォローできるか
        ----------------------------------------------------------------
        """
        # データ作成 ------------------------------------------------
        u1 = self.make_user('u1', 'a@b.jp', '0000')
        u2 = self.make_user('u2', 'b@b.jp', '0000')

        p1 = self.make_profile(u1.id, True)
        p2 = self.make_profile(u2.id, True)

        lu = self.make_login_user(u1.id, u1.username)

        # 実行 -----------------------------------------------------
        url = reverse('friend:run_follow', args=(u2.id, ))
        response = self.client.get(url)

        count_f = Follow.objects.filter(
            follow_user_id=u1.id, followed_user_id=u2.id
        ).count()

        # テスト ---------------------------------------------------
        # レスポンス
        self.assertEqual(response.status_code, 302)
        self.assertEqual(count_f, 1)

    def test_permit(self):
        """
        ----------------------------------------------------------------
        ** テスト内容 **
        - 公開されていないユーザーに申請できるか
        ----------------------------------------------------------------
        """
        # データ作成 ------------------------------------------------
        u1 = self.make_user('u1', 'a@b.jp', '0000')
        u2 = self.make_user('u2', 'b@b.jp', '0000')

        p1 = self.make_profile(u1.id, True)
        p2 = self.make_profile(u2.id, False)

        lu = self.make_login_user(u1.id, u1.username)

        # 実行 -----------------------------------------------------
        url = reverse('friend:run_follow', args=(u2.id, ))
        response = self.client.get(url)

        count_p = Permit.objects.filter(
            request_user_id=u1.id, target_user_id=u2.id
        ).count()

        # テスト ---------------------------------------------------
        # レスポンス
        self.assertEqual(response.status_code, 302)
        self.assertEqual(count_p, 1)


    def test_follow_with_no_user(self):
        """
        ----------------------------------------------------------------
        ** テスト内容 **
        - 公開されていないユーザーに申請できるか
        ----------------------------------------------------------------
        """
        # データ作成 ------------------------------------------------
        u1 = self.make_user('u1', 'a@b.jp', '0000')
        u2 = self.make_user('u2', 'b@b.jp', '0000')

        p1 = self.make_profile(u1.id, True)
        p2 = self.make_profile(u2.id, False)

        lu = self.make_login_user(u1.id, u1.username)

        # 実行 -----------------------------------------------------
        url = reverse('friend:run_follow', args=(0, ))
        response = self.client.get(url)

        # テスト ---------------------------------------------------
        self.assertRedirects(
            response,
            expected_url=reverse('errors:errors'),
            status_code=302,
            target_status_code=200,
        )

    def test_redirect(self):
        """
        ----------------------------------------------------------------
        ** テスト内容 **
        - ユーザーがログインしてない状態でのリダイレクト
        ----------------------------------------------------------------
        """
        # データ作成 ------------------------------------------------
        u1 = self.make_user("usr1", "aa@bb.jp", "1234")
        u2 = self.make_user("usr2", "bb@bb.jp", "1234")

        f = self.make_relation(u1.id, u2.id)

        # 実行 -----------------------------------------------------
        response = self.client.get(reverse('friend:run_follow', args=(u2.id, )))

        # テスト ---------------------------------------------------
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
    def test_release(self):
        """
        ----------------------------------------------------------------
        ** テスト内容 **
        - フォローを解除できるか
        ----------------------------------------------------------------
        """
        # データ作成 ------------------------------------------------
        u1 = self.make_user('u1', 'a@b.jp', '0000')
        u2 = self.make_user('u2', 'b@b.jp', '0000')

        p1 = self.make_profile(u1.id, True)
        p2 = self.make_profile(u2.id, True)

        lu = self.make_login_user(u1.id, u1.username)

        f = self.make_relation(u1.id, u2.id)

        # 実行 -----------------------------------------------------
        url = reverse('friend:release', args=(f.id, ))
        response = self.client.get(url)

        count_f = Follow.objects.filter(
            follow_user_id   = u1.id,
            followed_user_id = u2.id,
        ).count()
        # テスト ---------------------------------------------------
        # レスポンス
        self.assertEqual(response.status_code, 302)
        self.assertEqual(count_f, 0)


    def test_release_with_no_follow_id(self):
        """
        ----------------------------------------------------------------
        ** テスト内容 **
        - 指定されたIDに該当する情報がない場合エラーページに遷移するか
        ----------------------------------------------------------------
        """
        # データ作成 ------------------------------------------------
        u1 = self.make_user('u1', 'a@b.jp', '0000')
        u2 = self.make_user('u2', 'b@b.jp', '0000')

        p1 = self.make_profile(u1.id, True)
        p2 = self.make_profile(u2.id, True)

        lu = self.make_login_user(u1.id, u1.username)

        f = self.make_relation(u1.id, u2.id)

        # 実行 -----------------------------------------------------
        url = reverse('friend:release', args=(0, ))
        response = self.client.get(url)

        count_f = Follow.objects.filter(
            follow_user_id   = u1.id,
            followed_user_id = u2.id,
        ).count()
        # テスト ---------------------------------------------------
        # レスポンス
        self.assertRedirects(
            response,
            expected_url=reverse('errors:errors'),
            status_code=302,
            target_status_code=200,
        )

        self.assertEqual(count_f, 1)

    def test_redirect(self):
        """
        ----------------------------------------------------------------
        ** テスト内容 **
        - ユーザーがログインしてない状態でのリダイレクト
        ----------------------------------------------------------------
        """
        # データ作成 ------------------------------------------------
        u1 = self.make_user("usr1", "aa@bb.jp", "1234")
        u2 = self.make_user("usr2", "bb@bb.jp", "1234")

        f = self.make_relation(u1.id, u2.id)

        # 実行 -----------------------------------------------------
        response = self.client.get(reverse('friend:release', args=(f.id, )))

        # テスト ---------------------------------------------------
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
    def test_show_permit(self):
        """
        ----------------------------------------------------------------
        ** テスト内容 **
        - 申請一覧を表示する
        ----------------------------------------------------------------
        """
        # データ作成 ------------------------------------------------
        u1 = self.make_user('u1', 'a@b.jp', '0000')
        u2 = self.make_user('u2', 'b@b.jp', '0000')
        u3 = self.make_user('u3', 'c@b.jp', '0000')
        u4 = self.make_user('u4', 'd@b.jp', '0000')

        lu = self.make_login_user(u1.id, u1.username)

        p1 = self.make_permit(u1.id, u2.id)
        p2 = self.make_permit(u1.id, u3.id)
        p3 = self.make_permit(u3.id, u1.id)

        # 実行 -----------------------------------------------------
        url = reverse('friend:permit', args=(u1.id, ))
        response = self.client.get(url)
        # テスト ---------------------------------------------------
        pl1 = f"{{'id': { p1.id }, 'user': <User: { u2 }>}}"
        pl2 = f"{{'id': { p2.id }, 'user': <User: { u3 }>}}"
        pl3 = f"{{'id': { p3.id }, 'user': <User: { u3 }>}}"
        # レスポンス
        self.assertEqual(response.status_code, 200)
        # レスポンス(配列・構造体)
        self.assertQuerysetEqual(
            response.context['permit_list'],
            [pl3],
            ordered=False,
        )
        self.assertQuerysetEqual(
            response.context['permited_list'],
            [pl1, pl2],
            ordered=False,
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
        response = self.client.get(reverse('friend:permit', args=(user.id, )))

        # テスト ---------------------------------------------------
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
    def test_permit(self):
        """
        ----------------------------------------------------------------
        ** テスト内容 **
        - 申請許可処理ができる
        ----------------------------------------------------------------
        """
        # データ作成 ------------------------------------------------
        u1 = self.make_user('u1', 'a@b.jp', '0000')
        u2 = self.make_user('u2', 'b@b.jp', '0000')

        lu = self.make_login_user(u1.id, u1.username)

        p1 = self.make_permit(u1.id, u2.id)

        # 実行 -----------------------------------------------------
        url = reverse('friend:run_permit', args=(p1.id, ))
        response = self.client.get(url)

        count_f = Follow.objects.filter(
            follow_user_id   = u1.id,
            followed_user_id = u2.id,
        ).count()

        count_p = Permit.objects.all().count()

        # テスト ---------------------------------------------------
        self.assertEqual(response.status_code, 302)
        self.assertEqual(count_f, 1)
        self.assertEqual(count_p, 0)

    def test_permit_with_no_permit_data(self):
        """
        ----------------------------------------------------------------
        ** テスト内容 **
        - IDに該当する申請データが存在しない場合にエラーに飛ぶ
        ----------------------------------------------------------------
        """
        # データ作成 ------------------------------------------------
        u1 = self.make_user('u1', 'a@b.jp', '0000')
        u2 = self.make_user('u2', 'b@b.jp', '0000')

        lu = self.make_login_user(u1.id, u1.username)

        p1 = self.make_permit(u1.id, u2.id)

        # 実行 -----------------------------------------------------
        url = reverse('friend:run_permit', args=(0, ))
        response = self.client.get(url)
        
        # テスト ---------------------------------------------------
        self.assertRedirects(
            response,
            expected_url=reverse('errors:errors'),
            status_code=302,
            target_status_code=200,
        )


    def test_redirect(self):
        """
        ----------------------------------------------------------------
        ** テスト内容 **
        - ユーザーがログインしてない状態でのリダイレクト
        ----------------------------------------------------------------
        """
        # データ作成 ------------------------------------------------
        u1 = self.make_user("usr1", "aa@bb.jp", "1234")
        u2 = self.make_user("usr2", "bb@bb.jp", "1234")

        p = self.make_permit(u1.id, u2.id)

        # 実行 -----------------------------------------------------
        response = self.client.get(reverse('friend:run_permit', args=(p.id, )))

        # テスト ---------------------------------------------------
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
    def test_nopermit(self):
        """
        ----------------------------------------------------------------
        ** テスト内容 **
        - 申請不許可処理ができる
        ----------------------------------------------------------------
        """
        # データ作成 ------------------------------------------------
        u1 = self.make_user('u1', 'a@b.jp', '0000')
        u2 = self.make_user('u2', 'b@b.jp', '0000')

        lu = self.make_login_user(u1.id, u1.username)

        p1 = self.make_permit(u1.id, u2.id)

        # 実行 -----------------------------------------------------
        url = reverse('friend:run_nopermit', args=(p1.id, ))
        response = self.client.get(url)

        count_f = Follow.objects.all().count()

        count_p = Permit.objects.all().count()

        # テスト ---------------------------------------------------
        self.assertEqual(response.status_code, 302)
        self.assertEqual(count_f, 0)
        self.assertEqual(count_p, 0)

    def test_nopermit_with_no_permit_data(self):
        """
        ----------------------------------------------------------------
        ** テスト内容 **
        - IDに該当する申請データが存在しない場合にエラーに飛ぶ
        ----------------------------------------------------------------
        """
        # データ作成 ------------------------------------------------
        u1 = self.make_user('u1', 'a@b.jp', '0000')
        u2 = self.make_user('u2', 'b@b.jp', '0000')

        lu = self.make_login_user(u1.id, u1.username)

        p1 = self.make_permit(u1.id, u2.id)

        # 実行 -----------------------------------------------------
        url = reverse('friend:run_permit', args=(0, ))
        response = self.client.get(url)
        
        # テスト ---------------------------------------------------
        self.assertRedirects(
            response,
            expected_url=reverse('errors:errors'),
            status_code=302,
            target_status_code=200,
        )

    def test_redirect(self):
        """
        ----------------------------------------------------------------
        ** テスト内容 **
        - ユーザーがログインしてない状態でのリダイレクト
        ----------------------------------------------------------------
        """
        # データ作成 ------------------------------------------------
        u1 = self.make_user("usr1", "aa@bb.jp", "1234")
        u2 = self.make_user("usr2", "bb@bb.jp", "1234")

        p = self.make_permit(u1.id, u2.id)

        # 実行 -----------------------------------------------------
        response = self.client.get(reverse('friend:run_nopermit', args=(p.id, )))

        # テスト ---------------------------------------------------
        self.assertRedirects(
            response,
            expected_url=reverse('top:top'),
            status_code=302,
            target_status_code=200,
        )