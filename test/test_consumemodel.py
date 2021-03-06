# -*- coding: utf-8 -*-
"""Test the ConsumeModel object."""

import os
import shutil
import pytest
from parker import consumemodel, fileops
from parker.configloader import load_site_config
from parker.mediafile import MediaFile
from test_client import client_fixture
from test_page import page_fixture
from test_consumepage import consumepage_fixture

TEST_URI = "http://www.staples.co.uk/full-strip-stapler/cbs/412852.html"
TEST_CONFIG_NAME = "staples"
TEST_CONFIG = load_site_config(TEST_CONFIG_NAME)
TEST_FILE = "/tmp/test.data"
TEST_PATH = "/tmp"
EXPECTED_KV_DICT = {
    u'Staple Compatibility :': u'26/06/2014',
    u'Brands :': u'Staples',
    u'Stapling Capacity (sheets) :': u'20 sheets',
    u'Quantity :': u'1'
}
EXPECTED_CRUMB_LIST = [
    u'Pens | Tape | Desk Supplies',
    u'Desktop Stationery | Clips | Accessories',
    u'Staplers'
]
EXPECTED_MEDIA_LIST_URLS = [
    'http://www.staples.co.uk/content/images/product/uk_412852_1_xnl.jpg'
]
EXPECTED_DATA_DICT = {
    'title': 'Full Strip Stapler',
    'sku': 'WW-412852',
    'colour': 'Black'
}
EXPECTED_UNIQUE_FIELD = 'WW-412852'
EXPECTED_MEDIA_PATH = "/tmp/staples/WW-/412/852"
EXPECTED_MEDIA_FILE = "/tmp/staples/WW-/412/852/WW-412852_0.jpg"


@pytest.fixture(scope="function")
def consumemodel_fixture(consumepage_fixture):
    """Test fixture to ensure correct mocking for parsedpage."""
    return consumemodel.get_instance(consumepage_fixture)


def test_get_instance_creates_consumemodel_object(consumepage_fixture):
    """Test consumemodel.get_instance creates a ConsumeModel object."""
    test_consumemodel = consumemodel.get_instance(consumepage_fixture)

    assert isinstance(test_consumemodel, consumemodel.ConsumeModel)


def test_get_instance_raises_typeerror_unexpected_parameter_type():
    """Test consumemodel.get_instance throws TypeError on unexpected param."""
    with pytest.raises(TypeError):
        test_consumemodel = consumemodel.get_instance(None)


def test_load_from_config_populates_model(consumemodel_fixture):
    """Test consumemodel.load_from_config populates the model members."""
    test_consumemodel = consumemodel_fixture
    test_consumemodel.load_from_config(TEST_CONFIG)

    assert test_consumemodel.site == TEST_CONFIG_NAME
    assert test_consumemodel.data_dict == EXPECTED_DATA_DICT
    assert test_consumemodel.key_value_dict == EXPECTED_KV_DICT
    assert test_consumemodel.crumb_list == EXPECTED_CRUMB_LIST
    assert test_consumemodel.unique_field == EXPECTED_UNIQUE_FIELD

    for mediafile in test_consumemodel.media_list:
        assert isinstance(mediafile, MediaFile)
        assert mediafile.uri in EXPECTED_MEDIA_LIST_URLS
