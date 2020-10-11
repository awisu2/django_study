# django study

- [01_install](READMES/01_install.md)
- [02_migrate](READMES/02_migrate.md)
- [03_admin](READMES/03_admin.md)

## install

- python3 以上
- vscode 推奨
- windows の場合
  - bash 系のターミナルを前提としています。(Git Bash で十分)
- bin/util で、各種コマンド入力の自動化をしています
  - 一度 `bin/util` を実行してみてください
  - 実行時にどんなコマンドが実行されているかはなるべく出力するようにしています

## 参考 links

- [はじめての Django アプリ作成、その 1 \| Django ドキュメント \| Django](https://docs.djangoproject.com/ja/3.0/intro/tutorial01/)

## 1. 初期設定

`bin/util setup`

- venv の作成
- Django や必要パッケージのインストール

## 2. project の作成

`bin/util create_project django_study`

- プロジェクトの作成
- 新しいプロジェクトは新規ディレクトリで作成される
- django_study の部分はプロジェクト名、好きな名前をどうぞ

### 特殊処理：本番プロジェクトではは不要

`mv django_study _tmp && mv -f _tmp/* ./ && rm -rf _tmp`

この勉強ではパスがずれると進めずらいので無理やり中身を移動

## 3. サーバ起動

`bin/util start`

http://127.0.0.1:8000/

### 4. アプリケーションの作成

実際の機能を持ったコードを書く場所を作成します
※ ここまでで作成したのはプロジェクト(機能の枠組み)で中身が空のためこの作業が必要です

`bin/util start_app task`
