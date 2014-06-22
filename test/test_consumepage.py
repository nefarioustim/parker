# -*- coding: utf-8 -*-
"""Test the ConsumePage object."""

import pytest
from pyquery import PyQuery
from parker import parser, consumepage, parsedpage
from parker.configloader import load_site_config
from test_client import client_fixture
from test_page import page_fixture
import utils

TEST_URI = "http://www.staples.co.uk/full-strip-stapler/cbs/412852.html"
TEST_KEY_SELECTOR = "#divSpecifications dd .l"
TEST_VALUE_SELECTOR = "#divSpecifications dd .r"
TEST_CRUMB_SELECTOR = "#skuBreadCrumbs span[itemprop=title]"
TEST_MEDIA_SELECTOR = ".s7Thumbs img"
TEST_MEDIA_ATTRIBUTE = "data-zoomimage"
TEST_CONFIG_NAME = "staples"
TEST_CONFIG = load_site_config(TEST_CONFIG_NAME)
TEST_DATA_CONFIG = TEST_CONFIG['specific_data']
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
EXPECTED_MEDIA_LIST = [
    '//www.staples.co.uk/content/images/product/uk_412852_1_xnl.jpg'
]
EXPECTED_DATA_DICT = {
    'title': 'Full Strip Stapler',
    'sku': 'WW-412852'
}


@pytest.fixture(scope="function")
def consumepage_fixture(page_fixture):
    """Test fixture to ensure correct mocking for parsedpage."""
    test_consumepage = consumepage.get_instance(
        page_fixture
    )
    return test_consumepage


def test_get_instance_creates_consumepage_object(page_fixture):
    """Test parsedpage.get_instance creates a ParsedPage object."""
    test_consumepage = consumepage.get_instance(
        page_fixture
    )
    expected_repr = "<class 'parker.consumepage.ConsumePage'>(%s)" % (
        TEST_URI
    )

    assert isinstance(test_consumepage, consumepage.ConsumePage)
    assert isinstance(test_consumepage.parsedpage, parsedpage.ParsedPage)
    assert test_consumepage.__repr__() == expected_repr


def test_get_key_value_dict_by_selectors_returns_expected_dict(
    consumepage_fixture
):
    """Test consumepage.get_key_value_dict_by_selectors.

    Ensure returns the expected dictionary of data.
    """
    test_consumepage = consumepage_fixture
    key_value_dict = test_consumepage.get_key_value_dict_by_selectors(
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


def test_get_media_list_by_selector_returns_expected_list(
    consumepage_fixture
):
    """Test consumepage.get_media_list_by_selector.

    Ensure returns the expected list of media.
    """
    test_consumepage = consumepage_fixture
    media_list = test_consumepage.get_media_list_by_selector(
        TEST_MEDIA_SELECTOR,
        TEST_MEDIA_ATTRIBUTE
    )

    assert media_list == EXPECTED_MEDIA_LIST


def test_get_data_dict_from_config_returns_expected_dict(
    consumepage_fixture
):
    """Test consumepage.get_data_dict_from_config.

    Ensure returns the expected dictionary of data.
    """
    test_consumepage = consumepage_fixture
    data_dict = test_consumepage.get_data_dict_from_config(TEST_DATA_CONFIG)

    assert data_dict == EXPECTED_DATA_DICT
