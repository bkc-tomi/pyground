/**
 * ------------------------------------------------------------
 * csrftokenの取得に使用する関数群
 * ------------------------------------------------------------
 */
function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            // var cookie = jQuery.trim(cookies[i]);
            var cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

function csrfSafeMethod(method) {
    // these HTTP methods do not require CSRF protection
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}

/**
 * ------------------------------------------------------------
 * index_page
 * ------------------------------------------------------------
 */
function savePost() {
    // 値の取得
    const csrfToken = getCookie("csrftoken");
    const codeName  = document.getElementById("index-code-name");
    const code      = document.getElementById("index-code");
    
    // フォームの作成
    let f = document.createElement('form');   
    f.method = 'post';
    f.action = '/playground/save/';

    // 要素の追加
    tokenTag    = '<input type="hidden" name="csrfmiddlewaretoken" value='+ csrfToken + '>';
    codeNameTag = '<input type="hidden" name="code-name" value='+  codeName.value + '>';
    codeTag     = '<textarea name="code">'+  code.value + '</textarea>';

    f.innerHTML = tokenTag + codeNameTag + codeTag;

    // フォームの送信
    document.body.append(f);
    f.submit();
}

// 未実装
function runPost() {
    const csrfToken = getCookie("csrftoken");
    const code     = document.getElementById("index-code");
    const codeName = document.getElementById("index-code-name");
    
    // フォームの作成
    let f = document.createElement('form');   
    f.method = 'post';
    f.action = '/playground/run/';

    // 要素の追加
    tokenTag    = '<input type="hidden" name="csrfmiddlewaretoken" value='+ csrfToken + '>';
    codeNameTag = '<input type="hidden" name="code-name" value='+  codeName.value + '>';
    codeTag     = '<textarea name="code">'+  code.value + '</textarea>';

    f.innerHTML = tokenTag + codeNameTag + codeTag;
    
    // フォームの送信
    document.body.append(f);
    f.submit();
}

/**
 * ------------------------------------------------------------
 * edit_page
 * ------------------------------------------------------------
 */

function updateEditPost(code_id) {
    const csrfToken = getCookie("csrftoken");
    const code     = document.getElementById("edit-code");
    const codeName = document.getElementById("edit-code-name");
    
    // フォームの作成
    let f = document.createElement('form');   
    f.method = 'post';
    f.action = '/playground/' + code_id + '/update/';

    // 要素の追加
    tokenTag    = '<input type="hidden" name="csrfmiddlewaretoken" value='+ csrfToken + '>';
    codeNameTag = '<input type="hidden" name="code-name" value='+  codeName.value + '>';
    codeTag     = '<textarea name="code">'+  code.value + '</textarea>';

    f.innerHTML = tokenTag + codeNameTag + codeTag;
    
    // フォームの送信
    document.body.append(f);
    f.submit();
}

// 未実装
function runEditPost(code_id) {
    const csrfToken = getCookie("csrftoken");
    const code     = document.getElementById("edit-code");
    const codeName = document.getElementById("edit-code-name");
    
    // フォームの作成
    let f = document.createElement('form');   
    f.method = 'post';
    f.action = '/playground/'+ code_id + '/run/';

    // 要素の追加
    tokenTag    = '<input type="hidden" name="csrfmiddlewaretoken" value='+ csrfToken + '>';
    codeNameTag = '<input type="hidden" name="code-name" value='+  codeName.value + '>';
    codeTag     = '<textarea name="code">'+  code.value + '</textarea>';

    f.innerHTML = tokenTag + codeNameTag + codeTag;
    
    // フォームの送信
    document.body.append(f);
    f.submit();
}

/**
 * ------------------------------------------------------------
 * question_page
 * ------------------------------------------------------------
 */

// 未実装
function runQuestionPost(question_id) {
    const csrfToken = getCookie("csrftoken");
    const code      = document.getElementById("question-code");
    const answer    = document.getElementById("question-answer");
    
    // フォームの作成
    let f = document.createElement('form');   
    f.method = 'post';
    f.action = '/playground/question/' + question_id + '/run/';

    // 要素の追加
    tokenTag    = '<input type="hidden" name="csrfmiddlewaretoken" value='+ csrfToken + '>';
    codeTag     = '<textarea name="code">'+  code.value + '</textarea>';
    answerTag   = '<textarea name="answer">'+  answer.value + '</textarea>';

    f.innerHTML = tokenTag + codeTag + answerTag;
    
    // フォームの送信
    document.body.append(f);
    f.submit();
}

