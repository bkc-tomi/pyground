import logging
import uuid

from django.shortcuts import render
from django.urls      import reverse
from django.http      import HttpResponse, HttpResponseRedirect, Http404
from django.core.mail import BadHeaderError, send_mail

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
    try:
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
        # 描画データ作成
        # -------------------------------------------------------
        message = ''
        if 'message' in request.session:
            message = request.session['message']
            del request.session['message']

        # -------------------------------------------------------
        # ページ遷移
        # -------------------------------------------------------
        return render(request, "user/register.html", {
            'message': message,
        })

    # -------------------------------------------------------
    # エラー処理
    # -------------------------------------------------------
    except Exception as e:
        errors = {
            'type': str(type(e)),
            'args': str(e.args),
            'err' : str(e),
            'msg' : '',
        }
        request.session['errors'] = errors
        return HttpResponseRedirect(reverse('errors:errors'))

def register_complete(request, token):
    """
    ----------------------------------------------------------------------
    ユーザー／登録完了ページ
    ----------------------------------------------------------------------
    """
    try:
        # -------------------------------------------------------
        # ユーザー取得
        # -------------------------------------------------------
        user = User.objects.get(token=token)

        # -------------------------------------------------------
        # セッション登録
        # -------------------------------------------------------
        login_user = {
            'id'      : user.id,
            'username': user.username,
        }

        request.session['login_user'] = login_user

        # -------------------------------------------------------
        # トークン削除
        # -------------------------------------------------------
        user.token = ''
        user.save()
        
        # -------------------------------------------------------
        # ページ遷移
        # -------------------------------------------------------
        return render(request, "user/register_complete.html")

    # -------------------------------------------------------
    # エラー処理
    # -------------------------------------------------------
    except User.DoesNotExist as e:
        errors = {
            'type': str(type(e)),
            'args': str(e.args),
            'err' : str(e),
            'msg' : 'このユーザーはすでに本登録が済んでいます。',
        }
        request.session['errors'] = errors
        return HttpResponseRedirect(reverse('errors:errors'))

    except Exception as e:
        errors = {
            'type': str(type(e)),
            'args': str(e.args),
            'err' : str(e),
            'msg' : '',
        }
        request.session['errors'] = errors
        return HttpResponseRedirect(reverse('errors:errors'))

def run_register(request):
    """
    ----------------------------------------------------------------------
    ユーザー／登録処理
    ----------------------------------------------------------------------
    """
    try:
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
        # 本登録用トークン作成 --------------------------
        token = str(uuid.uuid4())

        # -------------------------------------------------------
        # バリデーション
        # -------------------------------------------------------
        # 未入力 -------------------------------------------
        empty_list = ''
        for key, value in post_dict.items():
            if value == '':
                empty_list += ', ' + str(key)
            
        if empty_list != '':
            request.session['message'] = '未入力項目:' + str(empty_list)
            return HttpResponseRedirect(reverse('user:register'))

        # passwordのチェック --------------------------------
        if post_dict['password'] != post_dict['check']:
            request.session['message'] = 'パスワードとパスワード(確認)が異なります。'
            return HttpResponseRedirect(reverse('user:register'))

        # -------------------------------------------------------
        # データベース保存
        # -------------------------------------------------------

        # DB処理 --------------------------------------
        user = User(
            username = post_dict['username'],
            email    = post_dict['email'],
            password = post_dict['password'],
            token    = token,
        )
        user.save()


        # -------------------------------------------------------
        # 後処理
        # -------------------------------------------------------
        # メールの送信 --------------------------------------
        # メール文章作成
        """題名"""
        subject = "仮登録完了"
        """本文"""
        message = f"""\
仮登録が完了しました。以下のリンクにアクセスして本登録をお願いします。
http://localhost:8000/user/register/complete/{ token }/
        """
        """送信元メールアドレス"""
        from_email = "information@myproject"
        """宛先メールアドレス"""
        recipient_list = [
            "apptest@apptest.com"
        ]

        # メール送信
        send_mail(subject, message, from_email, recipient_list)

        # -------------------------------------------------------
        # ページ遷移
        # -------------------------------------------------------
        # メッセージの追加
        request.session['message'] = "仮登録が完了しました。"

        # ページ遷移
        return HttpResponseRedirect(reverse('user:register'))

    # -------------------------------------------------------
    # エラー処理
    # -------------------------------------------------------
    except Exception as e:
        errors = {
            'type': str(type(e)),
            'args': str(e.args),
            'err' : str(e),
            'msg' : '',
        }
        request.session['errors'] = errors
        return HttpResponseRedirect(reverse('errors:errors'))

