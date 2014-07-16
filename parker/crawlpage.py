# -*- coding: utf-8 -*-
"""CrawlPage object for Parker."""

import page
import parser

_instances = dict()


def get_instance(page_to_consume):
    """Return an instance of CrawlPage."""
    if isinstance(page_to_consume, str):
        uri = page_to_consume
        page_to_consume = page.get_instance(uri)
    elif isinstance(page_to_consume, page.Page):
        uri = page_to_consume.uri
    else:
        raise TypeError(
            "get_instance() expects a parker.Page or str derivative."
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

    def get_uris(self, base_uri):
        """Return a set of internal URIs."""
        return {
            link.attrib['href']
            for link in self.parsedpage.get_nodes_by_selector('a')
            if 'href' in link.attrib
            and base_uri in link.attrib['href']
        }
