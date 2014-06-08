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

    def get_nodes_by_selector(self, selector, not_selector=None):
        """Return a collection of filtered nodes.

        Filtered based on the @selector and @not_selector parameters.
        """
        nodes = self.parsed(selector)

        if not_selector is not None:
            nodes = nodes.not_(not_selector)

        return nodes