def login(request):
    """
    ----------------------------------------------------------------------
    ユーザー／ログインページ
    ----------------------------------------------------------------------
    """
    try:
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
        # 描画データ作成
        # -------------------------------------------------------
        message = ''
        if 'message' in request.session:
            message = request.session['message']
            del request.session['message']

        # -------------------------------------------------------
        # ページ遷移
        # -------------------------------------------------------
        return render(request, "user/login.html", {
            'message': message,
        })

    # -------------------------------------------------------
    # エラー処理
    # -------------------------------------------------------
    except Exception as e:
        errors = {
            'type': str(type(e)),
            'args': str(e.args),
            'err' : str(e),
            'msg' : '',
        }
        request.session['errors'] = errors
        return HttpResponseRedirect(reverse('errors:errors'))

def run_login(request):
    """
    ----------------------------------------------------------------------
    ユーザー／ログイン処理
    ----------------------------------------------------------------------
    """
    try:
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
            request.session['message'] = '未入力項目:' + str(empty_list)
            return HttpResponseRedirect(reverse('user:login'))

        # -------------------------------------------------------
        # 前処理
        # -------------------------------------------------------
        # データ取得 ------------------------------------
        user_list = User.objects.filter(
            email    = post_dict['email'],
            password = post_dict['password']
        )
        

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
            request.session['message'] = 'ログインに失敗しました。メールアドレス・パスワードをお確かめください。'
            return HttpResponseRedirect(reverse('user:login'))

    # -------------------------------------------------------
    # エラー処理
    # -------------------------------------------------------
    # 該当ユーザーが見つからない時
    except User.DoesNotExist:
        request.session['message'] = 'ログインに失敗しました。メールアドレス・パスワードをお確かめください。'
        return HttpResponseRedirect(reverse('user:login'))
    
    # その他エラー
    except Exception as e:
        errors = {
            'type': str(type(e)),
            'args': str(e.args),
            'err' : str(e),
            'msg' : '',
        }
        request.session['errors'] = errors
        return HttpResponseRedirect(reverse('errors:errors'))
    
def run_logout(request, user_id):
    """
    ----------------------------------------------------------------------
    ユーザー／ログアウト処理
    ----------------------------------------------------------------------
    """
    try:
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
        del request.session['login_user']

        # -------------------------------------------------------
        # ページ遷移
        # -------------------------------------------------------
        return HttpResponseRedirect(reverse('top:top'))

    # -------------------------------------------------------
    # エラー処理
    # -------------------------------------------------------
    except Exception as e:
        errors = {
            'type': str(type(e)),
            'args': str(e.args),
            'err' : str(e),
            'msg' : '',
        }
        request.session['errors'] = errors
        return HttpResponseRedirect(reverse('errors:errors'))

def withdrawal(request):
    """
    ----------------------------------------------------------------------
    ユーザー／退会ページ
    ----------------------------------------------------------------------
    """
    try:
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

    # -------------------------------------------------------
    # エラー処理
    # -------------------------------------------------------
    except Exception as e:
        errors = {
            'type': str(type(e)),
            'args': str(e.args),
            'err' : str(e),
            'msg' : '',
        }
        request.session['errors'] = errors
        return HttpResponseRedirect(reverse('errors:errors'))

def run_withdrawal(request):
    """
    ----------------------------------------------------------------------
    ユーザー／退会処理
    ----------------------------------------------------------------------
    """
    try:
        # -------------------------------------------------------
        # セッション
        # -------------------------------------------------------
        if 'login_user' not in request.session:
            return HttpResponseRedirect(reverse('top:top'))
        
        login_user = request.session['login_user']

        # -------------------------------------------------------
        # 退会処理
        # -------------------------------------------------------
        # ユーザーをDBから削除
        user = User.objects.get(pk=login_user['id'])
        user.delete()

        # ユーザーをセッションから削除
        del request.session['login_user']

        # -------------------------------------------------------
        # ページ遷移
        # -------------------------------------------------------
        return HttpResponseRedirect(reverse('top:top'))
    
    # -------------------------------------------------------
    # エラー処理
    # -------------------------------------------------------
    except Exception as e:
        errors = {
            'type': str(type(e)),
            'args': str(e.args),
            'err' : str(e),
            'msg' : '',
        }
        request.session['errors'] = errors
        return HttpResponseRedirect(reverse('errors:errors'))

