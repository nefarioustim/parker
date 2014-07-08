# -*- coding: utf-8 -*-
"""MediaFile object for Parker."""

import client

_instances = dict()


def get_instance(uri):
    """Return an instance of MediaFile."""
    try:
        instance = _instances[uri]
    except KeyError:
        instance = MediaFile(
            uri,
            client.get_instance()
        )
        _instances[uri] = instance

    return instance


class MediaFile(object):

    """A MediaFile, as fetched from a client."""

    def __init__(self, uri, client):
        """Constructor."""
        self.uri = uri
        self.client = client

    def __repr__(self):
        """Return an unambiguous representation."""
        return "%s(%s)" % (self.__class__, self.uri)
