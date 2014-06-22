# -*- coding: utf-8 -*-
"""ConsumePage object for Parker."""

import page
import parser

_instances = dict()


def get_instance(uri):
    """Return an instance of ConsumePage."""
    try:
        instance = _instances[uri]
    except KeyError:
        instance = ConsumePage(
            page.get_instance(uri)
        )
        _instances[uri] = instance

    return instance


def _require_parsedpage(func):
    def _decorator(self, *args, **kwargs):
        if self.parsedpage is None:
            self._init_parsedpage()

        return func(self, *args, **kwargs)

    return _decorator


class ConsumePage(object):

    """A ConsumePage."""

    def __init__(self, page):
        """Constructor."""
        self.page = page
        self.parsedpage = None
        self.uri = self.page.uri

    def __repr__(self):
        """Return an unambiguous representation."""
        return "%s(%s)" % (self.__class__, self.uri)

    def _init_parsedpage(self):
        """Trigger the fetch of the Page and subsequent parse."""
        self.page.fetch()
        self.parsedpage = parser.parse(self.page)

    @_require_parsedpage
    def get_key_value_dict_by_selectors(self, key_selector, value_selector):
        """Return a dictionary of key value data."""
        key_nodes = self.parsedpage.get_nodes_by_selector(key_selector)
        value_nodes = self.parsedpage.get_nodes_by_selector(value_selector)

        keys = [
            self.parsedpage.get_text_from_node(node) for node in key_nodes
        ]
        vals = [
            self.parsedpage.get_text_from_node(node) for node in value_nodes
        ]

        return dict(zip(keys, vals))

    @_require_parsedpage
    def get_crumb_list_by_selector(self, crumb_selector):
        """Return a list of crumbs."""
        return [
            self.parsedpage.get_text_from_node(crumb)
            for crumb in self.parsedpage.get_nodes_by_selector(crumb_selector)
        ]

    @_require_parsedpage
    def get_media_list_by_selector(
        self, media_selector, media_attribute="src"
    ):
        """Return a list of media."""
        return [
            media.attrib[media_attribute]
            for media in self.parsedpage.get_nodes_by_selector(media_selector)
        ]

    @_require_parsedpage
    def get_data_dict_from_config(self, config_dict):
        """Return a dictionary of data inferred from config_dict."""
        return {
            key: self.parsedpage.get_filtered_values_by_selector(
                item_dict['selector'],
                item_dict.get('regex_filter', None),
                item_dict.get('regex_group', 1)
            )
            for key, item_dict in config_dict.iteritems()
            if item_dict.get('selector', None) is not None
        }
