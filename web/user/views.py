import logging

from django.shortcuts import render
from django.urls      import reverse
from django.http      import HttpResponse, HttpResponseRedirect, Http404

# モデル
from .models           import User, Profile
from playground.models import Code
from friend.models     import Follow, Permit

def register(request):
    """
    ----------------------------------------------------------------------
    ユーザー／登録ページ
    ----------------------------------------------------------------------
    """
    # -------------------------------------------------------
    # セッション
    # -------------------------------------------------------
    # ログイン状態なら別ページへ遷移
    if 'login_user' in request.session:
        user = request.session['login_user']
        return HttpResponseRedirect(
            reverse('user:detail', args=(user['id'], ))
        )

    # -------------------------------------------------------
    # ページ遷移
    # -------------------------------------------------------
    return render(request, "user/register.html")

def register_complete(request):
    """
    ----------------------------------------------------------------------
    ユーザー／登録完了ページ
    ----------------------------------------------------------------------
    """
    # -------------------------------------------------------
    # セッション
    # -------------------------------------------------------
    if 'login_user' not in request.session:
        return HttpResponseRedirect(reverse('top:top'))
    
    login_user = request.session['login_user']

    # -------------------------------------------------------
    # ページ遷移
    # -------------------------------------------------------
    return render(request, "user/register_complete.html")

def run_register(request):
    """
    ----------------------------------------------------------------------
    ユーザー／登録処理
    ----------------------------------------------------------------------
    """
    # -------------------------------------------------------
    # 初期値・値取得
    # -------------------------------------------------------
    # 初期化 ------------------------------------------
    login_user = {
        'id'      : '',
        'username': '',
    }
    # 入力値取得 ---------------------------------------
    post_dict = {
        'username': request.POST['username'],
        'email'   : request.POST['email'],
        'password': request.POST['password'],
        'check'   : request.POST['check'],
    }

    # -------------------------------------------------------
    # バリデーション
    # -------------------------------------------------------
    # 未入力 -------------------------------------------
    empty_list = ''
    for key, value in post_dict.items():
        if value == '':
            empty_list += ', ' + str(key)
        
    if empty_list != '':
        print('未入力項目:' + str(empty_list))
        return HttpResponseRedirect(reverse('user:register'))

    # passwordのチェック --------------------------------
    if post_dict['password'] != post_dict['check']:
        print('パスワードと確認用が異なります。')
        return HttpResponseRedirect(reverse('user:register'))

    # -------------------------------------------------------
    # データベース保存
    # -------------------------------------------------------
    # DB処理 --------------------------------------
    try:
        user = User(
            username = post_dict['username'],
            email    = post_dict['email'],
            password = post_dict['password'],
        )
        user.save()

    except:
        print('データベース登録エラー')
        return HttpResponseRedirect(reverse('user:register'))

    # -------------------------------------------------------
    # 後処理
    # -------------------------------------------------------
    # ユーザーデータ作成 ---------------------------------
    login_user['id']       = user.id
    login_user['username'] = user.username

    # -------------------------------------------------------
    # ページ遷移
    # -------------------------------------------------------
    # セッション保持
    request.session['login_user'] = login_user
    # ページ遷移
    return HttpResponseRedirect(reverse('user:register_complete'))

def login(request):
    """
    ----------------------------------------------------------------------
    ユーザー／ログインページ
    ----------------------------------------------------------------------
    """
    # -------------------------------------------------------
    # セッション
    # -------------------------------------------------------
    # ログイン状態なら別ページへ遷移
    if 'login_user' in request.session:
        user = request.session['login_user']
        return HttpResponseRedirect(
            reverse('user:detail', args=(user['id'], ))
        )

    # -------------------------------------------------------
    # ページ遷移
    # -------------------------------------------------------
    return render(request, "user/login.html")

