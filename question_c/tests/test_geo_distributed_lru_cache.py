import pytest
from time import sleep

from question_c.geo_distributed_lru_cache import GeoDistributedLRUCache


@pytest.fixture
def cache():
    return GeoDistributedLRUCache(capacity=3, expiration_time=10)


def test_cache_get_set_delete(cache):
    cache['key1'] = 'value1'
    assert cache['key1'] == 'value1'

    cache['key2'] = 'value2'
    assert cache['key2'] == 'value2'

    del cache['key1']
    assert 'key1' not in cache


def test_cache_capacity(cache):
    cache['key1'] = 'value1'
    cache['key2'] = 'value2'
    cache['key3'] = 'value3'

    cache['key4'] = 'value4'
    assert 'key1' not in cache


def test_cache_expiration(cache):
    cache['key1'] = 'value1'
    cache['key2'] = 'value2'

    sleep(11)
    cache.clean_expired_data()

    assert 'key1' not in cache
    assert 'key2' not in cache


def test_cache_clean_expired_data(cache):
    cache['key1'] = 'value1'
    cache['key2'] = 'value2'

    sleep(11)

    cache.clean_expired_data()

    assert 'key1' not in cache
    assert 'key2' not in cache


def test_cache_len(cache):
    cache['key1'] = 'value1'
    cache['key2'] = 'value2'
    assert len(cache) == 2

    del cache['key1']
    assert len(cache) == 1

    sleep(11)
    cache.clean_expired_data()
    assert len(cache) == 0


def test_cache_contains(cache):
    cache['key1'] = 'value1'
    assert 'key1' in cache

    del cache['key1']
    assert 'key1' not in cache
