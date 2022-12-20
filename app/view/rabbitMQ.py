import pika
class RabbitMQClient:
    def __init__(self, host='localhost'):
        self.host = host
        self.connection = None
        self.channel = None
        self.consumer_tags = {}  # Adicionei o dicionário consumer_tags para armazenar os consumer tags

    def connect(self):
        self.connection = pika.BlockingConnection(
            pika.ConnectionParameters(host=self.host)
        )
        self.channel = self.connection.channel()

    def close_connection(self):
        self.connection.close()

    def send_message(self, exchange, routing_key, body):
        routing_key = str(routing_key)  # converter routing_key para uma string
        self.channel.basic_publish(
            exchange=exchange,
            routing_key=routing_key,
            body=body
        )

    def cancel_consumer(self, consumer_tag):
        self.channel.basic_cancel(consumer_tag)
        del self.consumer_tags[consumer_tag]  # Removo o consumer tag do dicionário