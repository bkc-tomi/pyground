from django.shortcuts import render
from django.urls      import reverse
from django.http      import HttpResponse, HttpResponseRedirect

# モデル
from .models         import Code
from user.models     import User
from question.models import Question

# コード実行関数
from .code.execute import exec_code

def index(request):
    """
    ----------------------------------------------------------------------
    プレイグランド／プレイグランド
    ----------------------------------------------------------------------
    """
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
    code = """
def fib(n):
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a+b
    print()
fib(1000)"""
    # 変更を更新
    if 'code' in request.session:
        code = request.session['code']
    
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
    return render(request, 'playground/index.html', {
        'code_name'  : code_name,
        'code'       : code,
        'result'     : result,
    })

def run(request):
    """
    ----------------------------------------------------------------------
    プレイグランド／実行処理
    ----------------------------------------------------------------------
    """
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

def edit(request, code_id):
    """
    ----------------------------------------------------------------------
    プレイグランド／コード編集
    ----------------------------------------------------------------------
    """
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
    try:
        code = Code.objects.get(pk=code_id)
    except Exception as e:
        print('err:' + str(e))
        return HttpResponseRedirect(reverse('top:top'))

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

def run_edit(request, code_id):
    """
    ----------------------------------------------------------------------
    プレイグランド／編集実行処理
    ----------------------------------------------------------------------
    """
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

def question(request, question_id):
    """
    ----------------------------------------------------------------------
    プレイグランド／問題ページ
    ----------------------------------------------------------------------
    """
    # -------------------------------------------------------
    # セッション
    # -------------------------------------------------------
    if 'login_user' not in request.session:
        return HttpResponseRedirect(reverse('top:top'))
    
    login_user = request.session['login_user']

    # -------------------------------------------------------
    # 描画データ取得
    # -------------------------------------------------------
    try:
        question = Question.objects.get(pk=question_id)
        
    except Exception as e:
        print('err:' + str(e))
        return HttpResponseRedirect(reverse('top:top'))
    
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

def run_question(request, question_id):
    """
    ----------------------------------------------------------------------
    プレイグランド／問題処理
    ----------------------------------------------------------------------
    """
    # -------------------------------------------------------
    # セッション
    # -------------------------------------------------------
    if 'login_user' not in request.session:
        return HttpResponseRedirect(reverse('top:top'))
    
    login_user = request.session['login_user']

    # -------------------------------------------------------
    # 値取得
    # -------------------------------------------------------
    code      = request.POST['code']
    answer    = request.POST['answer']

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

def save(request):
    """
    ----------------------------------------------------------------------
    プレイグランド／保存処理
    ----------------------------------------------------------------------
    """
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
    try:
        code = Code(
            name           = request.POST['code-name'],
            code           = request.POST['code'],
            target_user_id = login_user['id'],
        )
        code.save()

    except Exception as e:
        print('err:' + str(e))
        return HttpResponseRedirect(request.META.get("HTTP_REFERER"))

    # -------------------------------------------------------
    # ページ遷移
    # -------------------------------------------------------

    return HttpResponseRedirect(
        reverse('playground:edit', args=(code.id,))
    )

def update(request, code_id):
    """
    ----------------------------------------------------------------------
    プレイグランド／更新処理
    ----------------------------------------------------------------------
    """
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
    try:
        code = Code.objects.get(pk=code_id)
        code.name = request.POST['code-name']
        code.code = request.POST['code']
        code.save()

    except Exception as e:
        print('err:' + str(e))
        return HttpResponseRedirect(request.META.get("HTTP_REFERER"))

    # -------------------------------------------------------
    # ページ遷移
    # -------------------------------------------------------
    return HttpResponseRedirect(
        reverse('playground:edit', args=(code.id,))
    )