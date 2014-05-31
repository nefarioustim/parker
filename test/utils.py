# -*- coding: utf-8 -*-
"""Module of utilities for testing."""

import urllib2


def is_online():
    """Return boolean representing online status."""
    try:
        # Ping google.co.uk IP
        urllib2.urlopen('http://173.194.41.191', timeout=1)
        return True
    except urllib2.URLError:
        pass

    return False
