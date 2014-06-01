# -*- coding: utf-8 -*-
"""Page object for Parker."""

import client

_instances = dict()


def get_instance(uri):
    """Return an instance of Page."""
    try:
        instance = _instances(uri)
    except:
        page_client = client.get_instance()
        instance = Page(uri, page_client)
        _instances[uri] = instance

    return instance


class Page(object):

    """A downloaded Page."""

    def __init__(self, uri, client):
        """Constructor."""
        self.uri = uri
        self.client = client

    def __repr__(self):
        """Return an unambiguous representation."""
        return "%s(%s)" % (self.__class__, self.uri)
