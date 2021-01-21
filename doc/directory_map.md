|No. |アプリケーション名|タイトル|URL|view|template|内容|備考|
|----|----|----|----|----|----|----|----|
|01|トップ|トップページ| /top/ | top | /top/index.html |サイトの説明<br>お知らせ||
|02|ユーザー|登録ページ| /user/register/ | register | /user/register.html |登録内容の入力<br>フォーム送信||
|03|ユーザー|登録処理| /user/run/register/ | run_register ||登録処理|登録ページからPOSTで取得|
|04|ユーザー|ログインページ| /user/login/ | login | /user/login.html |ログイン情報の入力<br>フォーム送信||
|05|ユーザー|ログイン処理| /user/run/login/ | run_login ||ログイン処理|ログインページからPOSTで取得|
|06|ユーザー|ログアウト処理| /user/<int: user_id>/run/logout/ | run_logout ||ログアウト処理|各ページのヘッダーからPOSTで取得|
|07|ユーザー|退会ページ| /user/<int: user_id>/withdrawal/ | withdrawal | /user/withdrawal.html |退会についての説明<br>大会の確認||
|08|ユーザー|退会処理| /user/<int: user_id>/run/withdrawal/ | run_withdrawal ||退会処理|退会ページからPOSTで取得|
|09|ユーザー|プロフィール詳細| /user/<int: user_id>/detail | detail | /user/detail.html |ユーザー情報の表示<br>フォローリスト・フォロワーリストの一部表示||
|10|ユーザー|プロフィール編集ページ| /user/<int: user_id>/edit/ | edit | /user/edit.html |ユーザー情報の編集<br>フォーム送信||
|11|ユーザー|プロフィール編集処理| /user/<int: user_id>/run/edit/ | run_edit ||ユーザー情報編集処理|プロフィール編集ページからPOSTで取得|
|12|ユーザー|ユーザー一覧ページ| /user/ | index | /user/index.html |ユーザーの表示||
|13|フォロー|フォロー一覧ページ| /user/<int: user_id>/follow/ | follow | /follow/follow.html |フォローしているユーザーを表示<br>フォロー解除||
|14|フォロー|フォロー解除処理| /user/<int: user_id>/follow/release?user_id= | release ||フォロー解除処理|フォロー一覧ページからPOSTで取得|
|15|フォロー|フォロワー一覧ページ| /user/<int: user_id>/follower/ | follower | /follow/follower.html |フォローされているユーザーを表示||
|16|フォロー|フォロー認証ページ| /user/<int: user_id>/follow/auth/ | auth | /follow/auth.html |フォロー申請の認証(プライベートアカウント)||
|17|フォロー|フォロー認証処理| /user/<int: user_id>/follow/run/auth/ | run_auth ||フォロー申請の認証(プライベートアカウント)|フォロー認証ページからPOSTで取得|
|18|問題|問題一覧ページ| /question/list/ | question | /question/index.html |問題一覧の表示(全て)<br>ブックマークフォーム送信||
|19|問題|自問題一覧ページ| /question/<int: user_id>/list/ | question | /question/index.html |問題一覧の表示(自作)||
|20|問題|ブックマーク処理| /question/list?user_id=&question_id= | bookmark ||ブックマーク処理|問題一覧ページからPOSTで取得|
|21|問題|問題詳細ページ| /question/<int: question_id>/detail/ | detail | /question/detail.html |問題詳細の表示(問題の情報、解いた人一覧)||
|22|問題|問題編集・新規作成ページ| /question/edit/ | edit | /question/edit.html |問題の作成・既存の問題の編集内容を入力<br>フォーム送信||
|23|問題|問題編集・新規作成処理| /question/run/edit?question_id= | run_edit |  |問題の作成・既存の問題の編集処理|問題編集・新規作成ページからPOSTで取得|
|24|ブックマーク|ブックマーク一覧ページ| /bookmark/<int: user_id>/list/ | index | /bookmark/index.html |問題一覧の表示(自分作成・ブックマーク)||
|25|ブックマーク|ブックマーク解除処理| /bookmark/<int: user_id>/list/ | release |  |問題一覧の表示(自分作成・ブックマーク)||
|26|プレイグランド|入力ページ| /playground/<int: code_id> | index | /playground/index.html |コード入力<br>実行フォーム送信<br>保存フォーム送信||
|27|プレイグランド|実行処理| /playground/<int: code_id>/run/ | run ||コードの実行<br>問題との答え合わせ<br>正解者登録|入力ページからPOSTで取得|
|28|プレイグランド|問題ページ| /playground/<int: question_id>/<int: code_id> | question | /playground/question.html |コード入力<br>問題フォーム送信<br>保存フォーム送信<br>問題フォーム送信||
|29|プレイグランド|問題処理| /playground/<int: question_id>/<int: code_id>/run/ | run_question ||コードの実行<br>問題との答え合わせ<br>正解者登録|問題ページからPOSTで取得|
|30|プレイグランド|保存処理| /playground/<int: code_id>/save/ | save ||コードの保存|入力ページ、問題ページからPOSTで取得|