def run_login(request):
    """
    ----------------------------------------------------------------------
    ユーザー／ログイン処理
    ----------------------------------------------------------------------
    """
    # -------------------------------------------------------
    # 初期値・値取得
    # -------------------------------------------------------

    # 入力値取得 -----------------------------------
    post_dict = {
        'email'   : request.POST['email'],
        'password': request.POST['password'],
    }

    # -------------------------------------------------------
    # バリデーション
    # -------------------------------------------------------
    # 未入力 ---------------------------------------
    empty_list = ''
    for key, value in post_dict.items():
        if value == '':
            empty_list += ', ' + str(key)
        
    if empty_list != '':
        print('未入力項目:' + str(empty_list))
        return HttpResponseRedirect(reverse('user:login'))

    # -------------------------------------------------------
    # 前処理
    # -------------------------------------------------------
    # データ取得 ------------------------------------
    try:
        user_list = User.objects.filter(
            email = post_dict['email'],
            password = post_dict['password']
        )
    except:
        return HttpResponseRedirect(reverse('user:login'))

    # -------------------------------------------------------
    # 後処理
    # -------------------------------------------------------
    login_user = {}
    # ユーザーデータ作成 ------------------------------
    if user_list:
        login_user['id']       = user_list[0].id
        login_user['username'] = user_list[0].username

    # -------------------------------------------------------
    # ページ遷移
    # -------------------------------------------------------
    if login_user:
        # ログイン成功 --------------------------------
        request.session['login_user'] = login_user
        return HttpResponseRedirect(
            reverse('user:detail', args=(login_user['id'],))
        )
    else:
        # ログイン失敗 --------------------------------
        return HttpResponseRedirect(reverse('user:login'))
    
def run_logout(request, user_id):
    """
    ----------------------------------------------------------------------
    ユーザー／ログアウト処理
    ----------------------------------------------------------------------
    """
    # -------------------------------------------------------
    # セッション
    # -------------------------------------------------------
    if 'login_user' not in request.session:
        return HttpResponseRedirect(reverse('top:top'))
    
    login_user = request.session['login_user']

    # -------------------------------------------------------
    # 後処理
    # -------------------------------------------------------
    # ログアウト処理
    try:
        del request.session['login_user']
    except KeyError:
        pass

    # -------------------------------------------------------
    # ページ遷移
    # -------------------------------------------------------
    return HttpResponseRedirect(reverse('top:top'))

def withdrawal(request):
    """
    ----------------------------------------------------------------------
    ユーザー／退会ページ
    ----------------------------------------------------------------------
    """
    # -------------------------------------------------------
    # セッション
    # -------------------------------------------------------
    if 'login_user' not in request.session:
        return HttpResponseRedirect(reverse('top:top'))
    
    login_user = request.session['login_user']

    # -------------------------------------------------------
    # ページ遷移
    # -------------------------------------------------------
    return render(request, "user/withdrawal.html")

def run_withdrawal(request):
    """
    ----------------------------------------------------------------------
    ユーザー／退会処理
    ----------------------------------------------------------------------
    """
    # -------------------------------------------------------
    # セッション
    # -------------------------------------------------------
    if 'login_user' not in request.session:
        return HttpResponseRedirect(reverse('top:top'))
    
    login_user = request.session['login_user']

    # -------------------------------------------------------
    # ページ遷移
    # -------------------------------------------------------
    # 退会処理 ----------------------------------------
    try:
        # ユーザーをDBから削除
        user = User.objects.get(pk=login_user['id'])
        user.delete()
        # ユーザーをセッションから削除
        del request.session['login_user']
        return HttpResponseRedirect(reverse('top:top'))
    except:
        print('ユーザーの削除に失敗')
        return render(request, "user/withdrawal.html")

