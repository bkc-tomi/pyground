from django.shortcuts import render
from django.http import HttpResponse

"""
----------------------------------------------------------------------
ブックマーク／一覧表示
----------------------------------------------------------------------
"""
def index(request, user_id):
    return HttpResponse(str(user_id) + "'s bookmark list.")

"""
----------------------------------------------------------------------
ブックマーク／ブックマーク処理
----------------------------------------------------------------------
"""
def run_bookmark(request, user_id, question_id):
    return HttpResponse(str(user_id) + " is bookmark question_id: " + str(question_id))

"""
----------------------------------------------------------------------
ブックマーク／ブックマーク解除
----------------------------------------------------------------------
"""
def release(request, user_id, question_id):
    return HttpResponse(str(user_id) + " is release question_id: " + str(question_id))