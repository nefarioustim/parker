# -*- coding: utf-8 -*-
"""RedisSet object for Parker."""

import redis
from configloader import load_config

_instances = dict()
_redis_config = load_config("redis")
_redis = redis.StrictRedis(**_redis_config)
_seconds_in_a_day = 60 * 60 * 24
_seconds_in_five_days = 5 * _seconds_in_a_day


def get_instance(key):
    """Return an instance of RedisSet."""
    global _instances
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

    def __init__(self, key, redis, expire=_seconds_in_five_days):
        """Constructor."""
        self.key = key
        self.redis = redis
        self.expire = expire

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
        added = self.redis.sadd(
            self.key,
            value
        )

        if self.redis.scard(self.key) < 2:
            self.redis.expire(self.key, self.expire)

        return added

    def delete(self, value):
        """Delete key from set."""
        return self.redis.srem(
            self.key,
            value
        )

    def destroy(self):
        """Destroy the set."""
        return self.redis.delete(self.key)

    def ttl(self):
        """Return the TTL for the set."""
        return self.redis.ttl(self.key)
