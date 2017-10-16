# automatic-sakito
[sakito.cirkit.jp](https://sakito.cirkit.jp/)を自動化するスクリプト

# 動かし方
1. ユーザファイルを作成する
```bash
vim user.py
```
- ファイルの中身は次のとおりです。
```python
email = 'your email'
password = 'your password'
```

2. Dockerイメージを作成
```bash
docker build -t automatic-sakito .
```

3. cronを使って毎日1時にスクリプトを走らせる
```bash
crontab -e
```
- ファイルの中身は次のとおりです。
```crontab
0 1 * * * docker run --name sakitoscript automatic-sakito /scripts/automatic-sakito.py -a && docker rm sakitoscript
```