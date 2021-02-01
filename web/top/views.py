from django.shortcuts import render
from django.http import HttpResponse

# 共通関数
from common.func import CommonFuncSet

def top(request):
    """
    ----------------------------------------------------------------------
    トップ／トップページ
    ----------------------------------------------------------------------
    """
    try:
        # -------------------------------------------------------
        # ページ遷移
        # -------------------------------------------------------
        return render(request, 'top/index.html')
    
    # -------------------------------------------------------
    # エラー処理
    # -------------------------------------------------------
    except Exception as e:
        CommonFuncSet.set_error_to_session(request, e, '')
        return HttpResponseRedirect(reverse('errors:errors'))