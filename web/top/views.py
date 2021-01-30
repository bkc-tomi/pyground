from django.shortcuts import render
from django.http import HttpResponse


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
        errors = {
            'type': str(type(e)),
            'args': str(e.args),
            'err' : str(e),
            'msg' : '',
        }
        request.session['errors'] = errors
        return HttpResponseRedirect(reverse('errors:errors'))