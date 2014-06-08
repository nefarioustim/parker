# -*- coding: utf-8 -*-
"""ParsedPage object for Parker."""

_instances = dict()


def get_instance(page, original, parsed):
    """Return an instance of ParsedPage."""
    try:
        instance = _instances[page.uri]
    except KeyError:
        instance = ParsedPage(page, original, parsed)
        _instances[page.uri] = instance

    return instance


class ParsedPage(object):

    """A ParsedPage."""

    def __init__(self, page, original, parsed):
        """Constructor."""
        self.page = page
        self.original = original
        self.parsed = parsed

    def __repr__(self):
        """Return an unambiguous representation."""
        return "%s(%s)" % (self.__class__, self.page.uri)
