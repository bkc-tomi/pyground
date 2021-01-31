from django.shortcuts import render
from django.urls      import reverse
from django.http      import HttpResponse, HttpResponseRedirect

# モデル
from .models         import Question, Correcter
from user.models     import User, Profile
from bookmark.models import Bookmark

def questions(request):
    """
    ----------------------------------------------------------------------
    問題／一覧ページ
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
        # 問題の取得 ---------------------------------------
        question_list = Question.objects.all()

        # -------------------------------------------------------
        # ページ遷移
        # -------------------------------------------------------
        return render(request, 'question/index.html', {
            'question_list': question_list,
        })

    # -------------------------------------------------------
    # エラー処理
    # -------------------------------------------------------
    except Exception as e:
        errors = {
            'type': str(type(e)),
            'args': str(e.args),
            'err' : str(e),
            'msg' : '',
        }
        request.session['errors'] = errors
        return HttpResponseRedirect(reverse('errors:errors'))

def manage(request, user_id):
    """
    ----------------------------------------------------------------------
    問題／管理ページ
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
        # ユーザーID取得
        user_id = login_user['id']

        # フォロー情報取得 ----------------------------------
        question_list = Question.objects.filter(target_user_id=user_id)

        # -------------------------------------------------------
        # ページ遷移
        # -------------------------------------------------------
        return render(request, 'question/manage.html', {
            'user_id'      : user_id,
            'question_list': question_list,
        })

    # -------------------------------------------------------
    # エラー処理
    # -------------------------------------------------------
    except Exception as e:
        errors = {
            'type': str(type(e)),
            'args': str(e.args),
            'err' : str(e),
            'msg' : '',
        }
        request.session['errors'] = errors
        return HttpResponseRedirect(reverse('errors:errors'))

def detail(request, question_id):
    """
    ----------------------------------------------------------------------
    問題／詳細ページ
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
        questions      = {}
        correct_users = []
        # 質問の取得 -----------------------------------
        question = Question.objects.get(pk=question_id)

        # 正解者の取得 ---------------------------------
        # 正解者テーブルの取得
        temps = Correcter.objects.filter(target_question_id=question_id)
        
        # 正解ユーザーの取得
        for temp in temps:
            user_id = temp.correct_user_id
            user = User.objects.get(pk=user_id)
            correct_users.append(user)
        
        # ブックマークの取得 -----------------------------
        # ブックマークの取得
        user_id = login_user['id']
        bookmark = Bookmark.objects.filter(
            target_question_id = question_id,
            target_user_id     = user_id,
        )

        # ブックマーク判定
        is_bookmark = False
        if len(bookmark) == 1:
            is_bookmark = True

        # -------------------------------------------------------
        # ページ遷移
        # -------------------------------------------------------
        return render(request, 'question/detail.html', {
            'user_id'      : user_id,
            'question'     : question,
            'correct_users': correct_users,
            'is_bookmark'  : is_bookmark,
        })

    # -------------------------------------------------------
    # エラー処理
    # -------------------------------------------------------
    except Exception as e:
        errors = {
            'type': str(type(e)),
            'args': str(e.args),
            'err' : str(e),
            'msg' : '',
        }
        request.session['errors'] = errors
        return HttpResponseRedirect(reverse('errors:errors'))

def create(request):
    """
    ----------------------------------------------------------------------
    問題／新規作成ページ
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
        # 値取得
        # -------------------------------------------------------
        # ユーザーID取得 -----------------------------------
        target_user_id = login_user['id']

        # メッセージの取得 -----------------------------------
        message = ''
        if 'message' in request.session:
            message = request.session['message']

            del request.session['message']

        # -------------------------------------------------------
        # ページ遷移
        # -------------------------------------------------------
        return render(request, 'question/create.html', {
            'target_user_id': target_user_id,
            'message'       : message,
        })

    # -------------------------------------------------------
    # エラー処理
    # -------------------------------------------------------
    except Exception as e:
        errors = {
            'type': str(type(e)),
            'args': str(e.args),
            'err' : str(e),
            'msg' : '',
        }
        request.session['errors'] = errors
        return HttpResponseRedirect(reverse('errors:errors'))

