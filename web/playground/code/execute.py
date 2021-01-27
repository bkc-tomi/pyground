import os
import subprocess
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

def exec_subprocess(cmd: str) -> (str, str, int):
    """
    シェルコマンド実行関数

    :explanation:OSコマンドを実行し結果を返す
    :param cmd  : コマンド文字列
    :return     : 標準出力、標準エラー出力、リターンコードのタプル
    """
    child = subprocess.Popen(cmd, shell=True,
                             stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = child.communicate()
    rt = child.returncode
    return stdout.decode(), stderr.decode(), rt

def exec_code(code: str):
    """
    コード実行関数

    :explanation:引数で受け取った文字列のコードを実行し結果を返す
    :param code : コード文字列
    :return     : 標準出力の文字列
    """
    # ファイルパス
    file_name = 'exec_code.py'
    file_path = str(BASE_DIR) + '/code/' + file_name

    # ファイルの作成
    f = open(file_path, 'w')
    f.write(code)
    f.close()

    # ファイルの実行
    stdout, stderr, rt = exec_subprocess("python " + file_path)

    if stderr:
        return stderr

    return stdout