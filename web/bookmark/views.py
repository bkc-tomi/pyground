from django.shortcuts import render
from django.http import HttpResponse

"""
----------------------------------------------------------------------
ブックマーク／一覧表示
----------------------------------------------------------------------
"""
def index(request):
    return HttpResponse("top page")


"""
----------------------------------------------------------------------
ブックマーク／ブックマーク解除
----------------------------------------------------------------------
"""
def release(request):
    return HttpResponse("run release")