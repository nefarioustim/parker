# -*- coding: utf-8 -*-
"""ParsedPage object for Parker."""

_instances = dict()


def get_instance(uri):
    """Return an instance of ParsedPage."""
    try:
        instance = _instances[uri]
    except KeyError:
        instance = ParsedPage(uri)
        _instances[uri] = instance

    return instance


class ParsedPage(object):

    """A ParsedPage."""

    def __init__(self, uri):
        """Constructor."""
        self.uri = uri

    def __repr__(self):
        """Return an unambiguous representation."""
        return "%s(%s)" % (self.__class__, self.uri)
