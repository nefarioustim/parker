# -*- coding: utf-8 -*-
"""Test the ParsedPage object."""

from pyquery import PyQuery
from parker import parsedpage
from test_client import client_fixture
from test_page import page_fixture
import utils

TEST_CONTENT = utils.load_stub_as_string('staples-stapler.html')
TEST_PARSED = PyQuery(TEST_CONTENT, parser='html')


def test_parsedpage_get_instance_creates_parsedpage_object(page_fixture):
    """Test parsedpage.get_instance creates a ParsedPage object."""
    test_page = page_fixture
    test_parsedpage = parsedpage.get_instance(
        test_page,
        TEST_CONTENT,
        TEST_PARSED
    )
    expected_repr = "<class 'parker.parsedpage.ParsedPage'>(%s)" % (
        test_page.uri
    )

    assert isinstance(test_parsedpage, parsedpage.ParsedPage) is True
    assert test_parsedpage.__repr__() == expected_repr
