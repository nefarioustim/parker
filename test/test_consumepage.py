# -*- coding: utf-8 -*-
"""Test the ConsumePage object."""

from pyquery import PyQuery
from parker import parser, consumepage
from test_client import client_fixture
from test_page import page_fixture
from test_parsedpage import parsedpage_fixture
import utils

TEST_CONTENT = utils.load_stub_as_string('staples-stapler.html')
TEST_PARSED = PyQuery(TEST_CONTENT, parser='html')


def test_consumepage_get_instance_creates_consumepage_object(
    parsedpage_fixture
):
    """Test parsedpage.get_instance creates a ParsedPage object."""
    test_parsedpage = parsedpage_fixture
    test_consumepage = consumepage.get_instance(
        test_parsedpage
    )
    expected_repr = "<class 'parker.consumepage.ConsumePage'>(%s)" % (
        test_parsedpage.page.uri
    )

    assert isinstance(test_consumepage, consumepage.ConsumePage) is True
    assert test_consumepage.__repr__() == expected_repr