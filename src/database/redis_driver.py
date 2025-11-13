# src/database/redis_driver.py

import redis
from src.config import REDIS_HOST, REDIS_PORT, REDIS_DB

class RedisDriver:
    def __init__(self):
        self.host = REDIS_HOST
        self.port = REDIS_PORT
        self.db = REDIS_DB
        self.connection = None

    def connect(self):
        try:
            self.connection = redis.Redis(
                host=self.host,
                port=self.port,
                db=self.db,
                decode_responses=True # Decode responses to strings
            )
            self.connection.ping() # Test connection
            print(f"Successfully connected to Redis at {self.host}:{self.port}/{self.db}")
            return self.connection
        except redis.exceptions.ConnectionError as e:
            print(f"Error connecting to Redis: {e}")
            return None

    def disconnect(self):
        if self.connection:
            self.connection.close()
            print("Redis connection closed.")

    def set_data(self, key: str, value: str, ex: int = None):
        """
        Set a key-value pair in Redis.
        :param key: The key to set.
        :param value: The value to store.
        :param ex: Expiration time in seconds.
        """
        if not self.connection:
            print("Redis not connected.")
            return False
        try:
            self.connection.set(key, value, ex=ex)
            return True
        except Exception as e:
            print(f"Error setting data in Redis: {e}")
            return False

    def get_data(self, key: str):
        """
        Get data from Redis by key.
        :param key: The key to retrieve.
        """
        if not self.connection:
            print("Redis not connected.")
            return None
        try:
            return self.connection.get(key)
        except Exception as e:
            print(f"Error getting data from Redis: {e}")
            return None

    def delete_data(self, key: str):
        """
        Delete data from Redis by key.
        :param key: The key to delete.
        """
        if not self.connection:
            print("Redis not connected.")
            return False
        try:
            self.connection.delete(key)
            return True
        except Exception as e:
            print(f"Error deleting data from Redis: {e}")
            return False

# Example usage (for testing purposes)
if __name__ == "__main__":
    redis_driver = RedisDriver()
    connection = redis_driver.connect()

    if connection:
        # Example: Set data
        print("Setting 'mykey' to 'myvalue' with 60s expiration.")
        redis_driver.set_data("mykey", "myvalue", ex=60)

        # Example: Get data
        value = redis_driver.get_data("mykey")
        print(f"Value for 'mykey': {value}")

        # Example: Delete data
        print("Deleting 'mykey'.")
        redis_data.delete_data("mykey")
        value = redis_driver.get_data("mykey")
        print(f"Value for 'mykey' after deletion: {value}")

        redis_driver.disconnect()
