|No. |アプリケーション名|タイトル|URL|view|template|内容|備考|
|----|----|----|----|----|----|----|----|
|0|トップ|トップページ| /top/ | top | /top/index.html |サイトの説明<br>お知らせ||
|0|ユーザー|登録ページ| /user/register/ | register | /user/register.html |登録内容の入力<br>フォーム送信|登録メールの送信メッセージを表示|
|0|ユーザー|登録完了ページ| /user/register/complete | register_complete | /user/register_complete.html |登録処理が終了したら遷移するページ||
|0|ユーザー|登録処理| /user/run/register/ | run_register ||登録処理|登録ページからPOSTで取得|
|0|ユーザー|ログインページ| /user/login/ | login | /user/login.html |ログイン情報の入力<br>フォーム送信||
|0|ユーザー|ログイン処理| /user/run/login/ | run_login ||ログイン処理|ログインページからPOSTで取得|
|0|ユーザー|ログアウト処理| /user/<int: user_id>/run/logout/ | run_logout ||ログアウト処理|各ページのヘッダーからPOSTで取得|
|0|ユーザー|退会ページ| /user/<int: user_id>/withdrawal/ | withdrawal | /user/withdrawal.html |退会についての説明<br>大会の確認||
|0|ユーザー|退会処理| /user/<int: user_id>/run/withdrawal/ | run_withdrawal ||退会処理|退会ページからPOSTで取得|
|0|ユーザー|プロフィール詳細| /user/<int: user_id>/detail | detail | /user/detail.html |ユーザー情報の表示<br>フォローリスト・フォロワーリストの一部表示||
|0|ユーザー|プロフィール編集ページ| /user/<int: user_id>/edit/ | edit | /user/edit.html |ユーザー情報の編集<br>フォーム送信||
||ユーザー|プロフィール編集処理| /user/<int: user_id>/run/edit/ | run_edit ||ユーザー情報編集処理|プロフィール編集ページからPOSTで取得|
||ユーザー|ユーザー一覧ページ| /user/ | index | /user/index.html |ユーザーの表示||
||フレンド|フォロー一覧ページ| /friend/<int: user_id>/follow/ | follow | /follow/follow.html |フォローしているユーザーを表示<br>フォロー解除||
||フレンド|フォロー解除処理| /friend/<int: user_id>/follow/release?user_id= | release ||フォロー解除処理|フォロー一覧ページからPOSTで取得|
||フレンド|フォロワー一覧ページ| /friend/<int: user_id>/follower/ | follower | /follow/follower.html |フォローされているユーザーを表示||
||フレンド|フォロー許可ページ| /friend/<int: user_id>/follow/permit/ | permit | /follow/permit.html |フォロー申請の認証(プライベートアカウント)||
||フレンド|フォロー許可処理| /friend/<int: user_id>/follow/run/permit/ | run_permit ||フォロー申請の許可(プライベートアカウント)|フォロー許可ページからPOSTで取得|
||フレンド|フォロー不許可処理| /friend/<int: user_id>/follow/run/nopermit/ | run_nopermit ||フォロー申請の不許可(プライベートアカウント)|フォロー許可ページからPOSTで取得|
||問題|問題一覧ページ| /question/list/ | questions | /question/index.html |問題一覧の表示(全て)<br>ブックマークフォーム送信||
||問題|問題管理ページ| /question/<int: user_id>/manage/ | manage | /question/manage.html |問題一覧の表示(自作)||
||問題|問題詳細ページ| /question/<int: question_id>/detail/ | detail | /question/detail.html |問題詳細の表示(問題の情報、解いた人一覧)||
||問題|問題編集・新規作成ページ| /question/<int: question_id>/edit/ | edit | /question/edit.html |問題の作成・既存の問題の編集内容を入力<br>フォーム送信||
||問題|問題編集・新規作成処理| /question/<int: question_id>/run/edit?question_id= | run_edit |  |問題の作成・既存の問題の編集処理|問題編集・新規作成ページからPOSTで取得|
||ブックマーク|ブックマーク一覧ページ| /bookmark/<int: user_id>/list/ | index | /bookmark/index.html |問題一覧の表示(自分作成・ブックマーク)||
||ブックマーク|ブックマーク処理| /bookmark/<int: question_id>/run | run_bookmark ||ブックマーク処理|問題一覧ページからPOSTで取得|
||ブックマーク|ブックマーク解除処理| /bookmark/<int: question_id>/release/ | release |  |問題一覧の表示(自分作成・ブックマーク)||
||プレイグランド|入力ページ| /playground/<int: code_id> | index | /playground/index.html |コード入力<br>実行フォーム送信<br>保存フォーム送信||
||プレイグランド|実行処理| /playground/<int: code_id>/run/ | run ||コードの実行<br>問題との答え合わせ<br>正解者登録|入力ページからPOSTで取得|
||プレイグランド|問題ページ| /playground/<int: question_id>/<int: code_id> | question | /playground/question.html |コード入力<br>問題フォーム送信<br>保存フォーム送信<br>問題フォーム送信||
||プレイグランド|問題処理| /playground/<int: question_id>/<int: code_id>/run/ | run_question ||コードの実行<br>問題との答え合わせ<br>正解者登録|問題ページからPOSTで取得|
||プレイグランド|保存処理| /playground/<int: code_id>/save/ | save ||コードの保存|入力ページ、問題ページからPOSTで取得|