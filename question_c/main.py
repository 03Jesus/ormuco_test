import time
from geo_distributed_lru_cache import GeoDistributedLRUCache

if __name__ == '__main__':
    cache = GeoDistributedLRUCache(capacity=3, expiration_time=10)

    cache['key1'] = 'value1'
    cache['key2'] = 'value2'
    cache['key3'] = 'value3'
    print("\nCache state: ", cache.cache)

    print(cache['key1'])
    print("\nCache state: ", cache.cache)

    cache['key4'] = 'value4'

    print("\nCache actual state: ", cache.cache)
    print("Cleaning data...\n")
    time.sleep(11)
    cache.clean_expired_data()
    print("\nCache actual state: ", cache.cache)
