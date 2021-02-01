from pyground.tests import CommonTestCase
from django.urls    import reverse


# モデル
from bookmark.models   import Bookmark
from friend.models     import Follow, Permit
from playground.models import Code
from question.models   import Question, Correcter
from user.models       import User, Profile

# templateのあるviewのみテスト

class QuestionsViewTest(CommonTestCase):
    """
    ----------------------------------------------------------------------
    問題／一覧ページ
    ----------------------------------------------------------------------
    """
    def test_questions(self):
        """
        ----------------------------------------------------------------
        ** テスト内容 **
        - 質問一覧を表示できるか
        ----------------------------------------------------------------
        """
        # データ作成 ------------------------------------------------
        u = self.make_user('u1', 'a@b.jp', '0000')
        q1 = self.make_question(1, u.id)
        q2 = self.make_question(2, u.id)

        lu = self.make_login_user(u.id, u.username)

        # 実行 -----------------------------------------------------
        url = reverse('question:questions')
        response = self.client.get(url)
        # テスト ---------------------------------------------------
        res_q1 = "<Question: 1>"
        res_q2 = "<Question: 2>"
        # レスポンス
        self.assertEqual(response.status_code, 200)
        # レスポンス(配列・構造体)
        self.assertQuerysetEqual(
            response.context['question_list'],
            [res_q1, res_q2],
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
        response = self.client.get(reverse('question:questions'))

        # テスト ---------------------------------------------------
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
    def test_manage(self):
        """
        ----------------------------------------------------------------
        ** テスト内容 **
        該当の問題を表示できるか
        ** 入力値 **
        
        ** 期待値 **
        
        ----------------------------------------------------------------
        """
        # データ作成 ------------------------------------------------
        u = self.make_user('u1', 'a@b.jp', '0000')
        u_other = self.make_user('u2', 'a@b.jp', '0000')
        q1 = self.make_question(1, u.id)
        q2 = self.make_question(2, u.id)
        q3 = self.make_question(3, u_other.id)


        lu = self.make_login_user(u.id, u.username)

        # 実行 -----------------------------------------------------
        url = reverse('question:manage', args=(u.id, ))
        response = self.client.get(url)

        # テスト ---------------------------------------------------
        res_q1 = "<Question: 1>"
        res_q2 = "<Question: 2>"
        # レスポンス
        self.assertEqual(response.status_code, 200)
        # レスポンス(配列・構造体)
        self.assertQuerysetEqual(
            response.context['question_list'],
            [res_q1, res_q2],
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
        u = self.make_user('u1', 'a@n.jp', '0000')

        # 実行 -----------------------------------------------------
        response = self.client.get(reverse('question:manage', args=(u.id, )))

        # テスト ---------------------------------------------------
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
    def test_detail(self):
        """
        ----------------------------------------------------------------
        ** テスト内容 **
        - 該当の問題の詳細と周辺情報が表示できるか
        ----------------------------------------------------------------
        """
        # データ作成 ------------------------------------------------
        u1 = self.make_user('u1', 'a@b.jp', '0000')
        u2 = self.make_user('u2', 'b@b.jp', '0000')
        u3 = self.make_user('u3', 'c@b.jp', '0000')
        u4 = self.make_user('u4', 'd@b.jp', '0000')

        q = self.make_question(1, u4.id)
        c1 = self.make_collecter(u2.id, q.id)
        c2 = self.make_collecter(u3.id, q.id)

        b = self.make_bookmark(u1.id, q.id)

        lu = self.make_login_user(u1.id, u1.username)

        # 実行 -----------------------------------------------------
        url = reverse('question:detail', args=(q.id, ))
        response = self.client.get(url)

        # テスト ---------------------------------------------------
        res_c2 = '<User: u2>'
        res_c3 = '<User: u3>'
        # レスポンス
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['question'], q)
        self.assertEqual(response.context['is_bookmark'], True)
        # レスポンス(配列・構造体)
        self.assertQuerysetEqual(
            response.context['correct_users'],
            [res_c2, res_c3],
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
        u = self.make_user('u1', 'a@n.jp', '0000')
        q = self.make_question(1, u.id)

        # 実行 -----------------------------------------------------
        response = self.client.get(reverse('question:detail', args=(q.id, )))

        # テスト ---------------------------------------------------
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
        - ユーザーがログインしてない状態でのリダイレクト
        ----------------------------------------------------------------
        """
        # データ作成 ------------------------------------------------

        # 実行 -----------------------------------------------------
        response = self.client.get(reverse('question:create'))

        # テスト ---------------------------------------------------
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
    def test_run_create(self):
        """
        ----------------------------------------------------------------
        ** テスト内容 **
        - 問題の作成ができるか
        ----------------------------------------------------------------
        """
        # データ作成 ------------------------------------------------
        u1 = self.make_user('u1', 'a@b.jp', '0000')

        lu = self.make_login_user(u1.id, u1.username)

        post_data = {
            'name'           : 'q1',
            'question_text'  : 'aaaa',
            'question_input' : 'aaaa',
            'question_output': 'aaaa',
            'default_code'   : 'aaaa',
            'target_user_id' : u1.id,
        }
        # 実行 -----------------------------------------------------
        url = reverse('question:run_create')
        response = self.client.post(url, post_data)

        create_q = Question.objects.get(name = post_data['name'])

        # テスト ---------------------------------------------------
        # レスポンス
        self.assertRedirects(
            response,
            expected_url=reverse('question:manage', args=(u1.id, )),
            status_code=302,
            target_status_code=200,
        )
        self.assertEqual(create_q.name, post_data['name'])

    def test_validate_name(self):
        """
        ----------------------------------------------------------------
        ** テスト内容 **
        - 入力内容のバリデーションチェック(name)
        ----------------------------------------------------------------
        """
        # データ作成 ------------------------------------------------
        u1 = self.make_user('u1', 'a@b.jp', '0000')

        lu = self.make_login_user(u1.id, u1.username)

        post_data = {
            'name'           : '',
            'question_text'  : 'aaaa',
            'question_input' : 'aaaa',
            'question_output': 'aaaa',
            'default_code'   : 'aaaa',
            'target_user_id' : u1.id,
        }
        # 実行 -----------------------------------------------------
        url = reverse('question:run_create')
        response = self.client.post(url, post_data)

        ses_name = ''
        if 'message' in self.client.session:
            ses_name = self.client.session['message']

        # テスト ---------------------------------------------------
        self.assertRedirects(
            response,
            expected_url=reverse('question:create'),
            status_code=302,
            target_status_code=200,
        )
        self.assertEqual(ses_name, '問題名が設定されていません。')


    def test_validate_text(self):
        """
        ----------------------------------------------------------------
        ** テスト内容 **
        - 入力内容のバリデーションチェック(question_text)
        ----------------------------------------------------------------
        """
        # データ作成 ------------------------------------------------
        u1 = self.make_user('u1', 'a@b.jp', '0000')

        lu = self.make_login_user(u1.id, u1.username)

        post_data = {
            'name'           : 'q1',
            'question_text'  : '',
            'question_input' : 'aaaa',
            'question_output': 'aaaa',
            'default_code'   : 'aaaa',
            'target_user_id' : u1.id,
        }
        # 実行 -----------------------------------------------------
        url = reverse('question:run_create')
        response = self.client.post(url, post_data)

        ses_name = ''
        if 'message' in self.client.session:
            ses_name = self.client.session['message']

        # テスト ---------------------------------------------------
        self.assertRedirects(
            response,
            expected_url=reverse('question:create'),
            status_code=302,
            target_status_code=200,
        )
        self.assertEqual(ses_name, '問題文が設定されていません。')

    def test_validate_output(self):
        """
        ----------------------------------------------------------------
        ** テスト内容 **
        - 入力内容のバリデーションチェック(question_output)
        ----------------------------------------------------------------
        """
        # データ作成 ------------------------------------------------
        u1 = self.make_user('u1', 'a@b.jp', '0000')

        lu = self.make_login_user(u1.id, u1.username)

        post_data = {
            'name'           : 'q1',
            'question_text'  : 'aaaa',
            'question_input' : 'aaaa',
            'question_output': '',
            'default_code'   : 'aaaa',
            'target_user_id' : u1.id,
        }
        # 実行 -----------------------------------------------------
        url = reverse('question:run_create')
        response = self.client.post(url, post_data)

        ses_name = ''
        if 'message' in self.client.session:
            ses_name = self.client.session['message']

        # テスト ---------------------------------------------------
        self.assertRedirects(
            response,
            expected_url=reverse('question:create'),
            status_code=302,
            target_status_code=200,
        )
        self.assertEqual(ses_name, '出力値(答え)が設定されていません。')


    def test_redirect(self):
        """
        ----------------------------------------------------------------
        ** テスト内容 **
        - ユーザーがログインしてない状態でのリダイレクト
        ----------------------------------------------------------------
        """
        # データ作成 ------------------------------------------------

        # 実行 -----------------------------------------------------
        response = self.client.get(reverse('question:run_create'))

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
    問題／編集ページ
    ----------------------------------------------------------------------
    """
    def test_edit(self):
        """
        ----------------------------------------------------------------
        ** テスト内容 **
        - 問題をDBから取得できているか
        - セッションからメッセージを取得できているか
        ----------------------------------------------------------------
        """
        # データ作成 ------------------------------------------------
        u1 = self.make_user('u1', 'a@b.jp', '0000')
        q = self.make_question(1, u1.id)

        lu = self.make_login_user(u1.id, u1.username)

        ses = self.make_message('aaaa')

        # 実行 -----------------------------------------------------
        url = reverse('question:edit', args=(q.id, ))
        response = self.client.get(url)

        # テスト ---------------------------------------------------
        # レスポンス
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['message'], 'aaaa')
        self.assertEqual(response.context['question'], q)
        
    def test_edit_with_no_question(self):
        """
        ----------------------------------------------------------------
        ** テスト内容 **
        - 該当する問題情報がない時に適切な処理ができるか
        ----------------------------------------------------------------
        """
        # データ作成 ------------------------------------------------
        u1 = self.make_user('u1', 'a@b.jp', '0000')
        q = self.make_question(1, u1.id)

        lu = self.make_login_user(u1.id, u1.username)

        ses = self.make_message('aaaa')

        # 実行 -----------------------------------------------------
        url = reverse('question:edit', args=(0, ))
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
        u = self.make_user('u1', 'a@n.jp', '0000')
        q = self.make_question(1, u.id)


        # 実行 -----------------------------------------------------
        response = self.client.get(reverse('question:edit', args=(q.id, )))

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
    問題／編集処理
    ----------------------------------------------------------------------
    """
    def test_run_edit(self):
        """
        ----------------------------------------------------------------
        ** テスト内容 **
        - POSTデータを取得して変更できるか
        
        ----------------------------------------------------------------
        """
        # データ作成 ------------------------------------------------
        u = self.make_user('u1', 'a@b.jp', '0000')
        q = self.make_question(1, u.id)

        lu = self.make_login_user(u.id, u.username)

        post_data = {
            'question_id'    : q.id,
            'name'           : 'aaaa',
            'question_text'  : 'aaaa',
            'question_input' : 'aaaa',
            'question_output': 'aaaa',
            'default_code'   : 'aaaa',
        }

        # 実行 -----------------------------------------------------
        url = reverse('question:run_edit', args=(q.id, ))
        response = self.client.post(url, post_data)

        update_q = Question.objects.get(pk=q.id)

        # テスト ---------------------------------------------------
        self.assertEqual(update_q.name           , 'aaaa')
        self.assertEqual(update_q.question_text  , 'aaaa')
        self.assertEqual(update_q.question_input , 'aaaa')
        self.assertEqual(update_q.question_output, 'aaaa')
        self.assertEqual(update_q.default_code   , 'aaaa')
        self.assertRedirects(
            response,
            expected_url=reverse('question:manage', args=(u.id, )),
            status_code=302,
            target_status_code=200,
        )

    def test_run_edit_with_no_question_id(self):
        """
        ----------------------------------------------------------------
        ** テスト内容 **
        - question_idに該当する問題が存在しない時エラーページに飛ぶか
        ----------------------------------------------------------------
        """
        # データ作成 ------------------------------------------------
        u = self.make_user('u1', 'a@b.jp', '0000')
        q = self.make_question(1, u.id)

        lu = self.make_login_user(u.id, u.username)

        post_data = {
            'question_id'    : q.id,
            'name'           : 'aaaa',
            'question_text'  : 'aaaa',
            'question_input' : 'aaaa',
            'question_output': 'aaaa',
            'default_code'   : 'aaaa',
        }

        # 実行 -----------------------------------------------------
        url = reverse('question:run_edit', args=(0, ))
        response = self.client.post(url, post_data)

        # テスト ---------------------------------------------------
        self.assertRedirects(
            response,
            expected_url=reverse('errors:errors'),
            status_code=302,
            target_status_code=200,
        )


    def test_validate_name(self):
        """
        ----------------------------------------------------------------
        ** テスト内容 **
        - 入力情報のバリデーション(name)
        - セッションにメッセージは格納されているか
        ----------------------------------------------------------------
        """
        # データ作成 ------------------------------------------------
        u = self.make_user('u1', 'a@b.jp', '0000')
        q = self.make_question(1, u.id)

        lu = self.make_login_user(u.id, u.username)

        post_data = {
            'question_id'    : q.id,
            'name'           : '',
            'question_text'  : 'aaaa',
            'question_input' : 'aaaa',
            'question_output': 'aaaa',
            'default_code'   : 'aaaa',
        }

        # 実行 -----------------------------------------------------
        url = reverse('question:run_edit', args=(q.id, ))
        response = self.client.post(url, post_data)

        ses = ''
        if 'message' in self.client.session:
            ses = self.client.session['message']

        # テスト ---------------------------------------------------
        self.assertRedirects(
            response,
            expected_url=reverse('question:edit', args=(q.id, )),
            status_code=302,
            target_status_code=200,
        )
        self.assertEqual(ses, '問題名が設定されていません。')


    def test_validate_question_text(self):
        """
        ----------------------------------------------------------------
        ** テスト内容 **
        - 入力情報のバリデーション(question_text)
        - セッションにメッセージは格納されているか
        ----------------------------------------------------------------
        """
        # データ作成 ------------------------------------------------
        u = self.make_user('u1', 'a@b.jp', '0000')
        q = self.make_question(1, u.id)

        lu = self.make_login_user(u.id, u.username)

        post_data = {
            'question_id'    : q.id,
            'name'           : 'aaaa',
            'question_text'  : '',
            'question_input' : 'aaaa',
            'question_output': 'aaaa',
            'default_code'   : 'aaaa',
        }

        # 実行 -----------------------------------------------------
        url = reverse('question:run_edit', args=(q.id, ))
        response = self.client.post(url, post_data)

        ses = ''
        if 'message' in self.client.session:
            ses = self.client.session['message']

        # テスト ---------------------------------------------------
        self.assertRedirects(
            response,
            expected_url=reverse('question:edit', args=(q.id, )),
            status_code=302,
            target_status_code=200,
        )
        self.assertEqual(ses, '問題文が設定されていません。')

    def test_validate_question_output(self):
        """
        ----------------------------------------------------------------
        ** テスト内容 **
        - 入力情報のバリデーション(question_output)
        - セッションにメッセージは格納されているか
        ----------------------------------------------------------------
        """
        # データ作成 ------------------------------------------------
        u = self.make_user('u1', 'a@b.jp', '0000')
        q = self.make_question(1, u.id)

        lu = self.make_login_user(u.id, u.username)

        post_data = {
            'question_id'    : q.id,
            'name'           : 'aaaa',
            'question_text'  : 'aaaa',
            'question_input' : 'aaaa',
            'question_output': '',
            'default_code'   : 'aaaa',
        }

        # 実行 -----------------------------------------------------
        url = reverse('question:run_edit', args=(q.id, ))
        response = self.client.post(url, post_data)

        ses = ''
        if 'message' in self.client.session:
            ses = self.client.session['message']

        # テスト ---------------------------------------------------
        self.assertRedirects(
            response,
            expected_url=reverse('question:edit', args=(q.id, )),
            status_code=302,
            target_status_code=200,
        )
        self.assertEqual(ses, '出力値(答え)が設定されていません。')


    def test_redirect(self):
        """
        ----------------------------------------------------------------
        ** テスト内容 **
        - ユーザーがログインしてない状態でのリダイレクト
        ----------------------------------------------------------------
        """
        # データ作成 ------------------------------------------------
        u = self.make_user('u1', 'a@n.jp', '0000')
        q = self.make_question(1, u.id)

        # 実行 -----------------------------------------------------
        response = self.client.get(reverse('question:run_edit', args=(q.id, )))

        # テスト ---------------------------------------------------
        self.assertRedirects(
            response,
            expected_url=reverse('top:top'),
            status_code=302,
            target_status_code=200,
        )