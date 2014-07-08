# -*- coding: utf-8 -*-
"""Test the worker methods."""

import os.path
from parker import fileops
from parker.workers import consumer
from test_client import client_fixture

TEST_URI = "http://www.staples.co.uk/full-strip-stapler/cbs/412852.html"
TEST_SITE = "staples"
EXPECTED_FILE = os.path.join(
    fileops.DATA_DIR,
    TEST_SITE + '.data'
)
EXPECTED_DATA_DICT = {
    'title': 'Full Strip Stapler',
    'sku': 'WW-412852'
}


def test_consumer_writes_data_to_file(client_fixture):
    """Test workers.consumer writes correct data to file system."""
    consumer(TEST_SITE, TEST_URI)

    assert os.path.exists(EXPECTED_FILE)
    assert os.path.isfile(EXPECTED_FILE)

    line = fileops.get_line_from_file(EXPECTED_FILE).next()

    for key, value in EXPECTED_DATA_DICT.iteritems():
        assert value in line

    os.remove(EXPECTED_FILE)
