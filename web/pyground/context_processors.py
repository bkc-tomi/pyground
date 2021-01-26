import logging

from django.shortcuts import render
from django.urls      import reverse
from django.http      import HttpResponse, HttpResponseRedirect

from user.models           import User, Profile
from playground.models import Code
from friend.models     import Follow

def constant_text(request):
    login_user = ''

    if 'login_user' in request.session:
        login_user = request.session['login_user']

    return {
        'login_user': login_user,
    }
