from django.shortcuts import render
from django.http import HttpResponse

"""
----------------------------------------------------------------------
ユーザー／登録ページ
----------------------------------------------------------------------
"""
def register(request):
    return HttpResponse("register page")

"""
----------------------------------------------------------------------
ユーザー／登録完了ページ
----------------------------------------------------------------------
"""
def register_complete(request):
    return HttpResponse("register_complete page")

"""
----------------------------------------------------------------------
ユーザー／登録処理
----------------------------------------------------------------------
"""
def run_register(request):
    return HttpResponse("run_register page")

"""
----------------------------------------------------------------------
ユーザー／ログインページ
----------------------------------------------------------------------
"""
def login(request):
    return HttpResponse("login page")

"""
----------------------------------------------------------------------
ユーザー／ログイン処理
----------------------------------------------------------------------
"""
def run_login(request):
    return HttpResponse("run_login page")

"""
----------------------------------------------------------------------
ユーザー／ログアウト処理
----------------------------------------------------------------------
"""
def run_logout(request):
    return HttpResponse("run_logout page")

"""
----------------------------------------------------------------------
ユーザー／退会ページ
----------------------------------------------------------------------
"""
def withdrawal(request):
    return HttpResponse("withdrawal page")

"""
----------------------------------------------------------------------
ユーザー／退会処理
----------------------------------------------------------------------
"""
def run_withdrawal(request):
    return HttpResponse("run_withdrawal page")

"""
----------------------------------------------------------------------
ユーザー／プロフィール詳細ページ
----------------------------------------------------------------------
"""
def detail(request):
    return HttpResponse("detail page")

"""
----------------------------------------------------------------------
ユーザー／プロフィール編集・新規作成ページ
----------------------------------------------------------------------
"""
def edit(request):
    return HttpResponse("edit page")

"""
----------------------------------------------------------------------
ユーザー／プロフィール編集・新規作成処理
----------------------------------------------------------------------
"""
def run_edit(request):
    return HttpResponse("run_edit page")

"""
----------------------------------------------------------------------
ユーザー／ユーザー一覧ページ
----------------------------------------------------------------------
"""
def index(request):
    return HttpResponse("index page")