# -*- coding: utf-8 -*-
"""Page object for Parker."""

import client

_instances = dict()


def get_instance(uri):
    """Return an instance of Page."""
    try:
        instance = _instances[uri]
    except KeyError:
        instance = Page(
            uri,
            client.get_instance()
        )
        _instances[uri] = instance

    return instance


class Page(object):

    """A Page, as fetched from a client."""

    def __init__(self, uri, client):
        """Constructor."""
        self.uri = uri
        self.client = client
        self.content = None

    def __repr__(self):
        """Return an unambiguous representation."""
        return "%s(%s)" % (self.__class__, self.uri)

    def fetch(self):
        """Fetch Page.content from client."""
        self.content = self.client.get_content(
            uri=self.uri
        )
