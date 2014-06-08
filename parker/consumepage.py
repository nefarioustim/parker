# -*- coding: utf-8 -*-
"""ConsumePage object for Parker."""

from parsedpage import ParsedPage

_instances = dict()


def get_instance(parsedpage):
    """Return an instance of ConsumePage."""
    try:
        instance = _instances[parsedpage.page.uri]
    except KeyError:
        instance = ConsumePage(parsedpage)
        _instances[parsedpage.page.uri] = instance

    return instance


class ConsumePage(ParsedPage):

    """A ConsumePage."""

    def __init__(self, parsedpage):
        """Constructor."""
        self.parsedpage = parsedpage

    def __repr__(self):
        """Return an unambiguous representation."""
        return "%s(%s)" % (self.__class__, self.parsedpage.page.uri)
