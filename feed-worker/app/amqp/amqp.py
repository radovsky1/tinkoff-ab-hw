import pika
from aio_pika import connect_robust
from pika.exchange_type import ExchangeType

from ..domain import PostEvent
from ..usecase import PostInterface, PostUsecase


class Consumer:
    EXCHANGE = 'feed'
    QUEUE = 'feed-worker'

    def __init__(self, amqp_url, usecase: PostInterface = PostUsecase()):
        self._usecase = usecase
        params = pika.URLParameters(amqp_url)
        self._host = params.host
        self._port = params.port
        self._connection = pika.BlockingConnection(params)
        self._channel = self._connection.channel()
        self._channel.exchange_declare(
            exchange=self.EXCHANGE, exchange_type=ExchangeType.direct
        )
        self._channel.queue_declare(queue=self.QUEUE)
        self._channel.queue_bind(
            queue=self.QUEUE, exchange=self.EXCHANGE, routing_key=self.QUEUE
        )

    async def on_message(self, message):
        post_event = PostEvent.from_json(message.body)
        await self._usecase.handle_post(post_event)

    async def consume(self, loop):
        connection = await connect_robust(
            host=self._host, port=self._port, loop=loop
        )
        channel = await connection.channel()
        queue = await channel.declare_queue(self.QUEUE)
        await queue.consume(self.on_message)
        return connection
