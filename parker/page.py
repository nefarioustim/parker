# -*- coding: utf-8 -*-
"""Page object for Parker."""

import client

_instances = dict()


def get_instance(uri, page_client=None):
    """Return an instance of Page."""
    try:
        instance = _instances[uri]
    except KeyError:
        if not page_client:
            page_client = client.get_instance()

        instance = Page(uri, page_client)
        _instances[uri] = instance
    else:
        if page_client:
            instance.client = page_client

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
