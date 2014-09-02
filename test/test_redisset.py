# -*- coding: utf-8 -*-
"""Test the RedisSet object."""

import time
import pytest
from parker import redisset

TEST_SET_KEY = "test-set"
TEST_HASH = "isolemnlyswearimuptonogood"


@pytest.fixture(scope="function")
def redisset_fixture():
    """Test fixture for RedisSet."""
    return redisset.get_instance(TEST_SET_KEY)


def test_get_instance_creates_redisset_object():
    """Test redisset.get_instance creates a RedisSet object."""
    test_set = redisset.get_instance(TEST_SET_KEY)
    expected_repr = "<class 'parker.redisset.RedisSet'>(%s)" % (
        TEST_SET_KEY
    )

    assert isinstance(test_set, redisset.RedisSet)
    assert test_set.__repr__() == expected_repr


def test_has_returns_true_if_key_exists(redisset_fixture):
    """Test redisset.has returns something if key exists in set."""
    test_redisset = redisset_fixture

    test_redisset.redis.sadd(TEST_SET_KEY, TEST_HASH)

    assert test_redisset.has(TEST_HASH)

    test_redisset.redis.srem(TEST_SET_KEY, TEST_HASH)


def test_has_returns_false_if_key_does_not_exist(redisset_fixture):
    """Test redisset.has returns false if key does not exist in set."""
    test_redisset = redisset_fixture

    assert not test_redisset.has(TEST_HASH)


def test_add_adds_value_to_set(redisset_fixture):
    """Test redisset.add adds value to the set."""
    test_redisset = redisset_fixture

    assert not test_redisset.has(TEST_HASH)

    test_redisset.add(TEST_HASH)

    assert test_redisset.has(TEST_HASH)

    test_redisset.redis.srem(TEST_SET_KEY, TEST_HASH)


def test_delete_removes_value_from_set(redisset_fixture):
    """Test redisset.delete removes value from the set."""
    test_redisset = redisset_fixture

    test_redisset.add(TEST_HASH)

    assert test_redisset.has(TEST_HASH)

    test_redisset.delete(TEST_HASH)

    assert not test_redisset.has(TEST_HASH)


def test_destroy_destroys_the_set(redisset_fixture):
    """Test redisset.destroy destroys the redisset."""
    test_redisset = redisset_fixture
    test_redisset.add(TEST_HASH)

    test_redisset.destroy()

    assert not test_redisset.has(TEST_HASH)
    assert not test_redisset.redis.exists(TEST_SET_KEY)


def test_ttl_returns_ttl_of_set(redisset_fixture):
    """Test redisset.ttl returns TTL of the set."""
    test_redisset = redisset_fixture
    test_redisset.add(TEST_HASH)
    ttl = test_redisset.ttl()

    assert ttl > (432000 - 60)

    test_redisset.destroy()


def test_ttl_drops_regardless_of_adds(redisset_fixture):
    """Test the redisset.ttl continues falling despite adds."""
    test_redisset = redisset_fixture
    test_redisset.add('foo')
    orig_ttl = test_redisset.ttl()

    time.sleep(1)
    test_redisset.add('bar')
    ttl = test_redisset.ttl()

    assert ttl < orig_ttl

    test_redisset.destroy()
