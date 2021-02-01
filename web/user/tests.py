from pyground.tests import CommonTestCase
from django.urls    import reverse
from django.core    import mail

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
    def test_message(self):
        """
        ----------------------------------------------------------------
        ** テスト内容 **
        - セッションに格納したメッセージを取得して表示できるか
        ----------------------------------------------------------------
        """
        # データ作成 ------------------------------------------------
        m = self.make_message('メッセージ')

        # 実行 -----------------------------------------------------
        url = reverse('user:register')
        response = self.client.get(url)
        # テスト ---------------------------------------------------
        # レスポンス
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['message'], 'メッセージ')
        

    def test_redirect(self):
        """
        ----------------------------------------------------------------
        ** テスト内容 **
        - ユーザーがログインしている状態ならユーザー詳細のページへ遷移
        ----------------------------------------------------------------
        """
        # データ作成 ------------------------------------------------
        u = self.make_user('u1', 'a@b.jp', '0000')
        p = self.make_profile(u.id, True)
        login_user = self.make_login_user(u.id, u.username)

        # 実行 -----------------------------------------------------
        response = self.client.get(reverse('user:register'))

        # テスト ---------------------------------------------------
        self.assertRedirects(
            response,
            expected_url=reverse('user:detail', args=(u.id, )),
            status_code=302,
            target_status_code=200,
        )

class RegisterCompleteViewTest(CommonTestCase):
    """
    ----------------------------------------------------------------------
    ユーザー／登録完了ページ
    ----------------------------------------------------------------------
    """

    def test_register_complete(self):
        """
        ----------------------------------------------------------------
        ** テスト内容 **
        - セッションへのログインユーザーの情報登録ができているか
        - トークンの削除ができているか
        ----------------------------------------------------------------
        """
        # データ作成 ------------------------------------------------
        u = self.make_user('u1','a@b.jp', '0000')

        # 実行 -----------------------------------------------------
        url = reverse('user:register_complete', args=(u.token, ))
        response = self.client.get(url)

        u_reget = User.objects.get(pk=u.id)
        session = self.client.session['login_user']

        # テスト ---------------------------------------------------
        # その他
        self.assertIs(u_reget.token, '')
        self.assertIs(session['id'], u.id)
        
    def test_register_complete_with_no_token(self):
        """
        ----------------------------------------------------------------
        ** テスト内容 **
        - 指定されたトークンを持つユーザーがいない場合はエラーページに遷移するか
        - ちゃんとしたメッセージが送られているか
        ----------------------------------------------------------------
        """
        # データ作成 ------------------------------------------------
        u = self.make_user('u1','a@b.jp', '0000')

        # 実行 -----------------------------------------------------
        url = reverse('user:register_complete', args=('aaaaaa', ))
        response = self.client.get(url)

        u_reget = User.objects.get(pk=u.id)
        session = self.client.session['errors']

        # テスト ---------------------------------------------------
        # リダイレクト
        self.assertRedirects(
            response,
            expected_url=reverse('errors:errors'),
            status_code=302,
            target_status_code=200,
        )
        self.assertEqual(session['msg'], 'このユーザーはすでに本登録が済んでいます。')


