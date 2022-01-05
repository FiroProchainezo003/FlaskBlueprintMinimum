# Flask Blueprint 最小サンプル

## プロジェクトについて

このプロジェクトはFlaskのBlueprintを使った最小サンプルです。

Flaskのサンプルでは `app.py` がよく登場します。<br>
通常は `app.py` にエンドポイントを追加して機能を盛り込んでいきますが、10個20個とエンドポイントが増えていくと行数が多くなりすぎてわかりにくくなってしまいます。<br>
そんな時に役に立つのが `Blueprint` です。<br>
`Blueprint` を使うとソースコードのファイルを分割することができ非常に便利です。<br>
`Blueprint` でファイルを分割する場合は、機能毎に分割するなど自分なりのルールを作るとさらに分かり安くなります。<br>
本サンプルでは、メインファイルの `app.py` とは別に `views/app1.py`、`views/app2.py` を作成し、ファイル分割を行っています。<br>
それぞれに作成したエンドポイントは1つずつの合計3つですが、使い方は理解いただけると思います。<br>

`Blueprint` の使い方を学ぶ場合は、 `app.py` から確認ください。<br>

実行するととりあえず動きますので、ブラウザから `http://localhost:5000/` を確認してください。<br>
設定したエンドポイントがどのようなURLになっているか気になると思いますが、Pythonの対話モードを起動し、以下を実行すると簡単に確認可能です。<br>

```python
from app import app
app
<Flask 'app'>
app.url_map
Map([<Rule '/app1/' (OPTIONS, GET, HEAD) -> app1.index>,
 <Rule '/app2/' (OPTIONS, GET, HEAD) -> app2.index>,
 <Rule '/' (OPTIONS, GET, HEAD) -> hello_world>,
 <Rule '/static/<filename>' (OPTIONS, GET, HEAD) -> static>])
```

## プロジェクトの取得方法

クローンしてください。
```
git clone https://github.com/FiroProchainezo003/FlaskBlueprintMinimum
```

## 実行方法

### windows

```
# Cloneしたフォルダで
$ python3 -m vevn venv
$ venv\Scripts\activate
$ pip install -r requirements.txt
$ python app.py
```

ブラウザから localhost:5000 にアクセス

### linux

```
# Cloneしたフォルダで
$ python3 -m vevn venv
$ source venv/Scripts/activate
$ pip install -r requirements.txt
$ python app.py
```

ブラウザから localhost:5000 にアクセス

## pythonバージョン

作成環境は python 3.9.7

## Flaskがサポートしているバージョン

[Flask - 2.0.x Installation](https://flask.palletsprojects.com/en/2.0.x/installation/)

    Python 3.7+






