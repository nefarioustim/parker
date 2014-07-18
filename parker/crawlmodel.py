# -*- coding: utf-8 -*-
"""Model object for crawled pages in Parker."""

import crawlpage

_instances = dict()


def get_instance(page_to_crawl):
    """Return an instance of CrawlModel."""
    if isinstance(page_to_crawl, str):
        uri = page_to_crawl
        page_to_crawl = crawlpage.get_instance(uri)
    elif isinstance(page_to_crawl, crawlpage.CrawlPage):
        uri = page_to_crawl.uri
    else:
        raise TypeError(
            "get_instance() expects a parker.CrawlPage or str derivative."
        )

    try:
        instance = _instances[uri]
    except KeyError:
        instance = CrawlModel(page_to_crawl)
        _instances[uri] = instance

    return instance


class CrawlModel(object):

    """Model representing a consumed page."""

    def __init__(self, crawlpage):
        """Constructor."""
        self.crawlpage = crawlpage
        self.uri = crawlpage.uri
