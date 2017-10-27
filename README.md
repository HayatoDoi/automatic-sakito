# automatic-sakito
[sakito.cirkit.jp](https://sakito.cirkit.jp/)を自動化するスクリプト

# 動かし方
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
5 * * * * docker run --rm --name sakitoscript automatic-sakito python /scripts/check_new_qusation.py
```