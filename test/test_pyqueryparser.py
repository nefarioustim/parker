# -*- coding: utf-8 -*-
"""Test the PyQueryParser object."""

from parker import page, pyqueryparser
from test_page import page_fixture


def test_pyqueryparser_get_instance_creates_pyqueryparser_object():
    """Test pyqueryparser.get_instance creates a PyQueryParser object."""
    test_pyqueryparser = pyqueryparser.get_instance()

    assert isinstance(test_pyqueryparser, pyqueryparser.PyQueryParser) is True
