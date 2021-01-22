from django.shortcuts import render
from django.http import HttpResponse


"""
----------------------------------------------------------------------
トップ／トップページ
----------------------------------------------------------------------
"""
def top(request):
    return HttpResponse("top page")
