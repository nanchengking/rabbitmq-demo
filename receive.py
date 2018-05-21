import pika
import time

def callback(ch, method, properties, body):
    print(" [x] Received %r %s" % (body,time.time()))
    time.sleep(1)
    #ch.basic_ack(delivery_tag = method.delivery_tag)

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()
#channel.queue_declare(queue='hello')

#保证一条消息，在消费者没有ack之前，不会有新的消息过来
channel.basic_qos(prefetch_count=1)

channel.basic_consume(callback,
                      queue='task_queue',
                      no_ack=False)

print(' [*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()
