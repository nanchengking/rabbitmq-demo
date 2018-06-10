import pika

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()
channel.exchange_declare(exchange='logs',
                         exchange_type='fanout')
channel.queue_declare(queue='task_queue', durable=True)
# for i in range(0,20):
# 	channel.basic_publish(exchange='logs',
#                       routing_key='task_queue',
#                       body='Hello World!'+str(i),
#                       properties=pika.BasicProperties(
#                          delivery_mode = 2, # make message persistent
#                       ))
for i in range(0, 10):
    channel.basic_publish(exchange="logs",
                          routing_key="",
                          body="message number:" + str(i))
print(" [x] Sent 'Hello World!'")
connection.close()
