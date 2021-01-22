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
def run_login(request, user_id):
    return HttpResponse("login user_id:" + str(user_id))

"""
----------------------------------------------------------------------
ユーザー／ログアウト処理
----------------------------------------------------------------------
"""
def run_logout(request, user_id):
    return HttpResponse("logout user_id:" + str(user_id))

"""
----------------------------------------------------------------------
ユーザー／退会ページ
----------------------------------------------------------------------
"""
def withdrawal(request, user_id):
    return HttpResponse("withdrawal user_id:" + str(user_id))

"""
----------------------------------------------------------------------
ユーザー／退会処理
----------------------------------------------------------------------
"""
def run_withdrawal(request, user_id):
    return HttpResponse("run_withdrawal user_id:" + str(user_id))

"""
----------------------------------------------------------------------
ユーザー／プロフィール詳細ページ
----------------------------------------------------------------------
"""
def detail(request, user_id):
    return HttpResponse(str(user_id) + "'s detail")

"""
----------------------------------------------------------------------
ユーザー／プロフィール新規作成ページ
----------------------------------------------------------------------
"""
def create(request):
    return HttpResponse("'create user page")

"""
----------------------------------------------------------------------
ユーザー／プロフィール新規作成処理
----------------------------------------------------------------------
"""
def run_create(request):
    return HttpResponse("create user")

"""
----------------------------------------------------------------------
ユーザー／プロフィール編集ページ
----------------------------------------------------------------------
"""
def edit(request, user_id):
    return HttpResponse(str(user_id) + "'s edit page")

"""
----------------------------------------------------------------------
ユーザー／プロフィール編集処理
----------------------------------------------------------------------
"""
def run_edit(request, user_id):
    return HttpResponse("edit user_id:" + str(user_id))

"""
----------------------------------------------------------------------
ユーザー／ユーザー一覧ページ
----------------------------------------------------------------------
"""
def index(request):
    return HttpResponse("user list.")