class RunRegisterViewTest(CommonTestCase):
    """
    ----------------------------------------------------------------------
    ユーザー／登録処理
    ----------------------------------------------------------------------
    """
    def test_run_register(self):
        """
        ----------------------------------------------------------------
        ** テスト内容 **
        - データの登録ができているか
        - セッションへのメッセージの登録ができている
        - メールの送信はできているか
        ----------------------------------------------------------------
        """
        # データ作成 ------------------------------------------------
        post_user = {
            'username': 'u1',
            'email'   : 'a@b.jp',
            'password': '0000',
            'check'   : '0000',
        }
        # 実行 -----------------------------------------------------
        url = reverse('user:run_register')
        response = self.client.post(url, post_user)

        u = User.objects.get(email='a@b.jp')
        s = self.client.session['message']
        # テスト ---------------------------------------------------
        self.assertEqual(u.username, post_user['username'])
        self.assertEqual(s, '仮登録が完了しました。')
        self.assertEqual(len(mail.outbox), 1)
        

    def test_validate_not_entered(self):
        """
        ----------------------------------------------------------------
        ** テスト内容 **
        - 未入力に対するバリデーションができているか
        ----------------------------------------------------------------
        """
        # データ作成 ------------------------------------------------
        post_user = {
            'username': 'u1',
            'email'   : '',
            'password': '',
            'check'   : '0000',
        }
        # 実行 -----------------------------------------------------
        url = reverse('user:run_register')
        response = self.client.post(url, post_user)

        s = self.client.session['message']
        # テスト ---------------------------------------------------
        # リダイレクト
        self.assertRedirects(
            response,
            expected_url=reverse('user:register'),
            status_code=302,
            target_status_code=200,
        )
        # その他
        self.assertEqual(s, '未入力項目:, email, password')
        

    def test_validate_password(self):
        """
        ----------------------------------------------------------------
        ** テスト内容 **
        パスワードと確認用の付き合わせができているか
        ** 入力値 **
        
        ** 期待値 **
        
        ----------------------------------------------------------------
        """
        # データ作成 ------------------------------------------------
        post_user = {
            'username': 'u1',
            'email'   : 'a@b.jp',
            'password': '0000',
            'check'   : '1111',
        }
        # 実行 -----------------------------------------------------
        url = reverse('user:run_register')
        response = self.client.post(url, post_user)

        s = self.client.session['message']
        # テスト ---------------------------------------------------
        # リダイレクト
        self.assertRedirects(
            response,
            expected_url=reverse('user:register'),
            status_code=302,
            target_status_code=200,
        )
        # その他
        self.assertEqual(s, 'パスワードとパスワード(確認)が異なります。')
        
class LoginViewTest(CommonTestCase):
    """
    ----------------------------------------------------------------------
    ユーザー／ログインページ
    ----------------------------------------------------------------------
    """
    def test_message(self):
        """
        ----------------------------------------------------------------
        ** テスト内容 **
        セッションにメッセージを登録できているか
        ** 入力値 **
        
        ** 期待値 **
        
        ----------------------------------------------------------------
        """
        # データ作成 ------------------------------------------------
        msg = self.make_message('メッセージ')

        # 実行 -----------------------------------------------------
        url = reverse('user:login')
        response = self.client.get(url)
        # テスト ---------------------------------------------------
        # レスポンス
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['message'], 'メッセージ')

    def test_redirect(self):
        """
        ----------------------------------------------------------------
        ** テスト内容 **
        - ユーザーがログインしている状態ならユーザー詳細のページへ遷移
        ----------------------------------------------------------------
        """
        # データ作成 ------------------------------------------------
        u = self.make_user('u1', 'a@b.jp', '0000')
        p = self.make_profile(u.id, True)
        login_user = self.make_login_user(u.id, u.username)

        # 実行 -----------------------------------------------------
        response = self.client.get(reverse('user:login'))

        # テスト ---------------------------------------------------
        self.assertRedirects(
            response,
            expected_url=reverse('user:detail', args=(u.id, )),
            status_code=302,
            target_status_code=200,
        )

