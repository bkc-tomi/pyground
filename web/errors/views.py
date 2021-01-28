from django.shortcuts import render
from django.urls      import reverse
from django.http      import HttpResponse, HttpResponseRedirect

def errors(request):
    """
    ----------------------------------------------------------------------
    エラーページ
    ----------------------------------------------------------------------
    """
    # ---------------------------------------------
    # エラー情報取得
    # ---------------------------------------------
    errors = {}
    if 'errors' in request.session:
        errors = request.session['errors']
        del request.session['errors']

    # ---------------------------------------------
    # ページ遷移
    # ---------------------------------------------
    return render(request, 'errors/index.html', {
        'errors': errors,
    })