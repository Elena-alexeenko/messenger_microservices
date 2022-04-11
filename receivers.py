import pika
import sys
import os
import time


def receiverStartListening(name):
    connection = pika.BlockingConnection(
        pika.ConnectionParameters(host='localhost'))

    channel = connection.channel()
   # channel.queue_bind(queue=name)

    def callback(ch, method, properties, body):
        print(" [x] Received %r" % body.decode())
        time.sleep(body.count(b'.'))
        ch.basic_ack(delivery_tag=method.delivery_tag)

    channel.basic_consume(
        queue=name, on_message_callback=callback)

    print(' [*] Waiting for messages. To exit press CTRL+C')
    channel.start_consuming()


def callback(ch, method, properties, body):
    print(" [x] Received %r" % body.decode())


def main(receiver):
    try:
        if str(receiver):
            try:
                receiverStartListening(receiver)
            except KeyboardInterrupt:
                print('Interrupted')
                try:
                    sys.exit(0)
                except SystemExit:
                    os._exit(0)
    except ValueError:
        if not receiver:
            raise ValueError('empty string')
        else:
            raise ValueError('not str')
