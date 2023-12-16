import unittest
from server_shared import RedisClient  # Assuming your class is in redis_client.py

class TestRedisClient(unittest.TestCase):
    def setUp(self):
        self.client = RedisClient()
        self.test_key = "new key"
        self.test_value = "new value"

    def test_insert_retrieve(self):
        print('testing redis insert')
        self.client.insert(self.test_key, self.test_value)
        result = self.client.retrieve(self.test_key)
        print(f'retrieving value for key {self.test_key} value {result}')
        self.assertEqual(result, self.test_value.encode())

if __name__ == '__main__':
    unittest.main()
