# -*- coding: utf-8 -*-
"""ConsumePage object for Parker."""

import urlparse
import page
import parser
import mediafile

_instances = dict()


def get_instance(page_to_consume):
    """Return an instance of ConsumePage."""
    if isinstance(page_to_consume, unicode):
        uri = page_to_consume
        page_to_consume = page.get_instance(uri)
    elif isinstance(page_to_consume, page.Page):
        uri = page_to_consume.uri
    else:
        raise TypeError(
            "get_instance() expects a parker.Page or unicode derivative."
        )

    page_to_consume.fetch()
    parsed_page = parser.parse(page_to_consume)

    try:
        instance = _instances[uri]
    except KeyError:
        instance = ConsumePage(
            parsed_page
        )
        _instances[uri] = instance

    return instance


class ConsumePage(object):

    """A ConsumePage."""

    def __init__(self, parsedpage):
        """Constructor."""
        self.parsedpage = parsedpage
        self.uri = parsedpage.page.uri
        self.hash = parsedpage.page.hash

    def __repr__(self):
        """Return an unambiguous representation."""
        return "%s(%s)" % (self.__class__, self.uri)

    def get_key_value_dict_by_selectors(self, key_selector, value_selector):
        """Return a dictionary of key value data."""
        key_nodes = self.parsedpage.get_nodes_by_selector(key_selector)
        value_nodes = self.parsedpage.get_nodes_by_selector(value_selector)

        keys = [
            self.parsedpage.get_text_from_node(node)
            for node in key_nodes
        ]
        vals = [
            self.parsedpage.get_text_from_node(node)
            for node in value_nodes
        ]

        return dict(zip(keys, vals))

    def get_crumb_list_by_selector(self, crumb_selector):
        """Return a list of crumbs."""
        return [
            self.parsedpage.get_text_from_node(crumb)
            for crumb in self.parsedpage.get_nodes_by_selector(crumb_selector)
        ]

    def get_media_list_by_selector(
        self, media_selector, media_attribute="src"
    ):
        """Return a list of media."""
        return [
            mediafile.get_instance(
                urlparse.urlparse(
                    media.attrib[media_attribute],
                    scheme="http"
                ).geturl()
            )
            for media in self.parsedpage.get_nodes_by_selector(media_selector)
        ]

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
