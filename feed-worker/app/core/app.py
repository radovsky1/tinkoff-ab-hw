import os
import asyncio
from fastapi import FastAPI

from .routers import init_routers
from ..amqp import Consumer


class App(FastAPI):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.consumer = Consumer(os.getenv("AMQP_URL"))


def create_app() -> FastAPI:
    app = App()
    init_routers(app)

    async def startup():
        loop = asyncio.get_running_loop()
        task = loop.create_task(app.consumer.consume(loop))
        await task

    app.add_event_handler("startup", startup)
    return app
