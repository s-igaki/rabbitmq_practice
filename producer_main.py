#!/usr/local/var/pyenv/shims/python3

import pika

def connectPika():
    # コネクション作成
    pika_param = pika.ConnectionParameters('0.0.0.0')
    connection = pika.BlockingConnection(pika_param)

    # チャンネル作成
    channel = connection.channel()

    # キューの作成
    channel.queue_declare(queue='hello')

    # メッセージの送信
    channel.basic_publish(exchange="", routing_key="hello", body="hello wolrd!")

    # コネクション終了
    connection.close()

def main():
    connectPika()


if __name__ == '__main__':
    main()