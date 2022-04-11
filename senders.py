import pika


def sender(data):
    for input in data:
        if isinstance(input, str) == False or input == '':
            raise TypeError('Input must be string')
    if len(data) != 3:
        raise Exception('Not all data was entered')
    connection = pika.BlockingConnection(
        pika.ConnectionParameters(host='localhost'))
    channel = connection.channel()
    channel.queue_declare(queue=data[1])

    channel.basic_publish(
        exchange='', routing_key=data[1], body=data[2])
    print(" %s Sent 'Hello World!", data[0])
    connection.close()
    return 0
