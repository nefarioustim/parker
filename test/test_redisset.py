# -*- coding: utf-8 -*-
"""Test the RedisSet object."""

from parker import redisset

TEST_SET_KEY = "test-set"


def test_get_instance_creates_crawlpage_object():
    """Test redisset.get_instance creates a RedisSet object."""
    test_set = redisset.get_instance(TEST_SET_KEY)
    expected_repr = "<class 'parker.redisset.RedisSet'>(%s)" % (
        TEST_SET_KEY
    )

    assert isinstance(test_set, redisset.RedisSet)
    assert test_set.__repr__() == expected_repr
