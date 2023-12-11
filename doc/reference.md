# AviUtlPy

## How to Use
ある程度Pythonを理解している人向けです。<br/>
必要なライブラリは適宜`pip install`してください。

### lyric.py

歌詞、字幕、曲名表示などのテロップを作成します。

1. 表示したいテキストと表示時間を記述したtsvファイルを作成します。時間はミリ秒で指定します。<br/>
詳しくは`./sample/lyric/lyric.tsv`を参考にしてください。
2. 第1引数にテンプレートとするテキストオブジェクトのみを配置したexoファイル、<br/>
第2引数にtsvファイルを設定し、lyric.pyを実行します。<br>
サンプルを実行する場合の引数は以下の通りです。<br>
`../sample/lyric/lyric.exo　../sample/lyric/lyric.tsv`
3. `./output`配下に`lyric.exo`が出力されます。

### sing.py

キャラクターに口パクさせます。

1. sampleを参考にexoファイルを作成します。<br/>
その際、exoファイルを任意のテキストエディタで開き、画像のパスを相対表記に修正します。
2. 歌わせたい内容を母音 + 「ん」で一文字ずつ表記したものと表示時間を記述したtsvファイルを作成します。<br/>
時間はミリ秒で指定します。詳しくは`./sample/sing/sing.tsv`を参考にしてください。 
3. 第1引数にexoファイル、第2引数にtsvファイルを設定し、sing.pyを実行します。 <br>
サンプルを実行する場合の引数は以下の通りです。<br>
`../sample/sing/sing.exo　../sample/sing/sing.tsv`

### code.py

ハイライト表示されたコードの入力を再現します。<br/>
Node.js, highlight.jsの設定が済んでいる場合は手順3から実行します。

1. PCにNode.jsをインストールします。
2. `./script`配下で下記コマンドを実行します。<br/>
`npm install highlight.js`
3. `./script/syntaxHighlight.js`を開き、`{ language: 'python' }`を再現するコードの名前に変更します。<br/>
（例えばC#なら`{ language: 'csharp' }`と変更）
4. 第1引数にテンプレートとするテキストオブジェクトのみを配置したexoファイル、 <br/>
第2引数にコードが書かれたテキストファイルを設定し、code.pyを実行します。<br/>
サンプルを実行する場合の引数は以下の通りです。<br>
`../sample/code/code.exo　../sample/code/code.txt`
5. `./output`配下に`code.exo`が出力されます。かなり時間がかかります。

## ディレクトリ構成

`./sample` 各種サンプルが格納されています。sing.py用に立ち絵を同梱しています。<br/>
`./script` ハイライトを設定するための.jsファイルが格納されています。<br/>
`./src` 各種.pyファイルが格納されています。

## このスクリプトがしていること

AviUtlのexoファイルをリストと辞書のツリー構造に変換して読み込んで編集しています。<br/>
`./src/Util/exoUtil.py`にexoとツリー構造を相互に変換するメソッドがあります。<br/>
