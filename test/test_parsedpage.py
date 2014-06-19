# -*- coding: utf-8 -*-
"""Test the ParsedPage object."""

import pytest
from pyquery import PyQuery
from parker import parser, parsedpage
from test_client import client_fixture
from test_page import page_fixture
import utils

TEST_CONTENT = utils.load_stub_as_string('staples-stapler.html')
TEST_PARSED = PyQuery(TEST_CONTENT, parser='html')
TEST_SELECTOR = "#SideMenuListInner li"
TEST_H1_SELECTOR = "h1"
TEST_REGEX = r"(\w+)"
EXPECTED_NODES = 26
TEST_NOT_SELECTOR = "#sLi8"
EXPECTED_NODES_AFTER_NOT = 25
EXPECTED_VALUE = "Staples Full Strip Stapler"
EXPECTED_FILTERED_VALUE = "Staples"


@pytest.fixture(scope="function")
def parsedpage_fixture(page_fixture):
    """Test fixture to ensure correct mocking for parsedpage."""
    test_page = page_fixture
    return parser.parse(test_page)


def test_get_instance_creates_parsedpage_object(page_fixture):
    """Test parsedpage.get_instance creates a ParsedPage object."""
    test_page = page_fixture
    test_parsedpage = parsedpage.get_instance(
        test_page,
        TEST_CONTENT,
        TEST_PARSED
    )
    expected_repr = "<class 'parker.parsedpage.ParsedPage'>(%s)" % (
        test_page.uri
    )

    assert isinstance(test_parsedpage, parsedpage.ParsedPage) is True
    assert test_parsedpage.__repr__() == expected_repr


def test_get_nodes_by_selector_returns_expected_nodes(
    parsedpage_fixture
):
    """Test ParsedPage.get_nodes_by_selector returns the expected nodes."""
    test_parsedpage = parsedpage_fixture
    test_nodes = test_parsedpage.get_nodes_by_selector(TEST_SELECTOR)

    assert len(test_nodes) == EXPECTED_NODES


def test_get_nodes_by_selector_returns_expected_nodes_with_not(
    parsedpage_fixture
):
    """Test ParsedPage.get_nodes_by_selector returns the expected nodes."""
    test_parsedpage = parsedpage_fixture
    test_nodes = test_parsedpage.get_nodes_by_selector(
        TEST_SELECTOR,
        TEST_NOT_SELECTOR
    )

    assert len(test_nodes) == EXPECTED_NODES_AFTER_NOT


def test_get_filtered_values_by_selector_returns_expected_value_of_h1(
    parsedpage_fixture
):
    """Test consumepage.get_filtered_values_by_selector.

    Ensure returns the expected value of the H1.
    """
    test_consumepage = parsedpage_fixture
    actual_value = test_consumepage.get_filtered_values_by_selector(
        TEST_H1_SELECTOR
    )

    assert actual_value == EXPECTED_VALUE


def test_get_filtered_values_by_selector_returns_expected_filtered_value_of_h1(
    parsedpage_fixture
):
    """Test consumepage.get_filtered_values_by_selector.

    Ensure returns the expected value of the H1 filtered by regex.
    """
    test_consumepage = parsedpage_fixture
    actual_value = test_consumepage.get_filtered_values_by_selector(
        TEST_H1_SELECTOR,
        regex=TEST_REGEX
    )

    assert actual_value == EXPECTED_FILTERED_VALUE
