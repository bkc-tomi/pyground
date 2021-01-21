|No. |アプリケーション名|タイトル|URL|view|template|内容|備考|
|----|----|----|----|----|----|----|----|
|01|トップ|トップページ| /top/ |||サイトの説明<br>お知らせ||
|02|ユーザー|登録ページ| /user/register/ |||登録内容の入力<br>フォーム送信||
|03|ユーザー|登録処理| /user/run/register/ |||登録処理||
|04|ユーザー|ログインページ| /user/login/ |||ログイン情報の入力<br>フォーム送信||
|05|ユーザー|ログイン処理| /user/run/login/ |||ログイン処理||
|06|ユーザー|ログアウト処理| /user/<int: user_id>/run/logout/ |||ログアウト処理||
|07|ユーザー|退会ページ| /user/<int: user_id>/withdrawal/ |||退会についての説明<br>大会の確認||
|08|ユーザー|退会処理| /user/<int: user_id>/run/withdrawal/ |||退会処理||
|09|ユーザー|プロフィール詳細| /user/<int: user_id>/detail/ |||ユーザー情報の表示<br>フォローリスト・フォロワーリストの一部表示||
|10|ユーザー|プロフィール編集ページ| /user/<int: user_id>/edit/ |||ユーザー情報の編集<br>フォーム送信||
|11|ユーザー|プロフィール編集処理| /user/<int: user_id>/run/edit/ |||ユーザー情報編集処理||
|12|フォロー|ユーザー一覧| /user/list/ |||ユーザーの表示||
|13|フォロー|フォロー一覧| /user/<int: user_id>/follow/ |||フォローしているユーザーを表示<br>フォロー解除||
|14|フォロー|フォロー解除処理| /user/<int: user_id>/follow/release?user_id= |||フォロー解除処理||
|15|フォロー|フォロワー一覧| /user/<int: user_id>/follower/ |||フォローされているユーザーを表示||
|16|フォロー|フォロー認証| /user/<int: user_id>/follow/auth/ |||フォロー申請の認証(プライベートアカウント)||
|17|問題|問題一覧| /question/list/ |||問題一覧の表示(全て)<br>ブックマークフォーム送信||
|18|問題|ブックマーク処理| /question/list?user_id=&question_id= |||ブックマーク処理||
|19|問題|問題詳細| /question/<int: question_id>/detail/ |||問題詳細の表示(問題の情報、解いた人一覧)||
|20|問題|問題編集・新規作成ページ| /question/edit?question_id= |||問題の作成・既存の問題の編集内容を入力<br>フォーム送信||
|21|問題|問題編集・新規作成処理| /question/run/edit?question_id= |||問題の作成・既存の問題の編集処理||
|22|ブックマーク|問題一覧| /bookmark/<int: user_id>/list/ |||問題一覧の表示(自分作成・ブックマーク)||
|24|プレイグランド|入力ページ| /playground/<int: code_id> |||コード入力<br>実行フォーム送信<br>保存フォーム送信||
|25|プレイグランド|実行処理| /playground/<int: code_id>/run/ |||コードの実行<br>問題との答え合わせ<br>正解者登録||
|24|プレイグランド|問題ページ| /playground/<int: question_id>/<int: code_id> |||コード入力<br>問題フォーム送信<br>保存フォーム送信<br>問題フォーム送信||
|25|プレイグランド|問題処理| /playground/<int: question_id>/<int: code_id>/run/ |||コードの実行<br>問題との答え合わせ<br>正解者登録||
|26|プレイグランド|保存処理| /playground/<int: code_id>/save/ |||コードの保存||