import pika
from pika.exchange_type import ExchangeType

from ..domain import PostEvent


class Producer:
    EXCHANGE = 'feed'
    QUEUE = 'feed-worker'

    def __init__(self, amqp_url):
        params = pika.URLParameters(amqp_url)
        params.socket_timeout = 5
        self._connection = pika.BlockingConnection(params)
        self._channel = self._connection.channel()
        self._channel.exchange_declare(
            exchange=self.EXCHANGE, exchange_type=ExchangeType.direct
        )
        self._channel.queue_declare(queue=self.QUEUE)
        self._channel.queue_bind(
            queue=self.QUEUE, exchange=self.EXCHANGE, routing_key=self.QUEUE
        )

    def publish(self, post_event: PostEvent):
        self._channel.basic_publish(
            exchange=self.EXCHANGE,
            routing_key=self.QUEUE,
            body=post_event.to_json(),
        )

    def close(self):
        self._connection.close()