def detail(request, user_id):
    """
    ----------------------------------------------------------------------
    ユーザー／プロフィール詳細ページ
    ----------------------------------------------------------------------
    """
    try:
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
        user = User.objects.get(pk=user_id)

        # プロフィールの取得 --------------------------------
        profile = Profile.objects.get(target_user_id=user_id)

        # コードの取得 ------------------------------------
        codes = Code.objects.filter(target_user_id=user_id)

        # フォロー数の取得 ---------------------------------
        follow_num = Follow.objects.filter(follow_user_id=user_id).count()
        
        # フォロワー数の取得 -------------------------------
        follower_num = Follow.objects.filter(followed_user_id=user_id).count()

        # フォローしているかどうかの判定 ---------------------
        temp = ''
        temp = Follow.objects.filter(follow_user_id=login_user['id'], followed_user_id=user_id)
        
        if len(temp) == 1:
            follow_id = temp[0].id

        # ログインユーザーの判定 ----------------------------
        if user.id == login_user['id']:
            is_me = True

        # 申請中の判定 ------------------------------------
        permit = Permit.objects.filter(target_user_id=user_id, request_user_id=login_user['id'])
        if permit:
            is_permit = True

        # -------------------------------------------------------
        # ページ遷移
        # -------------------------------------------------------
        return render(request, "user/detail.html", {
            'user'        : user,
            'profile'     : profile,
            'codes'       : codes,
            'follow_num'  : follow_num,
            'follower_num': follower_num,
            'follow_id'   : follow_id,
            'is_me'       : is_me,
            'is_permit'   : is_permit,
        })
    
    # -------------------------------------------------------
    # エラー処理
    # -------------------------------------------------------
    except Exception as e:
        errors = {
            'type': str(type(e)),
            'args': str(e.args),
            'err' : str(e),
            'msg' : '',
        }
        request.session['errors'] = errors
        return HttpResponseRedirect(reverse('errors:errors'))

def create(request):
    """
    ----------------------------------------------------------------------
    ユーザー／プロフィール新規作成ページ
    ----------------------------------------------------------------------
    """
    try:
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

    # -------------------------------------------------------
    # エラー処理
    # -------------------------------------------------------
    except Exception as e:
        errors = {
            'type': str(type(e)),
            'args': str(e.args),
            'err' : str(e),
            'msg' : '',
        }
        request.session['errors'] = errors
        return HttpResponseRedirect(reverse('errors:errors'))

def run_create(request):
    """
    ----------------------------------------------------------------------
    ユーザー／プロフィール新規作成処理
    ----------------------------------------------------------------------
    """
    try:
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
            user_id = request.POST['id']
            user = User.objects.get(pk=user_id)
            if 'image_icon' in request.FILES:
                if request.FILES['image_icon'] != '':
                    user.image_icon = request.FILES['image_icon']
            
            user.save()

        # プロフィール ----------------------------------------
        # 情報保管
        temp_pub = False
        if request.POST['publish'] == 'on':
            temp_pub = True

        # DB処理
        profile = Profile(
            profile_text   = request.POST['profile'],
            publish        = temp_pub,
            target_user_id = request.POST['id'],
        )
        profile.save()

        # -------------------------------------------------------
        # 後処理
        # -------------------------------------------------------
        # ユーザーID取得
        user_id = login_user['id']

        # -------------------------------------------------------
        # ページ遷移
        # -------------------------------------------------------
        return HttpResponseRedirect(reverse('user:detail', args=(user_id,)))

    # -------------------------------------------------------
    # エラー処理
    # -------------------------------------------------------
    except Exception as e:
        errors = {
            'type': str(type(e)),
            'args': str(e.args),
            'err' : str(e),
            'msg' : '',
        }
        request.session['errors'] = errors
        return HttpResponseRedirect(reverse('errors:errors'))

