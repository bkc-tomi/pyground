from django.shortcuts import render
from django.urls      import reverse
from django.http      import HttpResponse, HttpResponseRedirect

"""
----------------------------------------------------------------------
プレイグランド／プレイグランド
----------------------------------------------------------------------
"""
def index(request):
    return render(request, 'playground/index.html')

"""
----------------------------------------------------------------------
プレイグランド／実行処理
----------------------------------------------------------------------
"""
def run(request):
    return render(request, 'playground/index.html')

"""
----------------------------------------------------------------------
プレイグランド／コード編集
----------------------------------------------------------------------
"""
def edit(request, code_id):
    return render(request, 'playground/edit.html', {
        'code_id': code_id,
    })

"""
----------------------------------------------------------------------
プレイグランド／編集実行処理
----------------------------------------------------------------------
"""
def run_edit(request, code_id):
    return render(request, 'playground/edit.html', {
        'code_id': code_id,
    })

"""
----------------------------------------------------------------------
プレイグランド／問題ページ
----------------------------------------------------------------------
"""
def question(request, question_id):
    return render(request, 'playground/question.html', {
        'question_id': question_id,
    })

"""
----------------------------------------------------------------------
プレイグランド／問題処理
----------------------------------------------------------------------
"""
def run_question(request, question_id):
    return render(request, 'playground/question.html', {
        'question_id': question_id,
    })

"""
----------------------------------------------------------------------
プレイグランド／保存処理
----------------------------------------------------------------------
"""
def save(request):
    # 前のページにリダイレクト
    return HttpResponseRedirect(reverse('user:detail', args=(1,)))

"""
----------------------------------------------------------------------
プレイグランド／保存処理
----------------------------------------------------------------------
"""
def update(request, code_id):
    # 前のページにリダイレクト
    return HttpResponseRedirect(reverse('user:detail', args=(1,)))
