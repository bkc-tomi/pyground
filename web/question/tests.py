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
    def test_questions(self):
        """
        ----------------------------------------------------------------
        ** テスト内容 **
        質問一覧を表示できるか
        ** 入力値 **
        
        ** 期待値 **
        
        ----------------------------------------------------------------
        """
        # データ作成 ------------------------------------------------

        # 実行 -----------------------------------------------------

        # テスト ---------------------------------------------------


    def test_questions_with_no_question(self):
        """
        ----------------------------------------------------------------
        ** テスト内容 **
        該当する問題がない時の表示
        ** 入力値 **
        
        ** 期待値 **
        
        ----------------------------------------------------------------
        """
        # データ作成 ------------------------------------------------

        # 実行 -----------------------------------------------------

        # テスト ---------------------------------------------------


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

        # 実行 -----------------------------------------------------

        # テスト ---------------------------------------------------


    def test_manage_with_no_question(self):
        """
        ----------------------------------------------------------------
        ** テスト内容 **
        該当の問題がない時の表示
        ** 入力値 **
        
        ** 期待値 **
        
        ----------------------------------------------------------------
        """
        # データ作成 ------------------------------------------------

        # 実行 -----------------------------------------------------

        # テスト ---------------------------------------------------



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
        該当の問題の詳細と周辺情報が表示できるか
        ** 入力値 **
        
        ** 期待値 **
        
        ----------------------------------------------------------------
        """
        # データ作成 ------------------------------------------------

        # 実行 -----------------------------------------------------

        # テスト ---------------------------------------------------


    def test_is_bookmark_true(self):
        """
        ----------------------------------------------------------------
        ** テスト内容 **
        周辺情報であるブックマーク情報を正しく表示できるか
        ** 入力値 **
        
        ** 期待値 **
        
        ----------------------------------------------------------------
        """
        # データ作成 ------------------------------------------------

        # 実行 -----------------------------------------------------

        # テスト ---------------------------------------------------

    
    def test_is_bookmark_false(self):
        """
        ----------------------------------------------------------------
        ** テスト内容 **
        周辺情報であるブックマーク情報を正しく表示できるか
        ** 入力値 **
        
        ** 期待値 **
        
        ----------------------------------------------------------------
        """
        # データ作成 ------------------------------------------------

        # 実行 -----------------------------------------------------

        # テスト ---------------------------------------------------


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
    def test_create(self):
        """
        ----------------------------------------------------------------
        ** テスト内容 **
        問題ページの情報を表示できるか
        ** 入力値 **
        
        ** 期待値 **
        
        ----------------------------------------------------------------
        """
        # データ作成 ------------------------------------------------

        # 実行 -----------------------------------------------------

        # テスト ---------------------------------------------------

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
        問題の作成ができるか
        ** 入力値 **
        
        ** 期待値 **
        
        ----------------------------------------------------------------
        """
        # データ作成 ------------------------------------------------

        # 実行 -----------------------------------------------------

        # テスト ---------------------------------------------------


    def test_validate_name(self):
        """
        ----------------------------------------------------------------
        ** テスト内容 **
        入力内容のバリデーションチェック(name)
        ** 入力値 **
        
        ** 期待値 **
        
        ----------------------------------------------------------------
        """
        # データ作成 ------------------------------------------------

        # 実行 -----------------------------------------------------

        # テスト ---------------------------------------------------


    def test_validate_text(self):
        """
        ----------------------------------------------------------------
        ** テスト内容 **
        入力内容のバリデーションチェック(text)
        ** 入力値 **
        
        ** 期待値 **
        
        ----------------------------------------------------------------
        """
        # データ作成 ------------------------------------------------

        # 実行 -----------------------------------------------------

        # テスト ---------------------------------------------------


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
        編集ページに必要な情報を表示できるか
        ** 入力値 **
        
        ** 期待値 **
        
        ----------------------------------------------------------------
        """
        # データ作成 ------------------------------------------------

        # 実行 -----------------------------------------------------

        # テスト ---------------------------------------------------

    def test_edit_with_no_question(self):
        """
        ----------------------------------------------------------------
        ** テスト内容 **
        該当する問題情報がない時に適切な処理ができるか
        ** 入力値 **
        
        ** 期待値 **
        
        ----------------------------------------------------------------
        """
        # データ作成 ------------------------------------------------

        # 実行 -----------------------------------------------------

        # テスト ---------------------------------------------------


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
        問題の編集が登録できるか
        ** 入力値 **
        
        ** 期待値 **
        
        ----------------------------------------------------------------
        """
        # データ作成 ------------------------------------------------

        # 実行 -----------------------------------------------------

        # テスト ---------------------------------------------------


    def test_run_edit_with_no_question_id(self):
        """
        ----------------------------------------------------------------
        ** テスト内容 **
        該当のquestion_idがない時に適切な処理ができるか
        ** 入力値 **
        
        ** 期待値 **
        
        ----------------------------------------------------------------
        """
        # データ作成 ------------------------------------------------

        # 実行 -----------------------------------------------------

        # テスト ---------------------------------------------------


    def test_validate_name(self):
        """
        ----------------------------------------------------------------
        ** テスト内容 **
        入力情報のバリデーション(name)
        ** 入力値 **
        
        ** 期待値 **
        
        ----------------------------------------------------------------
        """
        # データ作成 ------------------------------------------------

        # 実行 -----------------------------------------------------

        # テスト ---------------------------------------------------


    def test_validate_question_text(self):
        """
        ----------------------------------------------------------------
        ** テスト内容 **
        入力情報のバリデーション(text)
        ** 入力値 **
        
        ** 期待値 **
        
        ----------------------------------------------------------------
        """
        # データ作成 ------------------------------------------------

        # 実行 -----------------------------------------------------

        # テスト ---------------------------------------------------


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