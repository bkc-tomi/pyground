from django.shortcuts import render
from django.urls      import reverse
from django.http      import HttpResponse, HttpResponseRedirect

"""
----------------------------------------------------------------------
問題／一覧ページ
----------------------------------------------------------------------
"""
def questions(request):
    return render(request, 'question/index.html')

"""
----------------------------------------------------------------------
問題／管理ページ
----------------------------------------------------------------------
"""
def manage(request, user_id):
    return render(request, 'question/manage.html', {
        'user_id': user_id,
    })

"""
----------------------------------------------------------------------
問題／詳細ページ
----------------------------------------------------------------------
"""
def detail(request, question_id):
    return render(request, 'question/detail.html', {
        'question_id': question_id,
    })

"""
----------------------------------------------------------------------
問題／新規作成ページ
----------------------------------------------------------------------
"""
def create(request):
    return render(request, 'question/create.html')

"""
----------------------------------------------------------------------
問題／新規作成処理
----------------------------------------------------------------------
"""
def run_create(request):
    # 問題管理ページへ
    return HttpResponseRedirect(reverse('question:manage', args=(1,)))

"""
----------------------------------------------------------------------
問題／編集ページ
----------------------------------------------------------------------
"""
def edit(request, question_id):
    return render(request, 'question/edit.html', {
        'question_id': question_id,
    })

"""
----------------------------------------------------------------------
問題／編集処理
----------------------------------------------------------------------
"""
def run_edit(request, question_id):
    # 問題管理ページへ
    return HttpResponseRedirect(reverse('question:manage'))