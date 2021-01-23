from django.shortcuts import render
from django.urls      import reverse
from django.http      import HttpResponse, HttpResponseRedirect

"""
----------------------------------------------------------------------
ブックマーク／一覧表示
----------------------------------------------------------------------
"""
def index(request, user_id):
    return render(request, 'bookmark/index.html', {
        'user_id': user_id,
    })

"""
----------------------------------------------------------------------
ブックマーク／ブックマーク処理
----------------------------------------------------------------------
"""
def run_bookmark(request, user_id, question_id):

    # 前のページにリダイレクト
    return HttpResponseRedirect(request.META.get("HTTP_REFERER"))

"""
----------------------------------------------------------------------
ブックマーク／ブックマーク解除
----------------------------------------------------------------------
"""
def release(request, user_id, question_id):

    # 前のページにリダイレクト
    return HttpResponseRedirect(request.META.get("HTTP_REFERER"))