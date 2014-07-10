# -*- coding: utf-8 -*-
"""Module of utilities for testing."""

import os
import urllib2

STUB_PATH = os.path.join(
    os.environ['PROJECT'],
    'test',
    'stubs'
)


def is_online():
    """Return boolean representing online status."""
    try:
        # Ping google.co.uk IP
        urllib2.urlopen('http://173.194.41.191', timeout=1)
        return True
    except urllib2.URLError:
        pass

    return False


def load_stub_as_string(filename):
    """Load a stub file."""
    filepath = os.path.join(
        STUB_PATH,
        filename
    )

    with open(filepath, "r") as myfile:
        return myfile.read()


def load_stub_as_iterable(filename):
    """Load a stub file as an iterable."""
    filepath = os.path.join(
        STUB_PATH,
        filename
    )

    return open(filepath, "r")
