from django.shortcuts import render
from django.urls      import reverse
from django.http      import HttpResponse, HttpResponseRedirect

# 共通関数
from common.func import CommonFuncSet

def errors(request):
    """
    ----------------------------------------------------------------------
    エラーページ
    ----------------------------------------------------------------------
    """
    # ---------------------------------------------
    # エラー情報取得
    # ---------------------------------------------
    # 初期値
    errors = {
        'type': '',
        'args': '',
        'err' : '',
        'msg' : '',
    }

    # 更新
    err = CommonFuncSet.get_from_session(request, 'errors')
    if err != '':
        errors = err
        
    # ---------------------------------------------
    # ページ遷移
    # ---------------------------------------------
    return render(request, 'errors/index.html', {
        'errors': errors,
    })