# -*- coding: utf-8 -*-
"""Consumer object for consuming pages in Parker."""

_instance = None


def get_instance():
    """Return an instance of Consumer."""
    _instance = _instance or Consumer()

    return _instance


class Consumer(object):

    """Consumer consumes pages."""
