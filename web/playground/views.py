from django.shortcuts import render
from django.urls      import reverse
from django.http      import HttpResponse, HttpResponseRedirect

# モデル
from .models         import Code
from user.models     import User
from question.models import Question, Correcter

# コード実行関数
from .code.execute import exec_code

def index(request):
    """
    ----------------------------------------------------------------------
    プレイグランド／プレイグランド
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
        # 描画配列作成
        # -------------------------------------------------------
        # コード ----------------------------------------
        # 初期値
        code_name = ""
        code = """\
# フィボナッチ数列

a, b = 0, 1
while a < 1000:
    print(a, end=' ')
    a, b = b, a+b
"""
        # 変更を更新
        if 'code' in request.session:
            code = request.session['code']
        
            # セッションデータの破棄
            del request.session['code']

        # 実行結果 --------------------------------------
        # 初期値
        result = """\
左のコードを消して、好きなコードを書いてください。
ライブラリ等のインポートには対応していません。
"""

        # 変更を更新
        if 'result' in request.session:
            result = request.session['result']

            # セッションデータの破棄
            del request.session['result']

        # -------------------------------------------------------
        # ページ遷移
        # -------------------------------------------------------
        return render(request, 'playground/index.html', {
            'code_name'  : code_name,
            'code'       : code,
            'result'     : result,
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

def run(request):
    """
    ----------------------------------------------------------------------
    プレイグランド／実行処理
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
        code_name = request.POST['code-name']
        code      = request.POST['code']

        # -------------------------------------------------------
        # コード実行
        # -------------------------------------------------------
        result = exec_code(code)

        # -------------------------------------------------------
        # 描画配列作成
        # -------------------------------------------------------
        # セッションに結果を格納
        request.session['result'] = result
        request.session['code']   = code

        # -------------------------------------------------------
        # ページ遷移
        # -------------------------------------------------------
        return HttpResponseRedirect(reverse('playground:index'))

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

def edit(request, code_id):
    """
    ----------------------------------------------------------------------
    プレイグランド／コード編集
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
        # DBから取得 -----------------------------------------
        code = Code.objects.get(pk=code_id)

        # 変更を更新
        if 'code' in request.session:
            code.code = request.session['code']
        
            # セッションデータの破棄
            del request.session['code']

        # 実行結果 --------------------------------------
        # 初期値
        result = ''

        # 変更を更新
        if 'result' in request.session:
            result = request.session['result']

            # セッションデータの破棄
            del request.session['result']

        # -------------------------------------------------------
        # ページ遷移
        # -------------------------------------------------------
        return render(request, 'playground/edit.html', {
            'code'  : code,
            'result': result,
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

def run_edit(request, code_id):
    """
    ----------------------------------------------------------------------
    プレイグランド／編集実行処理
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
        code_name = request.POST['code-name']
        code      = request.POST['code']

        # -------------------------------------------------------
        # コード実行
        # -------------------------------------------------------
        result = exec_code(code)

        # -------------------------------------------------------
        # 描画配列作成
        # -------------------------------------------------------
        # セッションに結果を格納
        request.session['result'] = result
        request.session['code']   = code

        # -------------------------------------------------------
        # ページ遷移
        # -------------------------------------------------------
        return HttpResponseRedirect(
            reverse('playground:edit', args=(code_id,)),
        )

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

def question(request, question_id):
    """
    ----------------------------------------------------------------------
    プレイグランド／問題ページ
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
        question = Question.objects.get(pk=question_id)
        
        # 変更を更新
        if 'code' in request.session:
            question.default_code = request.session['code']
        
            # セッションデータの破棄
            del request.session['code']

        # 実行結果 --------------------------------------
        # 初期値
        result = ''

        # 変更を更新
        if 'result' in request.session:
            result = request.session['result']

            # セッションデータの破棄
            del request.session['result']

        # -------------------------------------------------------
        # ページ遷移
        # -------------------------------------------------------
        return render(request, 'playground/question.html', {
            'question': question,
            'result'  : result,
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

def run_question(request, question_id):
    """
    ----------------------------------------------------------------------
    プレイグランド／問題処理
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
        code   = request.POST['code']
        answer = request.POST['answer']

        # -------------------------------------------------------
        # コード実行
        # -------------------------------------------------------
        # 実行結果
        run = exec_code(code)

        # 正解判定
        run = ''.join(run.splitlines())

        if run == answer:
            judge = '正解'
        else:
            judge = '不正解'
        
        result = f"""\
実行結果: { run }
答え　　: { answer }
判定　　: { judge }
        """
        # -------------------------------------------------------
        # 正解者登録
        # -------------------------------------------------------
        user_id = login_user['id']
        if judge == '正解':
            if not Correcter.objects.filter(correct_user_id=user_id).exists():
                correcter = Correcter(
                    correct_user_id    = user_id,
                    target_question_id = question_id,
                )
                correcter.save()

        # -------------------------------------------------------
        # 描画配列作成
        # -------------------------------------------------------
        # セッションに結果を格納
        request.session['result'] = result
        request.session['code']   = code

        # -------------------------------------------------------
        # ページ遷移
        # -------------------------------------------------------
        return HttpResponseRedirect(
            reverse('playground:question', args=(question_id,)),
        )

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

def save(request):
    """
    ----------------------------------------------------------------------
    プレイグランド／保存処理
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
        # データベース保存
        # -------------------------------------------------------
        # DB登録 ------------------------------------------
        code = Code(
            name           = request.POST['code-name'],
            code           = request.POST['code'],
            target_user_id = login_user['id'],
        )
        code.save()

        # -------------------------------------------------------
        # ページ遷移
        # -------------------------------------------------------
        return HttpResponseRedirect(
            reverse('playground:edit', args=(code.id,))
        )

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

def update(request, code_id):
    """
    ----------------------------------------------------------------------
    プレイグランド／更新処理
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
        # データベース保存
        # -------------------------------------------------------
        # DB更新 ------------------------------------------
        code = Code.objects.get(pk=code_id)
        code.name = request.POST['code-name']
        code.code = request.POST['code']
        code.save()

        # -------------------------------------------------------
        # ページ遷移
        # -------------------------------------------------------
        return HttpResponseRedirect(
            reverse('playground:edit', args=(code.id,))
        )

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