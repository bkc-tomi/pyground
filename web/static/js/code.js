/**
 * ----------------------------------------------------------------------------
 * ** 内容 **  
 * インプット要素フォーカス時にタブキーを押すと次の要素にフォーカスするのをキャンセルし
 * タブ入力ができる
 * ----------------------------------------------------------------------------
 */
function tabInsertToEditer(e) {
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
}

/**
 * ----------------------------------------------------------------------------
 * ** 内容 **  
 * コード入力エリアにおいて書いているコードの行数に合わせて
 * 隣の行数表示の変更とテキストエリアの行数を変更する。
 * ----------------------------------------------------------------------------
 */
function changeRows(e) {
    const editer = e.currentTarget;
    // 行数取得 ------------------------------------------------
    let charNum = editer.value;
    num = charNum.match(/\n/g);   //IE未対応
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
}

const indexEditer    = document.getElementById('index-code');
const editEditer     = document.getElementById('edit-code');
const questionEditer = document.getElementById('question-code');

if (indexEditer) {
    indexEditer.addEventListener('keydown', tabInsertToEditer);
    indexEditer.addEventListener('keyup', changeRows);
}

if (editEditer) {
    editEditer.addEventListener('keydown', tabInsertToEditer);
    editEditer.addEventListener('keyup', changeRows);
}

if (questionEditer) {
    questionEditer.addEventListener('keydown', tabInsertToEditer);
    questionEditer.addEventListener('keyup', changeRows);
}