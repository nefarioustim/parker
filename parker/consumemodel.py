# -*- coding: utf-8 -*-
"""Model object for consumed pages in Parker."""

_instances = dict()


def get_instance(uri):
    """Return an instance of ConsumeModel."""
    try:
        instance = _instances[uri]
    except KeyError:
        instance = ConsumeModel()
        _instances[uri] = instance

    return instance


class ConsumeModel(object):

    """Model representing a consumed page."""

    def __init__(self):
        """Constructor."""
