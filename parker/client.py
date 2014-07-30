# -*- coding: utf-8 -*-
"""HTTP client for Parker."""

import random
import requests
from configloader import load_config

DEFAULT_UA = "Parker v0.1.0"
_PERMITTED_STATUS_CODES = [200]
_instances = dict()


def get_instance():
    """Return an instance of Client."""
    config = load_config('client')
    user_agents = config['user-agents']
    proxies = config['proxies']

    user_agent = user_agents[
        random.randint(0, len(user_agents) - 1)
    ] if len(user_agents) > 0 else DEFAULT_UA

    proxy = proxies[
        random.randint(0, len(proxies) - 1)
    ] if len(proxies) > 0 else None

    try:
        instance = _instances[user_agent]
    except KeyError:
        instance = Client(user_agent, proxy)
        _instances[user_agent] = instance

    return instance


class Client(object):

    """HTTP client object."""

    headers = {
        'accept': (
            'text/html,application/xhtml+xml,application/xml;'
            'q=0.9,image/webp,*/*;q=0.8'
        ),
        'accept-encoding': 'gzip,deflate,sdch',
        'accept-language': 'en-GB,en-US;q=0.8,en;q=0.6',
        'cache-control': 'no-cache',
        'connection': 'keep-alive',
        'pragma': 'no-cache'
    }

    def __init__(self, user_agent, proxy=False):
        """Constructor."""
        self.headers["user_agent"] = user_agent
        self.proxy = proxy
        self.response_headers = None

    def __repr__(self):
        """Return an unambiguous representation."""
        return "%s(%s)" % (self.__class__, self.headers["user_agent"])

    def get(self, uri, disable_proxy=False, stream=False):
        """Return Requests response to GET request."""
        proxy = self.proxy if not disable_proxy else False

        response = requests.get(
            uri,
            headers=self.headers,
            allow_redirects=True,
            cookies={},
            stream=stream,
            proxies=proxy
        )

        if response.status_code in _PERMITTED_STATUS_CODES:
            self.response_headers = response.headers
            return response.content if not stream else response.iter_content()
        else:
            raise requests.exceptions.HTTPError(
                "HTTP response did not have a permitted status code."
            )

    def get_content(self, uri, disable_proxy=False):
        """Return content from URI if Response status is good."""
        return self.get(uri=uri, disable_proxy=disable_proxy)

    def get_iter_content(self, uri, disable_proxy=False):
        """Return iterable content from URI if Response status is good."""
        return self.get(uri=uri, disable_proxy=disable_proxy, stream=True)
