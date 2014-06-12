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
EXPECTED_VALUE = "Staples Full Strip Stapler"
EXPECTED_FILTERED_VALUE = "Staples"


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
    """Test consumepage.get_filtered_data_by_selector.Ensure

    Ensure returns the expected value of the H1.
    """
    test_consumepage = consumepage_fixture
    actual_value = test_consumepage.get_filtered_data_by_selector(TEST_SELECTOR)

    assert actual_value == EXPECTED_VALUE


def test_get_filtered_data_by_selector_returns_expected_filtered_value_of_h1_with_regex(
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
