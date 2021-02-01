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
        - ユーザーがログインしてない状態でのリダイレクト
        ----------------------------------------------------------------
        """
        # データ作成 ------------------------------------------------

        # 実行 -----------------------------------------------------
        response = self.client.get(reverse('playground:index'))

        # テスト ---------------------------------------------------
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
    def test_run(self):
        """
        ----------------------------------------------------------------
        ** テスト内容 **
        - 正しい
        ----------------------------------------------------------------
        """
        # データ作成 ------------------------------------------------
        u = self.make_user('u1', 'a@b.jp', '0000')
        lu = self.make_login_user(u.id, u.username)

        post_data = {
            'code-name': 'code1',
            'code'     : '''\
a = 10
b = 5
print(a + b)
            ''',
        }

        # 実行 -----------------------------------------------------
        url = reverse('playground:run')
        response = self.client.post(url, post_data)

        result = self.client.session['result']
        code   = self.client.session['code']
        # テスト ---------------------------------------------------
        # レスポンス
        self.assertEqual(result, '15\n')
        self.assertEqual(code, '''\
a = 10
b = 5
print(a + b)
            ''')
        # リダイレクト
        self.assertRedirects(
            response,
            expected_url=reverse('playground:index'),
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

        # 実行 -----------------------------------------------------
        response = self.client.get(reverse('playground:run'))

        # テスト ---------------------------------------------------
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

    def test_show_edit(self):
        """
        ----------------------------------------------------------------
        ** テスト内容 **
        - DBから該当コードを取得し表示できるかどうか
        ----------------------------------------------------------------
        """
        # データ作成 ------------------------------------------------
        u = self.make_user('u1', 'a@b.jp', '0000')
        c = self.make_code(u.id, 'code1')
        lu = self.make_login_user(u.id, u.username)

        # 実行 -----------------------------------------------------
        url = reverse('playground:edit', args=(c.id, ))
        response = self.client.get(url)

        # テスト ---------------------------------------------------
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['code'], c)
        self.assertEqual(response.context['result'], '')

    def test_show_edit_with_session(self):
        """
        ----------------------------------------------------------------
        ** テスト内容 **
        - DBから該当コードを取得し表示できるかどうか
        - sessionでデータが上書きされているかどうか
        ----------------------------------------------------------------
        """
        # データ作成 ------------------------------------------------
        u = self.make_user('u1', 'a@b.jp', '0000')
        c = self.make_code(u.id, 'code1')
        lu = self.make_login_user(u.id, u.username)

        s_code   = self.make_code_session('print(10)')
        s_result = self.make_result_session('10')

        # 実行 -----------------------------------------------------
        url = reverse('playground:edit', args=(c.id, ))
        response = self.client.get(url)

        res_code = response.context['code']

        # テスト ---------------------------------------------------
        self.assertEqual(response.status_code, 200)
        self.assertEqual(res_code.code, 'print(10)')
        self.assertEqual(response.context['result'], '10')

    def test_show_with_no_code(self):
        """
        ----------------------------------------------------------------
        ** テスト内容 **
        - code_idで指定された問題が存在しない時エラーページに飛ぶか
        ----------------------------------------------------------------
        """
        # データ作成 ------------------------------------------------
        u = self.make_user('u1', 'a@b.jp', '0000')
        c = self.make_code(u.id, 'code1')
        lu = self.make_login_user(u.id, u.username)

        # 実行 -----------------------------------------------------
        url = reverse('playground:edit', args=(0, ))
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
        u = self.make_user('u1', 'a@b.jp', '0000')
        c = self.make_code(u.id, 'code1')

        # 実行 -----------------------------------------------------
        response = self.client.get(reverse('playground:edit', args=(c.id, )))

        # テスト ---------------------------------------------------
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
    def test_run_edit(self):
        """
        ----------------------------------------------------------------
        ** テスト内容 **
        - 正しい結果を返せるかどうか
        ----------------------------------------------------------------
        """
        # データ作成 ------------------------------------------------
        u = self.make_user('u1', 'a@b.jp', '0000')
        c = self.make_code(u.id, 'code1')
        lu = self.make_login_user(u.id, u.username)

        post_data = {
            'code-name': 'code1',
            'code'     : '''\
a = 10
b = 5
print(a + b)
            ''',
        }

        # 実行 -----------------------------------------------------
        url = reverse('playground:run_edit', args=(c.id, ))
        response = self.client.post(url, post_data)

        result = self.client.session['result']
        code   = self.client.session['code']
        # テスト ---------------------------------------------------
        # レスポンス
        self.assertEqual(result, '15\n')
        self.assertEqual(code, '''\
a = 10
b = 5
print(a + b)
            ''')
        # リダイレクト
        self.assertRedirects(
            response,
            expected_url=reverse('playground:edit', args=(c.id, )),
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
        c = self.make_code(u.id, 'code1')
        
        # 実行 -----------------------------------------------------
        response = self.client.get(reverse('playground:run_edit', args=(c.id, )))

        # テスト ---------------------------------------------------
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
    def test_show_question(self):
        """
        ----------------------------------------------------------------
        ** テスト内容 **
        指定された問題を取得し表示できるかどうか
        ----------------------------------------------------------------
        """
        # データ作成 ------------------------------------------------
        u = self.make_user('u1', 'a@b.jp', '0000')
        q = self.make_question(1, u.id)
        lu = self.make_login_user(u.id, u.username)

        # 実行 -----------------------------------------------------
        url = reverse('playground:question', args=(q.id, ))
        response = self.client.get(url)

        # テスト ---------------------------------------------------
        # レスポンス
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['question'], q)
        self.assertEqual(response.context['result'], '')

    def test_show_question_with_session(self):
        """
        ----------------------------------------------------------------
        ** テスト内容 **
        指定された問題を取得し表示できるかどうか
        ----------------------------------------------------------------
        """
        # データ作成 ------------------------------------------------
        u = self.make_user('u1', 'a@b.jp', '0000')
        q = self.make_question(1, u.id)
        lu = self.make_login_user(u.id, u.username)

        s_code   = self.make_code_session('print(10)')
        s_result = self.make_result_session('10')

        # 実行 -----------------------------------------------------
        url = reverse('playground:question', args=(q.id, ))
        response = self.client.get(url)

        res_code = response.context['question']
        # テスト ---------------------------------------------------
        # レスポンス
        self.assertEqual(response.status_code, 200)
        self.assertEqual(res_code.default_code, 'print(10)')
        self.assertEqual(response.context['result'], '10')


    def test_show_with_no_question_id(self):
        """
        ----------------------------------------------------------------
        ** テスト内容 **
        question_idで指定された問題が存在しない時エラーページに飛ぶか
        ** 入力値 **
        
        ** 期待値 **
        
        ----------------------------------------------------------------
        """
        # データ作成 ------------------------------------------------
        u = self.make_user('u1', 'a@b.jp', '0000')
        q = self.make_question(1, u.id)
        lu = self.make_login_user(u.id, u.username)

        # 実行 -----------------------------------------------------
        url = reverse('playground:question', args=(0, ))
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
        u = self.make_user('u1', 'a@b.jp', '0000')
        q = self.make_question(1, u.id)

        # 実行 -----------------------------------------------------
        response = self.client.get(reverse('playground:question', args=(q.id, )))

        # テスト ---------------------------------------------------
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
    def test_true_judge(self):
        """
        ----------------------------------------------------------------
        ** テスト内容 **
        - 正しい結果を返せるかどうか
        ----------------------------------------------------------------
        """
        # データ作成 ------------------------------------------------
        u = self.make_user('u1', 'a@b.jp', '0000')
        q = self.make_question(1, u.id)
        lu = self.make_login_user(u.id, u.username)

        post_data = {
            'code'     : '''\
a = 10
b = 5
print(a + b)
            ''',
            'answer': '15',
        }

        # 実行 -----------------------------------------------------
        url = reverse('playground:run_question', args=(q.id, ))
        response = self.client.post(url, post_data)

        result = self.client.session['result']
        code   = self.client.session['code']
        # テスト ---------------------------------------------------
        # レスポンス
        self.assertEqual(result, f"""\
