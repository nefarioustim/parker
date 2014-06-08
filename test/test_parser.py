# -*- coding: utf-8 -*-
"""Test the Parser object."""

from parker import page, parsedpage, parser
from test_client import client_fixture
from test_page import page_fixture


def test_parser_parse_converts_page_into_parsedpage(page_fixture):
    """Test parser.parse converts a Page into a ParsedPage."""
    test_page = page_fixture

    test_parsed_page = parser.parse(test_page)

    assert isinstance(test_parsed_page, parsedpage.ParsedPage) is True
