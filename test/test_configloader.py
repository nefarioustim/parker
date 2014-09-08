# -*- coding: utf-8 -*-
"""Test the configuration loader."""

import pytest
from parker.configloader import load_config, load_site_config

TEST_CONFIG_NAME = 'redis'
TEST_CONFIG_KEY = 'host'
TEST_CONFIG_VALUE = 'localhost'
TEST_SITE_NAME = 'staples'
EXPECTED_SITE_CONFIG = {
    "id": "staples",
    "class": "supplies",
    "tags": ["office", "stationary"],
    "seconds_until_expire": 259200,
    "uri_base": "http://www.staples.co.uk/",
    "uri_start_crawl": "http://www.staples.co.uk/",
    'crawl_uri_filters': ['staples_soul'],
    "consume_selector": "#PageInner .skuPage",
    "unique_field": "sku",
    "specific_data": {
        "title": {
            "selector": "h1",
            "regex_filter": "Staples ([a-zA-Z0-9 ]+)"
        },
        "sku": {
            "selector": ".skuDetails .iNumber",
            "regex_filter": "([a-zA-Z0-9\\-]+)$"
        },
        "colour": {
            "kv_ref": "Colour :"
        }
    },
    "key_value_data": {
        "key_selector": "#divSpecifications dd .l",
        "value_selector": "#divSpecifications dd .r"
    },
    "crumbs": {
        "selector": "#skuBreadCrumbs span[itemprop=title]"
    },
    "media": {
        "selector": ".s7Thumbs img",
        "attribute": "data-zoomimage"
    }
}


def test_load_config_loads_json_into_a_dict():
    """Test 'redis' config loads and that 'host' is 'localhost'."""
    config = load_config(TEST_CONFIG_NAME)

    assert config[TEST_CONFIG_KEY] == TEST_CONFIG_VALUE


def test_load_site_config_loads_json_into_a_dict():
    """Test 'staples' test content is loaded correctly."""
    site_config = load_site_config(TEST_SITE_NAME)

    assert site_config == EXPECTED_SITE_CONFIG