def detail(request, user_id):
    """
    ----------------------------------------------------------------------
    ユーザー／プロフィール詳細ページ
    ----------------------------------------------------------------------
    """
    # -------------------------------------------------------
    # セッション
    # -------------------------------------------------------
    if 'login_user' not in request.session:
        return HttpResponseRedirect(reverse('top:top'))
    
    login_user = request.session['login_user']

    # -------------------------------------------------------
    # 初期値・値取得
    # -------------------------------------------------------
    # 初期値 ---------------------------------------
    profile = {
        'id'          : '',
        'image_icon'  : {},
        'username'    : '',
        'email'       : '',
        'password'    : '',
        'profile_text': '',
        'publish'     : '',
    }
    follow_num   = 0
    follower_num = 0
    follow_id    = False
    is_me        = False
    is_permit    = False
    codes        = {}

    # -------------------------------------------------------
    # 描画データ取得
    # -------------------------------------------------------
    # ユーザーの取得 ----------------------------------
    temp = ''
    try:
        temp = User.objects.get(pk=user_id)

    except User.DoesNotExist:
        raise Http404("User does not exist")

    profile['id']         = temp.id
    profile['username']   = temp.username
    profile['email']      = temp.email
    profile['image_icon'] = temp.image_icon
    

    # プロフィールの取得 --------------------------------
    temp = ''
    try:
        temp = Profile.objects.filter(target_user_id=user_id)[0:1]

    except Profile.DoesNotExist:
        raise Http404("Profile does not exist")
    
    if len(temp) > 0:
        temp2 = temp[0]
        profile['profile_text'] = temp2.profile_text
        profile['publish']      = temp2.publish

    # コードの取得 ------------------------------------
    try:
        codes = Code.objects.filter(target_user_id=user_id)

    except Code.DoesNotExist:
        raise Http404("Code does not exist")

    # フォロー数の取得 ---------------------------------
    try:
        follow_num = Follow.objects.filter(follow_user_id=user_id).count()

    except Code.DoesNotExist:
        raise Http404("Follow does not exist")
    
    # フォロワー数の取得 -------------------------------
    try:
        follower_num = Follow.objects.filter(followed_user_id=user_id).count()

    except Code.DoesNotExist:
        raise Http404("Follow does not exist")

    # フォローしているかどうかの判定 ---------------------
    temp = ''
    try:
        temp = Follow.objects.filter(follow_user_id=login_user['id'], followed_user_id=user_id)

    except Code.DoesNotExist:
        raise Http404("Follow does not exist")
    
    if len(temp) == 1:
        follow_id = temp[0].id

    # ログインユーザーの判定 ----------------------------
    if profile['id'] == login_user['id']:
        is_me = True

    # 申請中の判定 ------------------------------------
    try:
        permit = Permit.objects.filter(target_user_id=user_id)
        if permit:
            is_permit = True

    except Exception as e:
        print('申請中の判定err:' + str(e))
        return render(request, "user/index.html")

    # -------------------------------------------------------
    # ページ遷移
    # -------------------------------------------------------
    return render(request, "user/detail.html", {
        'profile'     : profile,
        'codes'       : codes,
        'follow_num'  : follow_num,
        'follower_num': follower_num,
        'follow_id'   : follow_id,
        'is_me'       : is_me,
        'is_permit'   : is_permit,
    })

def create(request):
    """
    ----------------------------------------------------------------------
    ユーザー／プロフィール新規作成ページ
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
    # ユーザーID取得 ---------------------------------
    target_user_id = login_user['id']

    # -------------------------------------------------------
    # ページ遷移
    # -------------------------------------------------------
    return render(request, "user/create.html", {
        'target_user_id': target_user_id,
    })

def run_create(request):
    """
    ----------------------------------------------------------------------
    ユーザー／プロフィール新規作成処理
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

    # DB処理
    if request.POST['id']:
        try:
            user = User(
                id=request.POST['id'],
                image_icon=request.FILES['image_icon'],
            )
            user.save()
        except Exception as e:
            print('userデータベース登録エラー')
            print('type:' + str(type(e)))
            print('args:' + str(e.args))
            # print('message:' + e.message)
            print('e自身:' + str(e))
            return HttpResponseRedirect(reverse('user:create'))

    # プロフィール ----------------------------------------
    # 情報保管
    temp_pub = False
    if request.POST['publish'] == 'on':
        temp_pub = True

    # DB処理
    try:
        profile = Profile(
            profile_text   = request.POST['profile'],
            publish        = temp_pub,
            target_user_id = request.POST['id'],
        )
        profile.save()

    except Exception as e:
            print('profileデータベース登録エラー')
            print('type:' + str(type(e)))
            print('args:' + str(e.args))
            # print('message:' + e.message)
            print('e自身:' + str(e))
            return HttpResponseRedirect(reverse('user:create'))

    # -------------------------------------------------------
    # 後処理
    # -------------------------------------------------------
    # ユーザーID取得
    user_id = login_user['id']

    # -------------------------------------------------------
    # ページ遷移
    # -------------------------------------------------------
    return HttpResponseRedirect(reverse('user:detail', args=(user_id,)))

