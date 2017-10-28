# automatic-sakito
[sakito.cirkit.jp](https://sakito.cirkit.jp/)を自動化するスクリプト

## スクリプトの説明
- [turn_gacha.py](https://github.com/HayatoDoi/automatic-sakito/blob/master/turn_gacha.py) : ガチャを回す,標準出力は引いたガチャの得点
- [check_new_question.py](https://github.com/HayatoDoi/automatic-sakito/blob/master/check_new_question.py) : 新規アンケートの確認,新規アンケートがあった場合Slackへ通知を送る

## 動かし方
1. 設定ファイルを作成する
```bash
vim config.py
```
- ファイルの中身は次のとおりです。
```python
sakito = {
  'email' : 'bxxxxxxx@planet.kanazawa-it.ac.jp',
  'password' : 'xxxxxxxxxxxxxxxxxx',
}

slack = {
  'webhooksUrl' : 'https[:]//hooks.slack.com/services/xxxxxxxxxxxxxxxx/xxxxxxxxxxxxxxxx/xxxxxxxxxxxxxx',
}
```
webhookUrlは[こちら](https://slack.com/services/new/incoming-webhook)から生成してください。

2. Dockerイメージを作成
```bash
docker build -t automatic-sakito .
```

3. cronを使って毎日1時にガチャを回す, 毎時5分にアンケートの確認
```bash
crontab -e
```
- ファイルの中身は次のとおりです。
```crontab
0 1 * * * docker run --rm --name sakitoscript automatic-sakito python /scripts/turn_gacha.py
5 * * * * docker run --rm --name sakitoscript automatic-sakito python /scripts/check_new_question.py
```