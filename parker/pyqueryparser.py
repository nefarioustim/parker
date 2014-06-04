# -*- coding: utf-8 -*-
"""Module for parsing pages into PyQuery parses."""

_instance = None


def get_instance():
    """Return an instance of PyQueryParser."""
    if _instance:
        instance = _instance
    else:
        instance = PyQueryParser()

    return instance


class PyQueryParser(object):

    """A parser to turn pages into PyQuery parses."""
