from django.shortcuts import render
from django.urls      import reverse
from django.http      import HttpResponse, HttpResponseRedirect

# モデル
from .models         import Bookmark
from question.models import Question
from user.models     import User, Profile

"""
----------------------------------------------------------------------
ブックマーク／一覧表示
----------------------------------------------------------------------
"""
def index(request, user_id):
    """
    ---------------------------------------------------------
    セッション
    ---------------------------------------------------------
    """
    if 'login_user' not in request.session:
        return HttpResponseRedirect(reverse('top:top'))
    
    login_user = request.session['login_user']

    """
    ---------------------------------------------------------
    描画データ取得
    ---------------------------------------------------------
    """
    # 対象ユーザー
    user_id = login_user['id']

    # ブックマークの取得 --------------------------------
    temps = {}
    # DB取得
    try:
        temps = Bookmark.objects.filter(target_user_id=user_id)
    except Exception as e:
        print('err:' + str(e))
        # # 前のページにリダイレクト
        # return HttpResponseRedirect(request.META.get("HTTP_REFERER"))
        

    # 描画オブジェクトの作成 -----------------------------
    bookmark_list = []
    try:
        for temp in temps:
            question = Question.objects.get(pk=temp.target_question_id)
            bookmark = {
                'id'      : temp.id,
                'question': question,
            }
            bookmark_list.append(bookmark)

    except Exception as e:
        print('err:' + str(e))
        # # 前のページにリダイレクト
        # return HttpResponseRedirect(request.META.get("HTTP_REFERER"))
        
    
    """
    ---------------------------------------------------------
    ページ遷移
    ---------------------------------------------------------
    """
    return render(request, 'bookmark/index.html', {
        'user_id'  : user_id,
        'bookmark_list': bookmark_list,
    })

"""
----------------------------------------------------------------------
ブックマーク／ブックマーク処理
----------------------------------------------------------------------
"""
def run_bookmark(request, question_id):
    """
    ---------------------------------------------------------
    セッション
    ---------------------------------------------------------
    """
    if 'login_user' not in request.session:
        return HttpResponseRedirect(reverse('top:top'))
    
    login_user = request.session['login_user']

    """
    ---------------------------------------------------------
    データベース操作
    ---------------------------------------------------------
    """
    # 各種ID取得 -------------------------------------
    # ユーザーID
    user_id = login_user['id']
    
    # DB登録 ----------------------------------------
    try:
        bookmark = Bookmark(
            target_question_id = question_id,
            target_user_id = user_id,
        )
        bookmark.save()

    except Exception as e:
        print('err:' + str(e))
        # 前のページにリダイレクト
        return HttpResponseRedirect(request.META.get("HTTP_REFERER"))

    """
    ---------------------------------------------------------
    ページ遷移
    ---------------------------------------------------------
    """
    # 前のページにリダイレクト
    return HttpResponseRedirect(request.META.get("HTTP_REFERER"))

"""
----------------------------------------------------------------------
ブックマーク／ブックマーク解除
----------------------------------------------------------------------
"""
def release(request, bookmark_id):
    """
    ---------------------------------------------------------
    セッション
    ---------------------------------------------------------
    """
    if 'login_user' not in request.session:
        return HttpResponseRedirect(reverse('top:top'))
    
    login_user = request.session['login_user']

    """
    ---------------------------------------------------------
    データベース操作
    ---------------------------------------------------------
    """
    # DB更新 -----------------------------------------
    try:
        bookmark = Bookmark.objects.get(pk=bookmark_id)
        bookmark.delete()
    except Exception as e:
        print('err:' + str(e))

    """
    ---------------------------------------------------------
    ページ遷移
    ---------------------------------------------------------
    """
    # 前のページにリダイレクト
    return HttpResponseRedirect(request.META.get("HTTP_REFERER"))