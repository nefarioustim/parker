# -*- coding: utf-8 -*-
"""Test the Page object."""

from parker import page

TEST_URI = "http://www.staples.co.uk/full-strip-stapler/cbs/412852.html"


def test_page_creation():
    """Test page.get_instance creates a Page object."""
    test_page = page.get_instance(TEST_URI)
    expected_repr = "<class 'parker.page.Page'>(%s)" % (
        TEST_URI
    )

    assert isinstance(test_page, page.Page) is True
    assert test_page.__repr__() == expected_repr
