# -*- coding: utf-8 -*-
"""Test the ConsumeModel object."""

from parker import consumemodel

TEST_URI = "http://www.staples.co.uk/full-strip-stapler/cbs/412852.html"


def test_get_instance_creates_consumemodel_object():
    """Test consumemodel.get_instance creates a ConsumeModel object."""
    test_consumemodel = consumemodel.get_instance(TEST_URI)

    assert isinstance(test_consumemodel, consumemodel.ConsumeModel) is True
