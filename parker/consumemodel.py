# -*- coding: utf-8 -*-
"""Model object for consumed pages in Parker."""

import consumepage

_instances = dict()


def get_instance(page_to_consume):
    """Return an instance of ConsumeModel."""
    if isinstance(page_to_consume, str):
        uri = page_to_consume
        page_to_consume = consumepage.get_instance(uri)
    elif isinstance(page_to_consume, consumepage.ConsumePage):
        uri = page_to_consume.uri
    else:
        raise TypeError(
            "get_instance() expects a parker.ConsumePage or str derivative."
        )

    try:
        instance = _instances[uri]
    except KeyError:
        instance = ConsumeModel(page_to_consume)
        _instances[uri] = instance

    return instance


class ConsumeModel(object):

    """Model representing a consumed page."""

    def __init__(self, consumepage):
        """Constructor."""
        self.consumepage = consumepage
