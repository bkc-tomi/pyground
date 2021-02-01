from django.shortcuts import render
from django.urls      import reverse
from django.http      import HttpResponse, HttpResponseRedirect

class CommonFuncSet():
    def set_error_to_session(request, e, msg):
        """
        ----------------------------------------------------------------------
        ** 内容 **
        エラーとメッセージをセッションにセットする関数
        ** 引数 **
        request: request
        e      : エラーオブジェクト(Exception)
        msg    : ユーザー指定メッセージ(文字列)
        ** 返り値 **
        なし
        ----------------------------------------------------------------------
        """
        errors = {
            'type': str(type(e)),
            'args': str(e.args),
            'err' : str(e),
            'msg' : msg,
        }
        request.session['errors'] = errors


    def get_from_session(request, key):
        """
        ----------------------------------------------------------------------
        ** 内容 **
        セッションから値を取得する関数
        ** 引数 **
        request: request
        key    : セッション配列のキー(session[key])
        ** 返り値 **
        値　　　（session[key]が存在する場合）
        空文字列（session[key]が存在しない場合）
        ----------------------------------------------------------------------
        """
        value = ''
        if key in request.session:
            value = request.session[key]
            del request.session[key]
        return value

    def set_to_session(request, key, value):
        """
        ----------------------------------------------------------------------
        ** 内容 **
        セッションに値をセットする関数
        ** 引数 **
        request: request
        key    : セッション配列のキー(session[key])
        value  : session[key]にセットする値
        ** 返り値 **
        なし
        ----------------------------------------------------------------------
        """
        request.session[key] = value