def edit(request, user_id):
    """
    ----------------------------------------------------------------------
    ユーザー／プロフィール編集ページ
    ----------------------------------------------------------------------
    """
    try:
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
        temp = User.objects.get(pk=user_id)

        disp_profile['id']         = temp.id
        disp_profile['username']   = temp.username
        disp_profile['password']   = temp.password
        disp_profile['image_icon'] = temp.image_icon
        

        # プロフィールの取得 -------------------------------
        temp = Profile.objects.filter(target_user_id=user_id)[0:1]

        if len(temp) > 0:
            temp2 = temp[0]
            disp_profile['profile_text'] = temp2.profile_text
            disp_profile['publish']      = temp2.publish

        # メッセージの取得
        message = ''
        if 'message' in request.session:
            message = request.session['message']
            del request.session['message']

        # -------------------------------------------------------
        # ページ遷移
        # -------------------------------------------------------
        return render(request, "user/edit.html", {
            'profile': disp_profile,
            'message': message,
        })

    # -------------------------------------------------------
    # エラー処理
    # -------------------------------------------------------
    except Exception as e:
        errors = {
            'type': str(type(e)),
            'args': str(e.args),
            'err' : str(e),
            'msg' : '',
        }
        request.session['errors'] = errors
        return HttpResponseRedirect(reverse('errors:errors'))

def run_edit(request, user_id):
    """
    ----------------------------------------------------------------------
    ユーザー／プロフィール編集処理
    ----------------------------------------------------------------------
    """
    try:
        # -------------------------------------------------------
        # セッション
        # -------------------------------------------------------
        if 'login_user' not in request.session:
            return HttpResponseRedirect(reverse('top:top'))
        
        login_user = request.session['login_user']

        # -------------------------------------------------------
        # バリデーション
        # -------------------------------------------------------
        # ユーザー名
        if request.POST['username'] == '':
            request.session['message'] = 'ユーザー名は必ず入力してください。'
            return HttpResponseRedirect(reverse('user:edit', args=(login_user['id'], )))
            
        # パスワード
        if request.POST['password'] == '':
            request.session['message'] = 'パスワードは必ず入力してください。'
            return HttpResponseRedirect(reverse('user:edit', args=(login_user['id'], )))
        
        # -------------------------------------------------------
        # データベース保存
        # -------------------------------------------------------
        # ユーザー -------------------------------------------
        if request.POST['id']:
            # 対象レコード取得
            user = User.objects.get(pk=request.POST['id'])
            if 'image_icon' in request.FILES:
                if request.FILES['image_icon'] != '':
                    user.image_icon = request.FILES['image_icon']
            user.username = request.POST['username']
            user.password = request.POST['password']

            # 更新
            user.save()
        
        # プロフィール ----------------------------------------
        # 情報保管
        temp_pub = False
        if request.POST['publish'] == 'on':
            temp_pub = True

        # 対象レコード取得
        profile = Profile.objects.get(target_user_id=request.POST['id'])
        profile.profile_text = request.POST['profile']
        profile.publish      = temp_pub

        # 更新
        profile.save()

        # -------------------------------------------------------
        # ページ遷移
        # -------------------------------------------------------
        return HttpResponseRedirect(reverse('user:detail', args=(user_id,)))

    # -------------------------------------------------------
    # エラー処理
    # -------------------------------------------------------
    except Exception as e:
        errors = {
            'type': str(type(e)),
            'args': str(e.args),
            'err' : str(e),
            'msg' : '',
        }
        request.session['errors'] = errors
        return HttpResponseRedirect(reverse('errors:errors'))

def index(request):
    """
    ----------------------------------------------------------------------
    ユーザー／ユーザー一覧ページ
    ----------------------------------------------------------------------
    """
    try:
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

        # -------------------------------------------------------
        # ページ遷移
        # -------------------------------------------------------
        return render(request, "user/index.html", {
            'user_list': user_list,
        })

    # -------------------------------------------------------
    # エラー処理
    # -------------------------------------------------------
    except Exception as e:
        errors = {
            'type': str(type(e)),
            'args': str(e.args),
            'err' : str(e),
            'msg' : '',
        }
        request.session['errors'] = errors
        return HttpResponseRedirect(reverse('errors:errors'))