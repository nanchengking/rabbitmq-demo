# demo for rabbit-mq in python
link from https://www.rabbitmq.com/tutorials/tutorial-one-python.html
#### 

### exchange

交换机的类型：

direct, topic, headers and fanout

但是可以默认不声明任何类型，类似于
```python
channel.basic_publish(exchange='',
                      routing_key='hello',
                      body=message)
```
这样的话，交换机就会把消息，投递到名字是routing_key的队列里面去。

申明一个扇形（fanout）交换机，会把消息扔到所有队列里面去
```python
channel.exchange_declare(exchange='logs',
                         exchange_type='fanout')
for i in range(0,10):
	channel.basic_publish(exchange="logs",
	routing_key="",
	body=i)
```


### Bindings

绑定规则，如下，声明一个绑定规则：

```python
channel.queue_bind(exchange=exchange_name,
                   queue=queue_name)
```
A binding is a relationship between an exchange and a queue. This can be simply read as: the queue is interested in messages from this exchange.
交换机和队列的绑定关系，就是一个绑定。比如fanout，如果没有声明队列，那么就相当于任何一个fanout类型的交换机所接收的消息，会被任何业务方的任何队列收到了。因为对于生产者，他只知道消息给了哪个交换机，不知道到了哪个队列~
不幸的是关于routing_key，fanout的交换机，如下操作
```python
channel.queue_bind(exchange=exchange_name,
                   queue=queue_name,
                   routing_key='black')
```
会直接忽略routing_key~，所以他只知道这个队列绑定了这个交换机。。。。
如果要使用routing_key进行路由，那么至少要使用direct的队列，因为它能支持。
We will use a direct exchange instead. The routing algorithm behind a direct exchange is simple - a message goes to the queues whose binding key exactly matches the routing key of the message.
