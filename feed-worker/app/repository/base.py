import redis


class RwRedisRepository:
    def __init__(self, host, port):
        self._redis = redis.Redis(host=host, port=port)

    async def get(self, key):
        return self._redis.get(key)

    async def set(self, key, value):
        return self._redis.set(key, value)


rw = RwRedisRepository(host='redis', port=6379)