実行結果: 15
答え　　: 15
判定　　: 正解
        """)
        self.assertEqual(code, '''\
a = 10
b = 5
print(a + b)
            ''')
        # リダイレクト
        self.assertRedirects(
            response,
            expected_url=reverse('playground:question', args=(q.id, )),
            status_code=302,
            target_status_code=200,
        )

    def test_false_judge(self):
        """
        ----------------------------------------------------------------
        ** テスト内容 **
        - 不正解判定
        ----------------------------------------------------------------
        """
        # データ作成 ------------------------------------------------
        u = self.make_user('u1', 'a@b.jp', '0000')
        q = self.make_question(1, u.id)
        lu = self.make_login_user(u.id, u.username)

        post_data = {
            'code'     : '''\
a = 10
b = 5
print(a + b)
            ''',
            'answer': '20',
        }

        # 実行 -----------------------------------------------------
        url = reverse('playground:run_question', args=(q.id, ))
        response = self.client.post(url, post_data)

        result = self.client.session['result']
        code   = self.client.session['code']
        # テスト ---------------------------------------------------
        # レスポンス
        self.assertEqual(result, f"""\
実行結果: 15
答え　　: 20
判定　　: 不正解
        """)
        self.assertEqual(code, '''\
a = 10
b = 5
print(a + b)
            ''')
        # リダイレクト
        self.assertRedirects(
            response,
            expected_url=reverse('playground:question', args=(q.id, )),
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
        u = self.make_user('u1', 'a@b.jp', '0000')
        q = self.make_question(1, u.id)

        # 実行 -----------------------------------------------------
        response = self.client.get(reverse('playground:run_question', args=(q.id, )))

        # テスト ---------------------------------------------------
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
    def test_save(self):
        """
        ----------------------------------------------------------------
        ** テスト内容 **
        - 保存が正しくなされるかどうか
        ----------------------------------------------------------------
        """
        # データ作成 ------------------------------------------------
        u = self.make_user('u1', 'a@b.jp', '0000')
        lu = self.make_login_user(u.id, u.username)

        post_data = {
            'code-name': 'code1',
            'code'     : 'print(10)',
        }

        # 実行 -----------------------------------------------------
        url = reverse('playground:save')
        response = self.client.post(url, post_data)

        c = Code.objects.filter(
            name = post_data['code-name'],
        )
        # テスト ---------------------------------------------------
        self.assertEqual(c.count(), 1)
        # リダイレクト
        self.assertRedirects(
            response,
            expected_url=reverse('playground:edit', args=(c[0].id, )),
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
        response = self.client.get(reverse('playground:save'))

        # テスト ---------------------------------------------------
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
    def test_update(self):
        """
        ----------------------------------------------------------------
        ** テスト内容 **
        - コードの変更が正しくなされるかどうか
        ----------------------------------------------------------------
        """
        # データ作成 ------------------------------------------------
        u = self.make_user('u1', 'a@b.jp', '0000')
        c = self.make_code(u.id, 'code')
        lu = self.make_login_user(u.id, u.username)

        post_data = {
            'code-name': 'code1',
            'code'     : 'print(10)',
        }

        # 実行 -----------------------------------------------------
        url = reverse('playground:update', args=(c.id, ))
        response = self.client.post(url, post_data)

        c_edit = Code.objects.get(pk=c.id)

        # テスト ---------------------------------------------------
        self.assertEqual(c_edit.name, 'code1')
        self.assertEqual(c_edit.code, 'print(10)')
        # リダイレクト
        self.assertRedirects(
            response,
            expected_url=reverse('playground:edit', args=(c.id, )),
            status_code=302,
            target_status_code=200,
        )

    def test_update_other(self):
        """
        ----------------------------------------------------------------
        ** テスト内容 **
        - 作成者と別のユーザーがコードを変更した場合、新規作成されるか
        ----------------------------------------------------------------
        """
        # データ作成 ------------------------------------------------
        u = self.make_user('u1', 'a@b.jp', '0000')
        other_u = self.make_user('u2', 'b@b.jp', '0000')
        c = self.make_code(u.id, 'code')
        lu = self.make_login_user(other_u.id, other_u.username)

        post_data = {
            'code-name': 'code1',
            'code'     : 'print(10)',
        }

        # 実行 -----------------------------------------------------
        url = reverse('playground:update', args=(c.id, ))
        response = self.client.post(url, post_data)

        c_edit = Code.objects.get(target_user_id=other_u.id)

        # テスト ---------------------------------------------------
        self.assertEqual(c_edit.name, 'code1')
        self.assertEqual(c_edit.code, 'print(10)')
        # リダイレクト
        self.assertRedirects(
            response,
            expected_url=reverse('playground:edit', args=(c.id, )),
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
        u = self.make_user('u1', 'a@b.jp', '0000')
        c = self.make_code(u.id, 'code')

        # 実行 -----------------------------------------------------
        response = self.client.get(reverse('playground:update', args=(c.id, )))

        # テスト ---------------------------------------------------
        self.assertRedirects(
            response,
            expected_url=reverse('top:top'),
            status_code=302,
            target_status_code=200,
        )