def edit(request, user_id):
    """
    ----------------------------------------------------------------------
    ユーザー／プロフィール編集ページ
    ----------------------------------------------------------------------
    """
    # -------------------------------------------------------
    # セッション
    # -------------------------------------------------------
    if 'login_user' not in request.session:
        return HttpResponseRedirect(reverse('top:top'))
    
    login_user = request.session['login_user']

    # -------------------------------------------------------
    # 初期値・値取得
    # -------------------------------------------------------
    disp_profile = {
        'id'          : '',
        'image_icon'  : {},
        'username'    : '',
        'password'    : '',
        'profile_text': '',
        'publish'     : '',
    }

    # -------------------------------------------------------
    # 描画データ取得
    # -------------------------------------------------------
    
    # ユーザーの取得 ---------------------------------
    try:
        temp = User.objects.get(pk=user_id)

    except User.DoesNotExist:
        raise Http404("User does not exist")

    disp_profile['id']         = temp.id
    disp_profile['username']   = temp.username
    disp_profile['password']   = temp.password
    disp_profile['image_icon'] = temp.image_icon
    

    # プロフィールの取得 -------------------------------
    try:
        temp = Profile.objects.filter(target_user_id=user_id)[0:1]

    except User.DoesNotExist:
        raise Http404("User does not exist")
    
    if len(temp) > 0:
        temp2 = temp[0]
        disp_profile['profile_text'] = temp2.profile_text
        disp_profile['publish']      = temp2.publish

    # -------------------------------------------------------
    # ページ遷移
    # -------------------------------------------------------
    return render(request, "user/edit.html", {
        'profile': disp_profile,
    })

def run_edit(request, user_id):
    """
    ----------------------------------------------------------------------
    ユーザー／プロフィール編集処理
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
    # ユーザー -------------------------------------------
    # DB処理
    if request.POST['id']:
        try:
            # 対象レコード取得
            user = User.objects.get(pk=request.POST['id'])
            if 'image_icon' in request.FILES:
                if request.FILES['image_icon'] != '':
                    user.image_icon = request.FILES['image_icon']
            user.username = request.POST['username']
            user.password = request.POST['password']

            # 更新
            user.save()

        except Exception as e:
            print('userデータベース登録エラー')
            print('type:' + str(type(e)))
            print('args:' + str(e.args))
            # print('message:' + e.message)
            print('e自身:' + str(e))
            return HttpResponseRedirect(
                reverse('user:edit', args=(login_user['id'],)),
            )

    # プロフィール ----------------------------------------
    # DB処理
    try:
        # 情報保管
        print(request.POST)
        temp_pub = False
        if request.POST['publish'] == 'on':
            temp_pub = True

        # 対象レコード取得
        profile = Profile.objects.get(target_user_id=request.POST['id'])
        profile.profile_text = request.POST['profile']
        profile.publish      = temp_pub

        # 更新
        profile.save()

    except Exception as e:
            print('profileデータベース登録エラー')
            print('type:' + str(type(e)))
            print('args:' + str(e.args))
            # print('message:' + e.message)
            print('e自身:' + str(e))
            return HttpResponseRedirect(
                reverse('user:edit', args=(login_user['id'],)),
            )

    # -------------------------------------------------------
    # ページ遷移
    # -------------------------------------------------------
    return HttpResponseRedirect(reverse('user:detail', args=(user_id,)))

def index(request):
    """
    ----------------------------------------------------------------------
    ユーザー／ユーザー一覧ページ
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
    user_list = User.objects.all()
    print(user_list)

    # -------------------------------------------------------
    # ページ遷移
    # -------------------------------------------------------
    return render(request, "user/index.html", {
        'user_list': user_list,
    })