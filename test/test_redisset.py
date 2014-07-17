# -*- coding: utf-8 -*-
"""Test the RedisSet object."""

import pytest
from parker import redisset

TEST_SET_KEY = "test-set"
TEST_HASH = "isolemnlyswearimuptonogood"


@pytest.fixture(scope="function")
def redisset_fixture():
    """Test fixture for RedisSet."""
    return redisset.get_instance(TEST_SET_KEY)


def test_get_instance_creates_crawlpage_object():
    """Test redisset.get_instance creates a RedisSet object."""
    test_set = redisset.get_instance(TEST_SET_KEY)
    expected_repr = "<class 'parker.redisset.RedisSet'>(%s)" % (
        TEST_SET_KEY
    )

    assert isinstance(test_set, redisset.RedisSet)
    assert test_set.__repr__() == expected_repr


def test_has_returns_true(redisset_fixture):
    """Test redisset.has returns something if key exists in set."""
    test_redisset = redisset_fixture

    test_redisset.redis.sadd(TEST_SET_KEY, TEST_HASH)

    assert test_redisset.has(TEST_HASH)

    test_redisset.redis.srem(TEST_SET_KEY, TEST_HASH)
