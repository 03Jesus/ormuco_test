from collections import OrderedDict
from datetime import datetime, timedelta


class GeoDistributedLRUCache:
    """
    A class that represents a geo-distributed LRU cache.
    """

    def __init__(self,
                 capacity: int,
                 expiration_time: int):
        self.capacity = capacity
        self.expiration_time = expiration_time
        self.cache = OrderedDict()
        """
        Constructor of the class
        :param capacity: The capacity of the cache
        :type capacity: int
        :param expiration_time: The expiration time of the cache
        :type expiration_time: int
        """

    @property
    def capacity(self) -> int:
        """
        Gets the capacity of the cache
        :return: The capacity of the cache
        :rtype: int
        """
        return self._capacity

    @capacity.setter
    def capacity(self, capacity: int):
        """
        Sets the capacity of the cache
        :param capacity: The capacity of the cache
        :type capacity: int
        """
        self._capacity = capacity

    @property
    def expiration_time(self) -> int:
        """
        Gets the expiration time of the cache
        :return: The expiration time of the cache
        :rtype: int
        """
        return self._expiration_time

    @expiration_time.setter
    def expiration_time(self, expiration_time: int):
        """
        Sets the expiration time of the cache
        :param expiration_time: The expiration time of the cache
        :type expiration_time: int
        """
        self._expiration_time = expiration_time

    @property
    def cache(self) -> OrderedDict:
        """
        Gets the cache
        :return: The cache
        :rtype: OrderedDict
        """
        return self._cache

    @cache.setter
    def cache(self, cache: OrderedDict):
        """
        Sets the cache
        :param cache: The cache
        :type cache: OrderedDict
        """
        self._cache = cache

    def __getitem__(self, key: str):
        """
        Gets the value of the key in the cache
        :param key: The key
        :type key: str
        :return: The value of the key in the cache
        :rtype: str
        """
        if key in self.cache:
            value = self.cache.pop(key)
            self.cache[key] = (value[0], datetime.now())
            return value[0]
        return None

    def __setitem__(self, key: str, value: str):
        """
        Sets the value of the key in the cache
        :param key: The key
        :type key: str
        :param value: The value
        :type value: str
        """
        if len(self.cache) >= self.capacity:
            self.cache.popitem(last=False)

        self.cache[key] = (value, datetime.now())

    def __delitem__(self, key: str):
        """
        Deletes the key in the cache
        :param key: The key
        :type key: str
        """
        if key in self.cache:
            self.cache.pop(key)

    def __contains__(self, key: str) -> bool:
        """
        Checks if the key is in the cache
        :param key: The key
        :type key: str
        :return: True if the key is in the cache, False otherwise
        :rtype: bool
        """
        return key in self.cache

    def __len__(self) -> int:
        """
        Gets the length of the cache
        :return: The length of the cache
        :rtype: int
        """
        return len(self.cache)

    def __repr__(self) -> str:
        """
        Gets the string representation of the cache
        :return: The string representation of the cache
        :rtype: str
        """
        return str(self.cache)

    def clean_expired_data(self):
        """
        Cleans the expired data in the cache
        """
        for key, value in self.cache.items():
            if datetime.now() - value[1] > timedelta(seconds=self.expiration_time):
                self.cache.pop(key)
