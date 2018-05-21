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

