# -*- coding: utf-8 -*-
"""Test the configuration loader."""

import pytest
from parker.configloader import load_config

TEST_CONFIG_NAME = 'redis'
TEST_CONFIG_KEY = 'host'
TEST_CONFIG_VALUE = 'localhost'


def test_load_config_loads_json_into_a_dict():
    """Test 'redis' config loads and that 'host' is 'localhost'."""
    config = load_config(TEST_CONFIG_NAME)

    assert config[TEST_CONFIG_KEY] == TEST_CONFIG_VALUE
