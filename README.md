####【説明】
　Python にて"yahooファイナンス(https://finance.yahoo.co.jp/)"から株価をhtml方式で取得します。
　LINE Notify(https://notify-bot.line.me/ja/)サービスを使用して、LINEに送信します。
　自動送信はAWSのlambdaサービスを使用しました。

####コードの注意】
　コード内のyahooファイナンスURLを取得したい会社に変更してください。
　LINE Notifyからアクセストークンを取得し、コードに入れ込んでください。

####【AWS lambdaで使用する際の注意点】
　AWS lambdaで使用する場合、以下のハンドラーを作成しメインの処理を入れ込む必要がある。
　また、使用したライブラリーをインストールした後、フォルダにひとまとめにする。
　最後に.zip形式にて圧縮することでAWSにアップロードできる。
　def lambda_handler(event, context):