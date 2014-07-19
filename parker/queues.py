# -*- coding: utf-8 -*-
"""RQ queues for Parker."""

from rq import Queue
from redis import StrictRedis
from configloader import load_config

_redis_config = load_config('redis')

crawl_q = Queue(
    'crawl',
    connection=StrictRedis(
        **_redis_config
    )
)
consume_q = Queue(
    'consume',
    connection=StrictRedis(
        **_redis_config
    )
)
