# -*- coding: utf-8 -*-
"""Test the ConsumePage object."""

import pytest
from pyquery import PyQuery
from parker import parser, consumepage
from test_client import client_fixture
from test_page import page_fixture
from test_parsedpage import parsedpage_fixture
import utils

TEST_SELECTOR = "h1"
TEST_REGEX = r"(\w+)"
TEST_KEY_SELECTOR = "#divSpecifications dd .l"
TEST_VALUE_SELECTOR = "#divSpecifications dd .r"
TEST_CRUMB_SELECTOR = "#skuBreadCrumbs span[itemprop=title]"
EXPECTED_VALUE = "Staples Full Strip Stapler"
EXPECTED_FILTERED_VALUE = "Staples"
EXPECTED_KV_DICT = {
    u'Staple Compatibility :': u'26/06/2014',
    u'Brands :': u'Staples',
    u'Stapling Capacity (sheets) :': u'20 sheets',
    u'Colour :': u'Black',
    u'Quantity :': u'1'
}
EXPECTED_CRUMB_LIST = [
    u'Pens | Tape | Desk Supplies',
    u'Desktop Stationery | Clips | Accessories',
    u'Staplers'
]


@pytest.fixture(scope="function")
def consumepage_fixture(parsedpage_fixture):
    """Test fixture to ensure correct mocking for parsedpage."""
    test_parsedpage = parsedpage_fixture
    return consumepage.get_instance(
        test_parsedpage
    )


def test_get_instance_creates_consumepage_object(
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


def test_get_filtered_data_by_selector_returns_expected_value_of_h1(
    consumepage_fixture
):
    """Test consumepage.get_filtered_data_by_selector.

    Ensure returns the expected value of the H1.
    """
    test_consumepage = consumepage_fixture
    actual_value = test_consumepage.get_filtered_data_by_selector(
        TEST_SELECTOR
    )

    assert actual_value == EXPECTED_VALUE


def test_get_filtered_data_by_selector_returns_expected_filtered_value_of_h1(
    consumepage_fixture
):
    """Test consumepage.get_filtered_data_by_selector.

    Ensure returns the expected value of the H1 filtered by regex.
    """
    test_consumepage = consumepage_fixture
    actual_value = test_consumepage.get_filtered_data_by_selector(
        TEST_SELECTOR,
        regex=TEST_REGEX
    )

    assert actual_value == EXPECTED_FILTERED_VALUE


def test_get_key_value_data_by_selectors_returns_expected_dict(
    consumepage_fixture
):
    """Test consumepage.get_key_value_data_by_selectors.

    Ensure returns the expected dictionary of data.
    """
    test_consumepage = consumepage_fixture
    key_value_dict = test_consumepage.get_key_value_data_by_selectors(
        TEST_KEY_SELECTOR,
        TEST_VALUE_SELECTOR
    )

    assert key_value_dict == EXPECTED_KV_DICT


def test_get_crumb_list_by_selector_returns_expected_list(
    consumepage_fixture
):
    """Test consumepage.get_crumb_list_by_selector.

    Ensure returns the expected list of crumbs.
    """
    test_consumepage = consumepage_fixture
    crumb_list = test_consumepage.get_crumb_list_by_selector(
        TEST_CRUMB_SELECTOR
    )

    assert crumb_list == EXPECTED_CRUMB_LIST
