import redis

class RedisClient:
    def __init__(self, host='localhost', port=6379, db=0):
        self.connection = redis.Redis(host=host, port=port, db=db)

    def insert(self, key, value):
        self.connection.set(key, value)

    def retrieve(self, key):
        return self.connection.get(key)