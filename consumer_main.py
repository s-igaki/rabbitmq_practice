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

    # コールバック関数の宣言
    def callback(ch, method, properties, body):
        print("{} is Received.".format(body))
        ch.basic_ack(delivery_tag=method.delivery_tag)

    channel.basic_consume(queue="hello", on_message_callback=callback)
    channel.start_consuming()

def main():
    connectPika()


if __name__ == '__main__':
    main()