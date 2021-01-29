from django.test import TestCase
from django.conf import settings
from importlib   import import_module
from django.urls import reverse


# モデル
from bookmark.models   import Bookmark
from friend.models     import Follow, Permit
from playground.models import Code
from question.models   import Question, Correcter
from user.models       import User, Profile


class CommonTestCase(TestCase):
    """
    ----------------------------------------------------------------
    共通で読み込むテストクラス
    ----------------------------------------------------------------
    """
    def setUp(self):
        """
        -----------------------------------------------
        セッションの設定
        -----------------------------------------------
        """
        settings.SESSION_ENGINE = 'django.contrib.sessions.backends.file'
        engine = import_module(settings.SESSION_ENGINE)
        store = engine.SessionStore()
        store.save()
        self.session = store
        self.client.cookies[settings.SESSION_COOKIE_NAME] = store.session_key

    def make_user(self, username, email, password):
        """
        -----------------------------------------------
        ユーザーの作成
        -----------------------------------------------
        """
        return User.objects.create(
            username = username,
            email    = email,
            password = password,
        )

    def make_question(self, question_number, target_user_id):
        """
        -----------------------------------------------
        問題の作成
        -----------------------------------------------
        """
        return Question.objects.create(
            name            = question_number,
            question_text   = "text: " + str(question_number),
            target_user_id  = target_user_id,
            question_input  = "input: " + str(question_number),
            question_output = "output: " + str(question_number),
            default_code    = "code: " + str(question_number),
        )

    def make_login_user(self, user_id, username):
        """
        -----------------------------------------------
        ログインユーザーの作成
        -----------------------------------------------
        """
        session = self.session
        session['login_user'] = {
            'id'      : user_id,
            'username': username,
        }
        session.save()

    def make_profile(self, user_id, publish):
        """
        -----------------------------------------------
        プロフィールの作成
        -----------------------------------------------
        """
        return Profile.objects.create(
            profile_text   = str(user_id) + "です。よろしく",
            publish        = publish,
            target_user_id = user_id,
        )
    
    def make_collecter(self, user_id, question_id):
        """
        -----------------------------------------------
        正解者の作成
        -----------------------------------------------
        """
        return Correcter.objects.create(
            target_user_id     = user_id,
            target_question_id = question_id,
        )

    def make_code(self, user_id, code_name):
        """
        -----------------------------------------------
        コードの作成
        -----------------------------------------------
        """
        return Code.objects.create(
            code           = f"print('hello { code_name }')",
            target_user_id = user_id,
            name           = code_name,
        )
    
    def make_relation(self, follow_id, followed_id):
        """
        -----------------------------------------------
        フォロー・フォロワーの作成
        -----------------------------------------------
        """
        return Follow.objects.create(
            follow_user_id   = follow_id,
            followed_user_id = followed_id,
        )
    
    def make_permit(self, request_id, target_id):
        """
        -----------------------------------------------
        申請の作成
        -----------------------------------------------
        """
        return Permit.objects.create(
            request_user_id = request_id,
            target_user_id  = target_id,
        )

    def make_bookmark(self, user_id, question_id):
        """
        -----------------------------------------------
        ブックマークの作成
        -----------------------------------------------
        """
        return Bookmark.objects.create(
            target_user_id     = user_id,
            target_question_id = question_id,
        )