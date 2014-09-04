# -*- coding: utf-8 -*-
"""Test the ConsumeStore object."""

import pytest
from parker import consumestore
from test_consumemodel import (
    client_fixture, page_fixture, consumepage_fixture, consumemodel_fixture
)


def test_get_instance_creates_consumestore_object(consumemodel_fixture):
    """Test consumestore.get_instance creates a ConsumeStore object."""
    test_consumestore = consumestore.get_instance(
        model=consumemodel_fixture
    )

    assert isinstance(test_consumestore, consumestore.ConsumeStore)


def test_get_instance_raises_type_error_on_non_model():
    """Test consumestore.get_instance raises a TypeError if a non-model is passed in."""
    with pytest.raises(TypeError):
        test_consumestore = consumestore.get_instance(
            model=''
        )
