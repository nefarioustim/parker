# -*- coding: utf-8 -*-
"""CrawlPage object for Parker."""

import re
import page
import parser
import urlparse

_instances = dict()


def get_instance(page_to_consume):
    """Return an instance of CrawlPage."""
    global _instances
    if isinstance(page_to_consume, basestring):
        uri = page_to_consume
        page_to_consume = page.get_instance(uri)
    elif isinstance(page_to_consume, page.Page):
        uri = page_to_consume.uri
    else:
        raise TypeError(
            "get_instance() expects a parker.Page or basestring derivative."
        )

    page_to_consume.fetch()
    parsed_page = parser.parse(page_to_consume)

    try:
        instance = _instances[uri]
    except KeyError:
        instance = CrawlPage(
            parsed_page
        )
        _instances[uri] = instance

    return instance


class CrawlPage(object):

    """A CrawlPage."""

    def __init__(self, parsedpage):
        """Constructor."""
        self.parsedpage = parsedpage
        self.uri = parsedpage.page.uri
        self.hash = parsedpage.page.hash

    def __repr__(self):
        """Return an unambiguous representation."""
        return "%s(%s)" % (self.__class__, self.uri)

    def get_uris(self, base_uri, filter_list=None):
        """Return a set of internal URIs."""
        return {
            re.sub(r'^/', base_uri, link.attrib['href'])
            for link in self.parsedpage.get_nodes_by_selector('a')
            if 'href' in link.attrib and (
                link.attrib['href'].startswith(base_uri) or
                link.attrib['href'].startswith('/')
            ) and
            not is_uri_to_be_filtered(link.attrib['href'], filter_list)
        }

    def has_selector(self, consume_selector):
        """Test if page has selector."""
        return bool(self.parsedpage.get_nodes_by_selector(consume_selector))


def is_uri_to_be_filtered(uri, filter_list):
    """Test whether @uri should be filtered by @filter_list."""
    match = False
    if filter_list:
        for uri_filter in filter_list:
            if re.search(uri_filter, uri, flags=re.IGNORECASE):
                match = True
        return match
