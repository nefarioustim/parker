# -*- coding: utf-8 -*-
"""Test the ParsedPage object."""

from parker import parsedpage

TEST_URI = "http://www.staples.co.uk/full-strip-stapler/cbs/412852.html"


def test_parsedpage_get_instance_creates_parsedpage_object():
    """Test parsedpage.get_instance creates a ParsedPage object."""
    test_parsedpage = parsedpage.get_instance(TEST_URI)
    expected_repr = "<class 'parker.parsedpage.ParsedPage'>(%s)" % (
        TEST_URI
    )

    assert isinstance(test_parsedpage, parsedpage.ParsedPage) is True
    assert test_parsedpage.__repr__() == expected_repr
