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
        self.uri = consumepage.uri
        self.data_dict = None
        self.key_value_dict = None
        self.crumb_list = None
        self.media_list = None

    def load_from_config(self, config):
        """Load model from passed configuration."""
        self._load_data(
            config.get("specific_data", False)
        )
        self._load_key_value(
            config.get("key_value_data", False)
        )
        self._load_crumb(
            config.get("crumbs", False)
        )
        self._load_media_list(
            config.get("media", False)
        )

    def _load_data(self, data_config):
        self.data_dict = self.consumepage.get_data_dict_from_config(
            data_config
        ) if data_config else None

    def _load_key_value(self, key_value_config):
        self.key_value_dict = self.consumepage.get_key_value_dict_by_selectors(
            key_value_config["key_selector"],
            key_value_config["value_selector"]
        ) if (
            key_value_config
            and key_value_config.get("key_selector", False)
            and key_value_config.get("value_selector", False)
        ) else None

    def _load_crumb(self, crumb_config):
        self.crumb_list = self.consumepage.get_crumb_list_by_selector(
            crumb_config["selector"]
        ) if (
            crumb_config
            and crumb_config.get("selector", False)
        ) else None

    def _load_media_list(self, media_config):
        self.media_list = self.consumepage.get_media_list_by_selector(
            media_config["selector"],
            media_config["attribute"],
        ) if (
            media_config
            and media_config.get("selector", False)
            and media_config.get("attribute", False)
        ) else None
