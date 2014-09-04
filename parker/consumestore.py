# -*- coding: utf-8 -*-
"""Storage class for ConsumeModel objects."""

from consumemodel import ConsumeModel
from fileops import DATA_DIR, IMG_DIR

_instances = dict()


def get_instance(model):
    """Return an instance of ConsumeStore."""
    global _instances
    if isinstance(model, ConsumeModel):
        key = model.uri
    else:
        raise TypeError(
            "get_instance() expects a parker.ConsumeModel derivative."
        )

    try:
        instance = _instances[key]
    except KeyError:
        instance = ConsumeStore(model)
        _instances[key] = instance

    return instance


class ConsumeStore(object):

    """Object for storing ConsumeModel objects."""

    def __init__(self, model):
        self.model = model

    def save_media():
        pass

    def save_data():
        pass