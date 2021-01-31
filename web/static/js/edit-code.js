const editer = document.getElementById('edit-code');

/**
 * ----------------------------------------------------------------------------
 * edit.html -> edit-code
 * 
 * テキストエリアにおいてタブ入力で別のタグにフォーカスすることをキャンセルしタブをいれる
 * ----------------------------------------------------------------------------
 */
editer.addEventListener('keydown',function(e) {
    var elem, end, start, value;
    if (e.keyCode === 9) {
        if (e.preventDefault) {
        e.preventDefault();
        }
        elem = e.target;
        start = elem.selectionStart;
        end = elem.selectionEnd;
        value = elem.value;
        elem.value = "" + (value.substring(0, start)) + "\t" + (value.substring(end));
        elem.selectionStart = elem.selectionEnd = start + 1;
        return false;
    }
});

/**
 * ----------------------------------------------------------------------------
 * edit.html -> edit-code
 * 
 * 行数を取得する
 * ----------------------------------------------------------------------------
 */
editer.addEventListener('keydown', function() {
    // 行数取得 ------------------------------------------------
    let charNum = editer.value;
    num = charNum.match(/\n/g);   //Firefox 用
    
    let lineNum = 20;
    if (num) {
        if (num.length + 1 > lineNum) {
            lineNum = num.length + 2;
        }
    }

    // 行数表示 ------------------------------------------------
    let codeNum = document.getElementsByClassName('line-number')[0];
    // 小要素削除
    while (codeNum.firstChild) {
        codeNum.removeChild(codeNum.firstChild);
    }

    // 新しい小要素追加
    for (let i = 1; i <= lineNum; i++) {
        var div = document.createElement('div');
        div.innerHTML = i;
        codeNum.appendChild(div);
    }

    // テキストエリアの行数変更 -----------------------------------
    editer.rows = lineNum;
    
});