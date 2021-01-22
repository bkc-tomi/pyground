from django.shortcuts import render
from django.http import HttpResponse

"""
----------------------------------------------------------------------
フレンド／フォロー一覧
----------------------------------------------------------------------
"""
def follow(request, user_id):
    return HttpResponse(str(user_id) + "'s follow list.")

"""
----------------------------------------------------------------------
フレンド／フォロー処理
----------------------------------------------------------------------
"""
def run_follow(request, user_id, follow_user_id):
    return HttpResponse(str(user_id) + "is following user_id:" + str(follow_user_id))

"""
----------------------------------------------------------------------
フレンド／フォロー解除処理
----------------------------------------------------------------------
"""
def release(request, user_id, follow_id):
    return HttpResponse(str(user_id) + "is release " + str(follow_id))

"""
----------------------------------------------------------------------
フレンド／フォロワー一覧
----------------------------------------------------------------------
"""
def follower(request, user_id):
    return HttpResponse(str(user_id) + "'s follower list.")

"""
----------------------------------------------------------------------
フレンド／フォロー許可ページ
----------------------------------------------------------------------
"""
def permit(request, user_id):
    return HttpResponse(str(user_id) + "'s permit list.")

"""
----------------------------------------------------------------------
フレンド／フォロー許可処理
----------------------------------------------------------------------
"""
def run_permit(request, user_id, follow_id):
    return HttpResponse(str(user_id) + "is permit follow_id:" + str(follow_id))

"""
----------------------------------------------------------------------
フレンド／フォロー不許可処理
----------------------------------------------------------------------
"""
def run_nopermit(request, user_id, follow_id):
    return HttpResponse(str(user_id) + "is not permit follow_id:" + str(follow_id))



