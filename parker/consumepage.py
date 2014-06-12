# -*- coding: utf-8 -*-
"""ConsumePage object for Parker."""

import re
from parsedpage import ParsedPage

_instances = dict()


def get_instance(parsedpage):
    """Return an instance of ConsumePage."""
    try:
        instance = _instances[parsedpage.page.uri]
    except KeyError:
        instance = ConsumePage(parsedpage)
        _instances[parsedpage.page.uri] = instance

    return instance


class ConsumePage(ParsedPage):

    """A ConsumePage."""

    def __init__(self, parsedpage):
        """Constructor."""
        self.parsedpage = parsedpage

    def __repr__(self):
        """Return an unambiguous representation."""
        return "%s(%s)" % (self.__class__, self.parsedpage.page.uri)

    def _get_stripped_text_from_node(self, node):
        """Return the stripped text content of a node."""
        return (
            node.text_content()
            .replace(u"\u00A0", " ")
            .replace("\t", "")
            .replace("\n", "")
            .strip()
        )

    def _filter_by_regex(self, regex, text, group=1):
        """Filter @text by @regex."""
        match = re.search(
            regex,
            text,
            re.MULTILINE
        )

        if match and match.groups():
            return match.group(group).strip()
        else:
            return text

    def _get_text_from_node(self, node, regex=None, group=1):
        """Get text from node and filter if necessary."""
        text = self._get_stripped_text_from_node(node)

        if regex is not None:
            text = self._filter_by_regex(regex, text, group)

        return text

    def get_filtered_data_by_selector(self, selector, regex=None, group=1):
        """Return the text content of @selector.

        Filter text content by @regex and @group.
        """
        nodes = self.parsedpage.get_nodes_by_selector(selector)
        values = [
            self._get_text_from_node(node, regex, group)
            for node in nodes
            if self._get_text_from_node(node, regex, group)
        ]

        if len(values) == 0:
            return None
        elif len(values) == 1:
            return values[0]
        else:
            return values
