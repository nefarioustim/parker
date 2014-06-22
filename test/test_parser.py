# -*- coding: utf-8 -*-
"""Test the Parser object."""

import pytest
from parker import page, parsedpage, parser
from test_client import client_fixture
from test_page import page_fixture


def test_parse_converts_page_into_parsedpage(page_fixture):
    """Test parser.parse converts a Page into a ParsedPage."""
    test_page = page_fixture
    test_parsedpage = parser.parse(test_page)
    expected_repr = "<class 'parker.parsedpage.ParsedPage'>(%s)" % (
        test_page.uri
    )

    assert isinstance(test_parsedpage, parsedpage.ParsedPage)
    assert test_parsedpage.__repr__() == expected_repr


def test_parse_throws_typeerror_wrong_input():
    """Test parser.parse throws a TypeError on the wrong input."""
    with pytest.raises(TypeError):
        test_parsedpage = parser.parse(None)