class RunLoginViewTest(CommonTestCase):
    """
    ----------------------------------------------------------------------
    ユーザー／ログイン処理
    ----------------------------------------------------------------------
    """
    def test_login(self):
        """
        ----------------------------------------------------------------
        ** テスト内容 **
        - ログイン処理を正常に行えるか
        - セッションにログインユーザーの情報を格納できているか
        ----------------------------------------------------------------
        """
        # データ作成 ------------------------------------------------
        user = self.make_user('u1', 'a@b.jp', '0000')
        p = self.make_profile(user.id, True)
        post_user = {
            'email'   : 'a@b.jp',
            'password': '0000',
        }
        # 実行 -----------------------------------------------------
        url = reverse('user:run_login')
        response = self.client.post(url, post_user)

        s = self.client.session['login_user']
        # テスト ---------------------------------------------------
        # リダイレクト
        self.assertRedirects(
            response,
            expected_url=reverse('user:detail', args=(user.id, )),
            status_code=302,
            target_status_code=200,
        )
        # その他
        self.assertEqual(s['id'], user.id)
        

    def test_validate_not_entered(self):
        """
        ----------------------------------------------------------------
        ** テスト内容 **
        - 未入力に対するバリデーションができているか
        ----------------------------------------------------------------
        """
        # データ作成 ------------------------------------------------
        post_user = {
            'email'   : '',
            'password': '0000',
        }
        # 実行 -----------------------------------------------------
        url = reverse('user:run_login')
        response = self.client.post(url, post_user)

        s = self.client.session['message']
        # テスト ---------------------------------------------------
        # リダイレクト
        self.assertRedirects(
            response,
            expected_url=reverse('user:login'),
            status_code=302,
            target_status_code=200,
        )
        # その他
        self.assertEqual(s, '未入力項目:, email')
       

