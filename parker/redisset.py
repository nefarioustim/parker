# -*- coding: utf-8 -*-
"""RedisSet object for Parker."""

import redis
from configloader import load_config

_instances = dict()
_redis_config = load_config("redis")
_redis = redis.StrictRedis(**_redis_config)


def get_instance(key):
    """Return an instance of RedisSet."""
    try:
        instance = _instances[key]
    except KeyError:
        instance = RedisSet(
            key,
            _redis
        )
        _instances[key] = instance

    return instance


class RedisSet(object):

    """Wrapper object for Redis sets."""

    def __init__(self, key, redis):
        """Constructor."""
        self.key = key
        self.redis = redis

    def __repr__(self):
        """Return an unambiguous representation."""
        return "%s(%s)" % (self.__class__, self.key)

    def has(self, value):
        """Test set has value."""
        return self.redis.sismember(
            self.key,
            value
        )

    def add(self, value):
        """Add value to set."""
        return self.redis.sadd(
            self.key,
            value
        )

    def delete(self, value):
        """Delete key from set."""
        return self.redis.srem(
            self.key,
            value
        )

    def destroy(self):
        """Destroy the set."""
        return self.redis.delete(self.key)
