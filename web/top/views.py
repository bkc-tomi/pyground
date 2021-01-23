from django.shortcuts import render
from django.http import HttpResponse


"""
----------------------------------------------------------------------
トップ／トップページ
----------------------------------------------------------------------
"""
def top(request):
    return render(request, 'top/index.html')
