# Rabbit MQの勉強用リポジトリ

## 概要

## 前提条件
以下がインストール済み
python3
pip3
docker

## 利用手順

```
pip3 inlstall pika
docker-compose up -d
```
以下のURLにアクセスするとRabbitMQの管理画面が見られます。
guest/guest
でログインしてみてください。

メッセージの作成は以下のコマンドを叩きます。
```
pytho3 ./producer_main.py
```
このタイミングで管理画面のQueueを参照すると、作成されていることが確認できます。
メッセージの受信は以下のコマンドを叩きます。
```
pytho3 ./consumer_main.py
```