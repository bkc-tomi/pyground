from django.shortcuts import render
from django.urls      import reverse
from django.http      import HttpResponse, HttpResponseRedirect

"""
----------------------------------------------------------------------
フレンド／フォロー一覧
----------------------------------------------------------------------
"""
def follow(request, user_id):
    return render(request, 'friend/follow.html', {
        'user_id': user_id,
    })

"""
----------------------------------------------------------------------
フレンド／フォロワー一覧
----------------------------------------------------------------------
"""
def follower(request, user_id):
    return render(request, 'friend/follower.html', {
        'user_id': user_id,
    })

"""
----------------------------------------------------------------------
フレンド／フォロー処理
----------------------------------------------------------------------
"""
def run_follow(request, user_id, follow_user_id):
    # 前のページにリダイレクト
    return HttpResponseRedirect(request.META.get("HTTP_REFERER"))

"""
----------------------------------------------------------------------
フレンド／フォロー解除処理
----------------------------------------------------------------------
"""
def release(request, user_id, follow_id):
    # 前のページにリダイレクト
    return HttpResponseRedirect(request.META.get("HTTP_REFERER"))

"""
----------------------------------------------------------------------
フレンド／フォロー許可ページ
----------------------------------------------------------------------
"""
def permit(request, user_id):
    return render(request, 'friend/permit.html', {
        'user_id': user_id,
    })

"""
----------------------------------------------------------------------
フレンド／フォロー許可処理
----------------------------------------------------------------------
"""
def run_permit(request, user_id, follow_id):
    # 前のページにリダイレクト
    return HttpResponseRedirect(request.META.get("HTTP_REFERER"))

"""
----------------------------------------------------------------------
フレンド／フォロー不許可処理
----------------------------------------------------------------------
"""
def run_nopermit(request, user_id, follow_id):
    # 前のページにリダイレクト
    return HttpResponseRedirect(request.META.get("HTTP_REFERER"))



