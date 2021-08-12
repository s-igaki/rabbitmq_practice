#!/usr/local/var/pyenv/shims/python3

import pika
import datetime
import json

def connectPika():
    # コネクション作成
    pika_param = pika.ConnectionParameters('0.0.0.0')
    connection = pika.BlockingConnection(pika_param)

    # チャンネル作成
    channel = connection.channel()

    # キューの作成
    channel.queue_declare(queue='hello')
    properties = pika.BasicProperties(content_type='application/json')

    # メッセージの送信
    dt_now = datetime.datetime.now()
    channel.basic_publish(exchange="", routing_key="hello", body=json.dumps({'title':"1hello wolrd {}!".format(dt_now)}), properties=properties)

    dt_now = datetime.datetime.now()
    channel.basic_publish(exchange="", routing_key="hello", body=json.dumps({'title':"2hello wolrd {}!".format(dt_now)}), properties=properties)

    dt_now = datetime.datetime.now()
    channel.basic_publish(exchange="", routing_key="hello", body=json.dumps({'title':"3hello wolrd {}!".format(dt_now)}), properties=properties)

    dt_now = datetime.datetime.now()
    channel.basic_publish(exchange="", routing_key="hello", body=json.dumps({'title':"4hello wolrd {}!".format(dt_now)}), properties=properties)

    dt_now = datetime.datetime.now()
    channel.basic_publish(exchange="", routing_key="hello", body=json.dumps({'title':"5hello wolrd {}!".format(dt_now)}), properties=properties)

    # コネクション終了
    connection.close()

def main():
    connectPika()


if __name__ == '__main__':
    main()