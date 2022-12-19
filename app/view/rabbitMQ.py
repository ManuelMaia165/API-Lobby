import pika

class RabbitMQClient:
    def __init__(self, host='localhost'):
        self.host = host
        self.connection = None
        self.channel = None

    def connect(self):
        self.connection = pika.BlockingConnection(
            pika.ConnectionParameters(host=self.host)
        )
        self.channel = self.connection.channel()

    def close_connection(self):
        self.connection.close()

    def send_message(self, exchange, routing_key, body):
        self.channel.exchange_declare(exchange=exchange, exchange_type='topic')
        self.channel.basic_publish(
            exchange=exchange,
            routing_key=routing_key,
            body=body
        )

rabbitmq_client = RabbitMQClient()