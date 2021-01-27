from django.shortcuts import render
from django.urls      import reverse
from django.http      import HttpResponse, HttpResponseRedirect

# モデル
from .models     import Follow, Permit
from user.models import User, Profile


def follow(request, user_id):
    """
    ----------------------------------------------------------------------
    フレンド／フォロー一覧
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
    # ユーザーID取得
    user_id = login_user['id']

    # フォロー情報取得 ----------------------------------
    temps = Follow.objects.filter(follow_user_id=user_id)

    # 描画オブジェクトの作成 -----------------------------
    follow_list = []
    for temp in temps:
        user = User.objects.get(pk=temp.followed_user_id)
        follow = {
            'id'  : temp.id,
            'user': user,
        }
        follow_list.append(follow)
    
    # -------------------------------------------------------
    # ページ遷移
    # -------------------------------------------------------
    return render(request, 'friend/follow.html', {
        'user_id'    : user_id,
        'follow_list': follow_list,
    })

def follower(request, user_id):
    """
    ----------------------------------------------------------------------
    フレンド／フォロワー一覧
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
    # ユーザーID取得
    user_id = login_user['id']

    # フォロー情報取得 ----------------------------------
    temp = Follow.objects.filter(followed_user_id=user_id)

    # 描画オブジェクトの作成 -----------------------------
    follower_list = []
    for follow in temp:
        user = User.objects.get(pk=follow.follow_user_id)
        follower = {
            'user': user,
            'follower': follow,
        }
        
        follower_list.append(follower)

    # -------------------------------------------------------
    # ページ遷移
    # -------------------------------------------------------
    return render(request, 'friend/follower.html', {
        'user_id'      : user_id,
        'follower_list': follower_list,
    })

def run_follow(request, follow_user_id):
    """
    ----------------------------------------------------------------------
    フレンド／フォロー処理
    ----------------------------------------------------------------------
    """
    # -------------------------------------------------------
    # セッション
    # -------------------------------------------------------
    if 'login_user' not in request.session:
        return HttpResponseRedirect(reverse('top:top'))
    
    login_user = request.session['login_user']

    # -------------------------------------------------------
    # データベース処理
    # -------------------------------------------------------
    # 各種ID取得 --------------------------------------
    # フォローユーザー
    follow_user = login_user['id']

    # フォローされたユーザー
    followed_user = follow_user_id

    # DB登録 -----------------------------------------
    try:
        user_prof = Profile.objects.get(target_user_id=follow_user_id)

        if user_prof.publish:
            # 公開の場合 ------------------------------
            follow = Follow(
                follow_user_id   = follow_user,
                followed_user_id = followed_user,
            )
            follow.save()
        else:
            # 非公開の場合 ----------------------------
            permit = Permit(
                request_user_id = follow_user,
                target_user_id  = followed_user,
            )
            permit.save()

    except Exception as e:
        print('err:' + str(e))

    # -------------------------------------------------------
    # ページ遷移
    # -------------------------------------------------------
    # 前のページにリダイレクト
    return HttpResponseRedirect(request.META.get("HTTP_REFERER"))

def release(request, follow_id):
    """
    ----------------------------------------------------------------------
    フレンド／フォロー解除処理
    ----------------------------------------------------------------------
    """
    # -------------------------------------------------------
    # セッション
    # -------------------------------------------------------
    if 'login_user' not in request.session:
        return HttpResponseRedirect(reverse('top:top'))
    
    login_user = request.session['login_user']

    # -------------------------------------------------------
    # データベース処理
    # -------------------------------------------------------
    # DB削除 ------------------------------------------
    try:
        follow = Follow.objects.get(pk=follow_id)
        follow.delete()

    except Exception as e:
        print('err:' + str(e))
        # 前のページにリダイレクト
    return HttpResponseRedirect(request.META.get("HTTP_REFERER"))

    # -------------------------------------------------------
    # ページ遷移
    # -------------------------------------------------------
    # 前のページにリダイレクト
    return HttpResponseRedirect(request.META.get("HTTP_REFERER"))

def permit(request, user_id):
    """
    ----------------------------------------------------------------------
    フレンド／フォロー許可ページ
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
    # ユーザーID取得
    user_id = login_user['id']

    # 申請一覧 ----------------------------------------
    # フォロー情報取得
    temps = Permit.objects.filter(target_user_id=user_id)

    # 描画オブジェクトの作成
    permit_list = []
    for temp in temps:
        user = User.objects.get(pk=temp.request_user_id)
        permit = {
            'id'  : temp.id,
            'user': user,
        }
        permit_list.append(permit)

    # 被申請一覧 ---------------------------------------
    # フォロー情報取得
    temps = Permit.objects.filter(request_user_id=user_id)

    # 描画オブジェクトの作成
    permited_list = []
    for temp in temps:
        user = User.objects.get(pk=temp.target_user_id)
        permit = {
            'id'  : temp.id,
            'user': user,
        }
        permited_list.append(permit)

    # -------------------------------------------------------
    # ページ遷移
    # -------------------------------------------------------
    return render(request, 'friend/permit.html', {
        'user_id'      : user_id,
        'permit_list'  : permit_list,
        'permited_list': permited_list,
    })

def run_permit(request, permit_id):
    """
    ----------------------------------------------------------------------
    フレンド／フォロー許可処理
    ----------------------------------------------------------------------
    """
    # -------------------------------------------------------
    # セッション
    # -------------------------------------------------------
    if 'login_user' not in request.session:
        return HttpResponseRedirect(reverse('top:top'))
    
    login_user = request.session['login_user']

    # -------------------------------------------------------
    # データベース処理
    # -------------------------------------------------------
    # 申請許可処理 -------------------------------------
    try:
        # 申請情報取得
        permit = Permit.objects.get(pk=permit_id)

        # DB更新
        follow = Follow(
            follow_user_id   = permit.request_user_id,
            followed_user_id = permit.target_user_id,
        )
        follow.save()

        # 申請情報の削除
        permit.delete()

    except Exception as e:
        print('err:' + str(e))
        # 前のページにリダイレクト
        user_id = login_user['id']
        return HttpResponseRedirect(
            reverse('friend:permit', args=(user_id,))
        )

    # -------------------------------------------------------
    # ページ遷移
    # -------------------------------------------------------
    # 前のページにリダイレクト
    return HttpResponseRedirect(request.META.get("HTTP_REFERER"))

def run_nopermit(request, permit_id):
    """
    ----------------------------------------------------------------------
    フレンド／フォロー不許可処理
    ----------------------------------------------------------------------
    """
    # -------------------------------------------------------
    # セッション
    # -------------------------------------------------------
    if 'login_user' not in request.session:
        return HttpResponseRedirect(reverse('top:top'))
    
    login_user = request.session['login_user']

    # -------------------------------------------------------
    # データベース処理
    # -------------------------------------------------------
    # 申請許可処理 -------------------------------------
    try:
        # 申請情報取得
        permit = Permit.objects.get(pk=permit_id)
        permit.delete()

    except Exception as e:
        print('err:' + str(e))
        # 前のページにリダイレクト
        user_id = login_user['id']
        return HttpResponseRedirect(
            reverse('friend:permit', args=(user_id,))
        )

    # -------------------------------------------------------
    # ページ遷移
    # -------------------------------------------------------
    # 前のページにリダイレクト
    return HttpResponseRedirect(request.META.get("HTTP_REFERER"))



