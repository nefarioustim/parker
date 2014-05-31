# -*- coding: utf-8 -*-
"""HTTP client for Parker."""

import random
from .configloader import load_config

_instances = dict()


def get_instance():
    """Return an instance of Client."""
    config = load_config('client')
    user_agent = config['user-agents'][
        random.randint(0, len(config['user-agents']) - 1)
    ]

    try:
        instance = _instances(user_agent)
    except:
        instance = Client(user_agent)
        _instances[user_agent] = instance

    return instance


class Client(object):

    """HTTP client object."""

    headers = {
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,\
            image/webp,*/*;q=0.8',
        'accept-encoding': 'gzip,deflate,sdch',
        'accept-language': 'en-GB,en-US;q=0.8,en;q=0.6',
        'cache-control': 'no-cache',
        'connection': 'keep-alive',
        'pragma': 'no-cache'
    }

    def __init__(self, user_agent):
        """Constructor."""
        self.headers["user_agent"] = user_agent

    def __repr__(self):
        """Return an unambiguous representation."""
        return "%s(%s)" % (self.__class__, self.headers["user_agent"])
