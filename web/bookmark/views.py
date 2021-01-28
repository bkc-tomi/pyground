from django.shortcuts import render
from django.urls      import reverse
from django.http      import HttpResponse, HttpResponseRedirect

# モデル
from .models         import Bookmark
from question.models import Question
from user.models     import User, Profile

def index(request, user_id):
    """
    ----------------------------------------------------------------------
    ブックマーク／一覧表示
    ----------------------------------------------------------------------
    """
    try:
        # -------------------------------------------------------
        # セッション
        # -------------------------------------------------------
        if 'login_user' not in request.session:
            return HttpResponseRedirect(reverse('top:top'))
        
        login_user = request.session['login_user']

        # -------------------------------------------------------
        # 描画データ取得
        # -------------------------------------------------------
        # 対象ユーザー
        user_id = login_user['id']

        # ブックマークの取得 --------------------------------
        temps = {}
        # DB取得
        temps = Bookmark.objects.filter(target_user_id=user_id)

        # 描画オブジェクトの作成 -----------------------------
        bookmark_list = []

        for temp in temps:
            question = Question.objects.get(pk=temp.target_question_id)
            bookmark = {
                'id'      : temp.id,
                'question': question,
            }
            bookmark_list.append(bookmark)
            
        # -------------------------------------------------------
        # ページ遷移
        # -------------------------------------------------------
        return render(request, 'bookmark/index.html', {
            'user_id'  : user_id,
            'bookmark_list': bookmark_list,
        })

    # -------------------------------------------------------
    # エラー処理
    # -------------------------------------------------------
    except Exception as e:
        errors = {
            'type': str(type(e)),
            'args': str(e.args),
            'err' : str(e),
        }
        request.session['errors'] = errors
        return HttpResponseRedirect(reverse('errors:errors'))

def run_bookmark(request, question_id):
    """
    ----------------------------------------------------------------------
    ブックマーク／ブックマーク処理
    ----------------------------------------------------------------------
    """
    try:
        # -------------------------------------------------------
        # セッション
        # -------------------------------------------------------
        if 'login_user' not in request.session:
            return HttpResponseRedirect(reverse('top:top'))
        
        login_user = request.session['login_user']

        # -------------------------------------------------------
        # データベース操作
        # -------------------------------------------------------
        # 各種ID取得 -------------------------------------
        # ユーザーID
        user_id = login_user['id']
        
        # DB登録 ----------------------------------------
        bookmark = Bookmark(
            target_question_id = question_id,
            target_user_id = user_id,
        )
        bookmark.save()


        # -------------------------------------------------------
        # ページ遷移
        # -------------------------------------------------------
        # 前のページにリダイレクト
        return HttpResponseRedirect(request.META.get("HTTP_REFERER"))

    # -------------------------------------------------------
    # エラー処理
    # -------------------------------------------------------
    except Exception as e:
        errors = {
            'type': str(type(e)),
            'args': str(e.args),
            'err' : str(e),
        }
        request.session['errors'] = errors
        return HttpResponseRedirect(reverse('errors:errors'))

def release(request, bookmark_id):
    """
    ----------------------------------------------------------------------
    ブックマーク／ブックマーク解除
    ----------------------------------------------------------------------
    """
    try:
        # -------------------------------------------------------
        # セッション
        # -------------------------------------------------------
        if 'login_user' not in request.session:
            return HttpResponseRedirect(reverse('top:top'))
        
        login_user = request.session['login_user']

        # -------------------------------------------------------
        # データベース操作
        # -------------------------------------------------------
        # DB更新 -----------------------------------------
        bookmark = Bookmark.objects.get(pk=bookmark_id)
        bookmark.delete()

        # -------------------------------------------------------
        # ページ遷移
        # -------------------------------------------------------
        # 前のページにリダイレクト
        return HttpResponseRedirect(request.META.get("HTTP_REFERER"))

    # -------------------------------------------------------
    # エラー処理
    # -------------------------------------------------------
    except Exception as e:
        errors = {
            'type': str(type(e)),
            'args': str(e.args),
            'err' : str(e),
        }
        request.session['errors'] = errors
        return HttpResponseRedirect(reverse('errors:errors'))