class RunLogoutViewTest(CommonTestCase):
    """
    ----------------------------------------------------------------------
    ユーザー／ログアウト処理
    ----------------------------------------------------------------------
    """
    def test_logout(self):
        """
        ----------------------------------------------------------------
        ** テスト内容 **
        - セッションのログインユーザー情報は破棄されているか
        - トップページにリダイレクトしているか
        ----------------------------------------------------------------
        """
        # データ作成 ------------------------------------------------
        u = self.make_user('u1', 'a@b.jp', '0000')
        login_user = self.make_login_user(u.id, u.username)

        # 実行 -----------------------------------------------------
        url = reverse('user:run_logout', args=(u.id, ))
        response = self.client.get(url)

        logout = 'done'
        if 'login_user' in self.client.session:
            logout = 'not yet'
        
        # テスト ---------------------------------------------------
        # その他
        self.assertEqual(logout, 'done')
        # リダイレクト
        self.assertRedirects(
            response,
            expected_url=reverse('top:top'),
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
        u = self.make_user('u1', 'a@b.jp', '0000')

        # 実行 -----------------------------------------------------
        response = self.client.get(reverse('user:run_logout', args=(u.id, )))

        # テスト ---------------------------------------------------
        self.assertRedirects(
            response,
            expected_url=reverse('top:top'),
            status_code=302,
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

        ** 入力値 **
        login_user
        ** 期待値 **
        リダイレクト先: top:top
        ----------------------------------------------------------------
        """
        # データ作成 ------------------------------------------------

        # 実行 -----------------------------------------------------
        response = self.client.get(reverse('user:withdrawal'))

        # テスト ---------------------------------------------------
        self.assertRedirects(
            response,
            expected_url=reverse('top:top'),
            status_code=302,
        )

class RunWithdrawalViewTest(CommonTestCase):
    """
    ----------------------------------------------------------------------
    ユーザー／退会処理
    ----------------------------------------------------------------------
    """
    def test_withdrawal(self):
        """
        ----------------------------------------------------------------
        ** テスト内容 **
        - セッションからログインユーザー情報は破棄できているか
        - ユーザー情報は削除できているか
        - トップページに遷移しているか
        ----------------------------------------------------------------
        """
        # データ作成 ------------------------------------------------
        u = self.make_user('u1', 'a@b.jp', '0000')
        s = self.make_login_user(u.id, u.username)

        # 実行 -----------------------------------------------------
        url = reverse('user:run_withdrawal')
        response = self.client.get(url)

        u_count = User.objects.all().count()
        
        withdrawal = 'done'
        if 'login_user' in self.client.session:
            print(self.session)
            withdrawal = 'not yet'

        # テスト ---------------------------------------------------
        # その他
        self.assertIs(u_count, 0)
        self.assertEqual(withdrawal, 'done')
        # リダイレクト
        self.assertRedirects(
            response,
            expected_url=reverse('top:top'),
            status_code=302,
            target_status_code=200,
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

        # 実行 -----------------------------------------------------
        response = self.client.get(reverse('user:run_withdrawal'))

        # テスト ---------------------------------------------------
        self.assertRedirects(
            response,
            expected_url=reverse('top:top'),
            status_code=302,
        )

class DetailViewTest(CommonTestCase):
    """
    ----------------------------------------------------------------------
    ユーザー／プロフィール詳細ページ
    ----------------------------------------------------------------------
    """
    def test_detail(self):
        """
        ----------------------------------------------------------------
        ** テスト内容 **
        - プロフィール
        - コード 未実装
        - フォロー人数
        - フォロワー人数　　　　　を正しく取得できているか
        ----------------------------------------------------------------
        """
        # データ作成 ------------------------------------------------
        # ユーザー
        u1 = self.make_user('u1', 'a@b.jp', '0000')
        u2 = self.make_user('u2', 'b@b.jp', '0000')
        u3 = self.make_user('u3', 'c@b.jp', '0000')

        # プロフィール
        p1 = self.make_profile(u1.id, True)
        p2 = self.make_profile(u2.id, True)
        p3 = self.make_profile(u3.id, True)

        # ログインユーザー
        lu = self.make_login_user(u1.id, u1.username)

        # フォロー (follow_num=2, follower_num=1)
        f1 = self.make_relation(u1.id, u2.id)
        f1 = self.make_relation(u1.id, u3.id)
        f1 = self.make_relation(u2.id, u1.id)

        # コード
        c1 = self.make_code(u1.id, 'code1')
        c2 = self.make_code(u1.id, 'code2')

        # 
        # 実行 -----------------------------------------------------
        url = reverse('user:detail', args=(u1.id, ))
        response = self.client.get(url)
        # テスト ---------------------------------------------------
        # レスポンス
        self.assertEqual(response.status_code, 200)
        # レスポンス(配列・構造体)
        self.assertEqual(response.context['user'], u1)
        self.assertEqual(response.context['profile'], p1)
        self.assertEqual(response.context['follow_num'], 2)
        self.assertEqual(response.context['follower_num'], 1)
        self.assertEqual(response.context['follow_id'], False)
        self.assertEqual(response.context['is_me'], True)
        self.assertEqual(response.context['is_permit'], False)
        self.assertQuerysetEqual(
            response.context['codes'],
            ['<Code: code2>', '<Code: code1>'],
            ordered=False,
        )
        

    def test_detail_with_no_user(self):
        """
        ----------------------------------------------------------------
        ** テスト内容 **
        - ユーザーIDに該当するユーザーがいない場合の処理が適切か
        ----------------------------------------------------------------
        """
        # データ作成 ------------------------------------------------
        u = self.make_user('u1', 'a@b.jp', '0000')
        lu = self.make_login_user(u.id, u.username)

        # 実行 -----------------------------------------------------
        url = reverse('user:detail', args=(10, ))
        response = self.client.get(url)
        # テスト ---------------------------------------------------
        # リダイレクト
        self.assertRedirects(
            response,
            expected_url=reverse('errors:errors'),
            status_code=302,
            target_status_code=200,
        )
        
    def test_is_me_false(self):
        """
        ----------------------------------------------------------------
        ** テスト内容 **
        - ログインユーザーの判定は適切か
        ----------------------------------------------------------------
        """
        # データ作成 ------------------------------------------------
        # ユーザー
        u1 = self.make_user('u1', 'a@b.jp', '0000')
        u2 = self.make_user('u2', 'b@b.jp', '0000')
        u3 = self.make_user('u3', 'c@b.jp', '0000')

        # プロフィール
        p1 = self.make_profile(u1.id, True)
        p2 = self.make_profile(u2.id, True)
        p3 = self.make_profile(u3.id, True)

        # ログインユーザー
        lu = self.make_login_user(u1.id, u1.username)

        # フォロー (follow_num=2, follower_num=1)
        f1 = self.make_relation(u1.id, u2.id)
        f1 = self.make_relation(u1.id, u3.id)
        f1 = self.make_relation(u2.id, u1.id)

        # 実行 -----------------------------------------------------
        url = reverse('user:detail', args=(u2.id, ))
        response = self.client.get(url)
        # テスト ---------------------------------------------------
        # レスポンス
        self.assertEqual(response.status_code, 200)
        # レスポンス(配列・構造体)
        self.assertEqual(response.context['is_me'], False)
        
    def test_is_permit_true(self):
        """
        ----------------------------------------------------------------
        ** テスト内容 **
        - 申請情報の取得は適切か
        ----------------------------------------------------------------
        """
        # データ作成 ------------------------------------------------
        # ユーザー
        u1 = self.make_user('u1', 'a@b.jp', '0000')
        u2 = self.make_user('u2', 'b@b.jp', '0000')
        u3 = self.make_user('u3', 'c@b.jp', '0000')

        # プロフィール
        p1 = self.make_profile(u1.id, True)
        p2 = self.make_profile(u2.id, True)
        p3 = self.make_profile(u3.id, True)

        # ログインユーザー
        lu = self.make_login_user(u1.id, u1.username)

        # 申請情報
        permit = self.make_permit(u1.id, u2.id)

        # 実行 -----------------------------------------------------
        url = reverse('user:detail', args=(u2.id, ))
        response = self.client.get(url)
        # テスト ---------------------------------------------------
        # レスポンス
        self.assertEqual(response.status_code, 200)
        # レスポンス(配列・構造体)
        self.assertEqual(response.context['is_permit'], True)


    def test_redirect(self):
        """
        ----------------------------------------------------------------
        ** テスト内容 **
        - ユーザーがログインしてない状態でのリダイレクト
        ----------------------------------------------------------------
        """
        # データ作成 ------------------------------------------------
        u = self.make_user('u1', 'a@b.jp', '0000')

        # 実行 -----------------------------------------------------
        response = self.client.get(reverse('user:detail', args=(u.id, )))

        # テスト ---------------------------------------------------
        self.assertRedirects(
            response,
            expected_url=reverse('top:top'),
            status_code=302,
        )

class CreateViewTest(CommonTestCase):
    """
    ----------------------------------------------------------------------
    ユーザー／プロフィール新規作成ページ
    ----------------------------------------------------------------------
    """
    def test_create(self):
        """
        ----------------------------------------------------------------
        ** テスト内容 **
        ログインしているユーザーのIDを取得できているか
        ** 入力値 **
        
        ** 期待値 **
        
        ----------------------------------------------------------------
        """
        # データ作成 ------------------------------------------------
        u = self.make_user('u1', 'a@b.jp', '0000')
        lu = self.make_login_user(u.id, u.username)

        # 実行 -----------------------------------------------------
        url = reverse('user:create')
        response = self.client.get(url)

        # テスト ---------------------------------------------------
        # レスポンス
        self.assertEqual(response.status_code, 200)
        # レスポンス(配列・構造体)
        self.assertEqual(response.context['target_user_id'], u.id)

    def test_redirect(self):
        """
        ----------------------------------------------------------------
        ** テスト内容 **
        - ユーザーがログインしてない状態でのリダイレクト
        ----------------------------------------------------------------
        """
        # データ作成 ------------------------------------------------

        # 実行 -----------------------------------------------------
        response = self.client.get(reverse('user:create'))

        # テスト ---------------------------------------------------
        self.assertRedirects(
            response,
            expected_url=reverse('top:top'),
            status_code=302,
        )

class RunCreateViewTest(CommonTestCase):
    """
    ----------------------------------------------------------------------
    ユーザー／プロフィール新規作成処理
    ----------------------------------------------------------------------
    """
    def test_run_create(self):
        """
        ----------------------------------------------------------------
        ** テスト内容 **
        - プロフィール情報が作成されているか
        ----------------------------------------------------------------
        """
        # データ作成 ------------------------------------------------
        # 初期データ
        u = self.make_user('u1', 'a@b.jp', '0000')
        lu = self.make_login_user(u.id, u.username)

        # 更新データ
        post_data = {
            'id'     : u.id,
            'profile': 'ああああ',
            'publish': 'off',
        }

        # 実行 -----------------------------------------------------
        url = reverse('user:run_create')
        response = self.client.post(url, post_data)

        create_p = Profile.objects.get(target_user_id=u.id)

        # テスト ---------------------------------------------------
        # レスポンス
        self.assertRedirects(
            response,
            expected_url=reverse('user:detail', args=(u.id,)),
            status_code=302,
            target_status_code=200,
        )
        # プロフィール情報の更新
        self.assertEqual(create_p.profile_text, 'ああああ')
        self.assertEqual(create_p.publish, False)

    def test_redirect(self):
        """
        ----------------------------------------------------------------
        ** テスト内容 **
        - ユーザーがログインしてない状態でのリダイレクト
        ----------------------------------------------------------------
        """
        # データ作成 ------------------------------------------------

        # 実行 -----------------------------------------------------
        response = self.client.get(reverse('user:run_create'))

        # テスト ---------------------------------------------------
        self.assertRedirects(
            response,
            expected_url=reverse('top:top'),
            status_code=302,
        )

class EditViewTest(CommonTestCase):
    """
    ----------------------------------------------------------------------
    ユーザー／プロフィール編集ページ
    ----------------------------------------------------------------------
    """
    def test_edit(self):
        """
        ----------------------------------------------------------------
        ** テスト内容 **
        - 適切なユーザーを取得しているか
        - 適切なプロフィールを取得しているか
        ----------------------------------------------------------------
        """
        # データ作成 ------------------------------------------------
        u = self.make_user('u1', 'a@b.jp', '0000')
        p = self.make_profile(u.id, True)
        lu = self.make_login_user(u.id, u.username)

        # 実行 -----------------------------------------------------
        url = reverse('user:edit', args=(u.id, ))
        response = self.client.get(url)

        disp = response.context['profile']
        # テスト ---------------------------------------------------
        # レスポンス
        self.assertEqual(response.status_code, 200)
        self.assertEqual(disp['id']          , u.id)
        self.assertEqual(disp['username']    , u.username)
        self.assertEqual(disp['password']    , u.password)
        self.assertEqual(disp['profile_text'], p.profile_text)
        self.assertEqual(disp['publish']     , p.publish)

    def test_with_no_user(self):
        """
        ----------------------------------------------------------------
        ** テスト内容 **
        - 指定したユーザーが存在しない時の処理は適切か
        ----------------------------------------------------------------
        """
        # データ作成 ------------------------------------------------
        u = self.make_user('u1', 'a@b.jp', '0000')
        p = self.make_profile(u.id, True)
        lu = self.make_login_user(u.id, u.username)

        # 実行 -----------------------------------------------------
        url = reverse('user:edit', args=(u.id + 1, ))
        response = self.client.get(url)
        # テスト ---------------------------------------------------
        # リダイレクト
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
        u = self.make_user('u1', 'a@b.jp', '0000')

        # 実行 -----------------------------------------------------
        response = self.client.get(reverse('user:edit', args=(u.id, )))

        # テスト ---------------------------------------------------
        self.assertRedirects(
            response,
            expected_url=reverse('top:top'),
            status_code=302,
        )

class RunEditViewTest(CommonTestCase):
    """
    ----------------------------------------------------------------------
    ユーザー／プロフィール編集処理
    ----------------------------------------------------------------------
    """
    def test_run_edit(self):
        """
        ----------------------------------------------------------------
        ** テスト内容 **
        - ユーザー情報の更新はできているか
        - プロフィール情報の更新はできているか
        ----------------------------------------------------------------
        """
        # データ作成 ------------------------------------------------
        u = self.make_user('u1', 'a@b.jp', '0000')
        p = self.make_profile(u.id, True)
        lu = self.make_login_user(u.id, u.username)

        post_data = {
            'id'      : u.id,
            'username': 'user',
            'password': 'yatta',
            'profile' : 'rrrrr',
            'publish' : 'on',
        }

        # 実行 -----------------------------------------------------
        url = reverse('user:run_edit', args=(u.id, ))
        response = self.client.post(url, post_data)

        update_u = User.objects.get(pk=u.id)
        update_p = Profile.objects.get(pk=p.id)
        # テスト ---------------------------------------------------
        # 更新データ
        self.assertEqual(update_u.username, post_data['username'])
        self.assertEqual(update_u.password, post_data['password'])
        self.assertEqual(update_p.profile_text , post_data['profile'])
        self.assertEqual(update_p.publish , True)
        # リダイレクト
        self.assertRedirects(
            response,
            expected_url=reverse('user:detail', args=(u.id, )),
            status_code=302,
            target_status_code=200,
        )

    def test_validate_username(self):
        """
        ----------------------------------------------------------------
        ** テスト内容 **
        - username未入力に対する処理は適切か
        ----------------------------------------------------------------
        """
        # データ作成 ------------------------------------------------
        u = self.make_user('u1', 'a@b.jp', '0000')
        p = self.make_profile(u.id, True)
        lu = self.make_login_user(u.id, u.username)

        post_data = {
            'id'      : u.id,
            'username': '',
            'password': 'yatta',
            'profile' : 'rrrrr',
            'publish' : 'on',
        }

        # 実行 -----------------------------------------------------
        url = reverse('user:run_edit', args=(u.id, ))
        response = self.client.post(url, post_data)

        session = self.client.session['message']
        # テスト ---------------------------------------------------
        # 更新データ
        self.assertEqual(session, 'ユーザー名は必ず入力してください。')
        # リダイレクト
        self.assertRedirects(
            response,
            expected_url=reverse('user:edit', args=(u.id, )),
            status_code=302,
            target_status_code=200,
        )

    def test_validate_password(self):
        """
        ----------------------------------------------------------------
        ** テスト内容 **
        - パスワード未入力に対する処理は適切か
        ----------------------------------------------------------------
        """
        # データ作成 ------------------------------------------------
        u = self.make_user('u1', 'a@b.jp', '0000')
        p = self.make_profile(u.id, True)
        lu = self.make_login_user(u.id, u.username)

        post_data = {
            'id'      : u.id,
            'username': 'aaaa',
            'password': '',
            'profile' : 'rrrrr',
            'publish' : 'on',
        }

        # 実行 -----------------------------------------------------
        url = reverse('user:run_edit', args=(u.id, ))
        response = self.client.post(url, post_data)

        session = self.client.session['message']
        # テスト ---------------------------------------------------
        # 更新データ
        self.assertEqual(session, 'パスワードは必ず入力してください。')
        # リダイレクト
        self.assertRedirects(
            response,
            expected_url=reverse('user:edit', args=(u.id, )),
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
        u = self.make_user('u1', 'a@b.jp', '0000')

        # 実行 -----------------------------------------------------
        response = self.client.get(reverse('user:run_edit', args=(u.id, )))

        # テスト ---------------------------------------------------
        self.assertRedirects(
            response,
            expected_url=reverse('top:top'),
            status_code=302,
        )

class IndexViewTest(CommonTestCase):
    """
    ----------------------------------------------------------------------
    ユーザー／ユーザー一覧ページ
    ----------------------------------------------------------------------
    """
    def test_index(self):
        """
        ----------------------------------------------------------------
        ** テスト内容 **
        - ユーザー情報を取得し表示できているか
        ----------------------------------------------------------------
        """
        # データ作成 ------------------------------------------------
        u1 = self.make_user('u1', 'a@b.jp', '0000')
        u2 = self.make_user('u2', 'b@b.jp', '0000')

        lu = self.make_login_user(u1.id, u1.username)

        # 実行 -----------------------------------------------------
        url = reverse('user:index')
        response = self.client.get(url)

        # テスト ---------------------------------------------------
        # レスポンス
        self.assertEqual(response.status_code, 200)
        # レスポンス(配列・構造体)
        self.assertQuerysetEqual(
            response.context['user_list'],
            ['<User: u1>', '<User: u2>'],
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

        # 実行 -----------------------------------------------------
        response = self.client.get(reverse('user:index'))

        # テスト ---------------------------------------------------
        self.assertRedirects(
            response,
            expected_url=reverse('top:top'),
            status_code=302,
        )