def run_create(request):
    """
    ----------------------------------------------------------------------
    問題／新規作成処理
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
        # バリデーション
        # -------------------------------------------------------
        if request.POST['name'] == '':
            request.session['message'] = '問題名が設定されていません。'
            return HttpResponseRedirect(reverse('question:create'))

        if request.POST['question_text'] == '':
            request.session['message'] = '問題文が設定されていません。'
            return HttpResponseRedirect(reverse('question:create'))

        if request.POST['question_output'] == '':
            request.session['message'] = '出力値(答え)が設定されていません。'
            return HttpResponseRedirect(reverse('question:create'))

        # -------------------------------------------------------
        # データベース保存
        # -------------------------------------------------------
        question = Question(
            name           =request.POST['name'],
            question_text  =request.POST['question_text'],
            question_input =request.POST['question_input'],
            question_output=request.POST['question_output'],
            default_code   =request.POST['default_code'],
            target_user_id =request.POST['target_user_id'],
        )
        question.save()

        # -------------------------------------------------------
        # 描画データ取得
        # -------------------------------------------------------
        # ユーザーID取得
        user_id = login_user['id']

        # -------------------------------------------------------
        # ページ遷移
        # -------------------------------------------------------
        # 問題管理ページへ
        return HttpResponseRedirect(reverse('question:manage', args=(user_id,)))

    # -------------------------------------------------------
    # エラー処理
    # -------------------------------------------------------
    except Exception as e:
        errors = {
            'type': str(type(e)),
            'args': str(e.args),
            'err' : str(e),
            'msg' : '',
        }
        request.session['errors'] = errors
        return HttpResponseRedirect(reverse('errors:errors'))

def edit(request, question_id):
    """
    ----------------------------------------------------------------------
    問題／編集ページ
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
        # ユーザーIDの取得
        user_id = login_user['id']

        # 問題の取得 --------------------------------------
        question = {}
        question = Question.objects.get(pk=question_id)

        # メッセージの取得 ---------------------------------
        message = ''
        if 'message' in request.session:
            message = request.session['message']

            del request.session['message']

        # -------------------------------------------------------
        # ページ遷移
        # -------------------------------------------------------
        return render(request, 'question/edit.html', {
            'user_id' : user_id,
            'question': question,
            'message' : message,
        })

    # -------------------------------------------------------
    # エラー処理
    # -------------------------------------------------------
    except Exception as e:
        errors = {
            'type': str(type(e)),
            'args': str(e.args),
            'err' : str(e),
            'msg' : '',
        }
        request.session['errors'] = errors
        return HttpResponseRedirect(reverse('errors:errors'))

def run_edit(request, question_id):
    """
    ----------------------------------------------------------------------
    問題／編集処理
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
        # バリデーション
        # -------------------------------------------------------
        if request.POST['name'] == '':
            request.session['message'] = '問題名が設定されていません。'
            return HttpResponseRedirect(reverse('question:create'))

        if request.POST['question_text'] == '':
            request.session['message'] = '問題文が設定されていません。'
            return HttpResponseRedirect(reverse('question:create'))

        if request.POST['question_output'] == '':
            request.session['message'] = '出力値(答え)が設定されていません。'
            return HttpResponseRedirect(reverse('question:create'))

        # -------------------------------------------------------
        # データベース保存
        # -------------------------------------------------------
        # DB処理 ----------------------------------------
        question = Question.objects.get(pk=request.POST['question_id'])
        question.name            = request.POST['name']
        question.question_text   = request.POST['question_text']
        question.question_input  = request.POST['question_input']
        question.question_output = request.POST['question_output']
        question.default_code    = request.POST['default_code']
        question.save()

        # -------------------------------------------------------
        # 描画データ取得
        # -------------------------------------------------------
        # ユーザーID取得
        user_id = login_user['id']

        # -------------------------------------------------------
        # ページ遷移
        # -------------------------------------------------------
        # 問題管理ページへ
        return HttpResponseRedirect(
            reverse('question:manage', args=(user_id, ))
        )

    # -------------------------------------------------------
    # エラー処理
    # -------------------------------------------------------
    except Exception as e:
        errors = {
            'type': str(type(e)),
            'args': str(e.args),
            'err' : str(e),
            'msg' : '',
        }
        request.session['errors'] = errors
        return HttpResponseRedirect(reverse('errors:errors'))