# -*- coding: utf-8 -*-
"""Test the ConsumeStore object."""

import os
import shutil
import pytest
from parker import consumestore, fileops
from parker.configloader import load_site_config
from test_consumemodel import (
    client_fixture, page_fixture, consumepage_fixture, consumemodel_fixture
)

TEST_CONFIG_NAME = "staples"
TEST_CONFIG = load_site_config(TEST_CONFIG_NAME)
TEST_FILE = "/tmp/supplies/staples.data"
TEST_PATH = "/tmp"
EXPECTED_MEDIA_PATH = "/tmp/staples/WW-/412/852"
EXPECTED_MEDIA_FILE = "/tmp/staples/WW-/412/852/WW-412852_0.jpg"
EXPECTED_DATA_DICT = {
    'title': 'Full Strip Stapler',
    'sku': 'WW-412852',
    'colour': 'Black'
}


@pytest.fixture(scope="function")
def consumestore_fixture(consumemodel_fixture):
    """Test fixture to ensure correct mocking for parsedpage."""
    test_consumemodel = consumemodel_fixture
    test_consumemodel.load_from_config(TEST_CONFIG)
    return consumestore.get_instance(test_consumemodel)


def test_save_media_raises_typeerror_on_non_model():
    """Test consumestore.get_instance raises a TypeError when expected."""
    with pytest.raises(TypeError):
        consumestore.get_instance(
            model=''
        )


def test_save_media_saves_media_to_filesystem(consumestore_fixture):
    """Test consumestore.save_media does what it says on the tin."""
    test_consumestore = consumestore_fixture
    test_consumestore.save_media(
        path=TEST_PATH
    )

    assert os.path.exists(EXPECTED_MEDIA_PATH)
    assert os.path.isfile(EXPECTED_MEDIA_FILE)

    shutil.rmtree('/tmp/staples')


def test_save_data_saves_model_to_file_as_json(consumestore_fixture):
    """Test consumestore.save_data saves the model to the passed file.

    Model should be saved as JSON.
    """
    test_consumestore = consumestore_fixture
    test_consumestore.save_data(
        path=TEST_PATH
    )

    assert os.path.exists(TEST_FILE)
    assert os.path.isfile(TEST_FILE)

    line = fileops.get_line_from_file(TEST_FILE).next()

    for key, value in EXPECTED_DATA_DICT.iteritems():
        assert value in line

    os.remove(TEST_FILE)
