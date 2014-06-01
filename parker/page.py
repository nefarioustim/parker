# -*- coding: utf-8 -*-
"""Page object for Parker."""

_instances = dict()


def get_instance(uri):
    """Return an instance of Page."""
    try:
        instance = _instances(uri)
    except:
        instance = Page(uri)
        _instances[uri] = instance

    return instance


class Page(object):

    """A downloaded Page."""

    def __init__(self, uri):
        """Constructor."""
        self.uri = uri
