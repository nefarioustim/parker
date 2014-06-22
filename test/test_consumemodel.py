# -*- coding: utf-8 -*-
"""Test the ConsumeModel object."""

import pytest
from parker import consumemodel
from test_client import client_fixture
from test_page import page_fixture
from test_consumepage import consumepage_fixture

TEST_URI = "http://www.staples.co.uk/full-strip-stapler/cbs/412852.html"


def test_get_instance_creates_consumemodel_object(consumepage_fixture):
    """Test consumemodel.get_instance creates a ConsumeModel object."""
    test_consumemodel = consumemodel.get_instance(consumepage_fixture)

    assert isinstance(test_consumemodel, consumemodel.ConsumeModel)


def test_get_instance_raises_typeerror_unexpected_parameter_type():
    """Test consumemodel.get_instance throws TypeError on unexpected param."""
    with pytest.raises(TypeError):
        test_consumemodel = consumemodel.get_instance(None)
