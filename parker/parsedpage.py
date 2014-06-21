# -*- coding: utf-8 -*-
"""ParsedPage object for Parker."""

import re

_instances = dict()


def get_instance(page, parsed):
    """Return an instance of ParsedPage."""
    try:
        instance = _instances[page.uri]
    except KeyError:
        instance = ParsedPage(page, parsed)
        _instances[page.uri] = instance

    return instance


class ParsedPage(object):

    """A ParsedPage."""

    def __init__(self, page, parsed):
        """Constructor."""
        self.page = page
        self.original = page.content
        self.parsed = parsed

    def __repr__(self):
        """Return an unambiguous representation."""
        return "%s(%s)" % (self.__class__, self.page.uri)

    def get_nodes_by_selector(self, selector, not_selector=None):
        """Return a collection of filtered nodes.

        Filtered based on the @selector and @not_selector parameters.
        """
        nodes = self.parsed(selector)

        if not_selector is not None:
            nodes = nodes.not_(not_selector)

        return nodes

    def get_text_from_node(self, node, regex=None, group=1):
        """Get text from node and filter if necessary."""
        text = self._get_stripped_text_from_node(node)

        if regex is not None:
            text = self._filter_by_regex(regex, text, group)

        return text

    def get_filtered_values_by_selector(self, selector, regex=None, group=1):
        """Return the text content of @selector.

        Filter text content by @regex and @group.
        """
        data = [
            self.get_text_from_node(node, regex, group)
            for node in self.get_nodes_by_selector(selector)
            if self.get_text_from_node(node, regex, group)
        ]

        return data if len(data) > 1 else data[0]

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

        return match.group(group).strip() if (
            match and match.groups()
        ) else text
