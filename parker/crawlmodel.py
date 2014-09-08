# -*- coding: utf-8 -*-
"""Model object for crawled pages in Parker."""

import crawlpage

_instances = dict()


def get_instance(page_to_crawl):
    """Return an instance of CrawlModel."""
    global _instances
    if isinstance(page_to_crawl, basestring):
        uri = page_to_crawl
        page_to_crawl = crawlpage.get_instance(uri)
    elif isinstance(page_to_crawl, crawlpage.CrawlPage):
        uri = page_to_crawl.uri
    else:
        raise TypeError(
            "get_instance() expects a parker.CrawlPage "
            "or basestring derivative."
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
        self.hash = crawlpage.hash
        self.site = None
        self.uri_base = None
        self.uris_to_crawl = None
        self.is_consume_page = False

    def load_from_config(self, config):
        """Load model from passed configuration."""
        self.site = config.get("id", False)
        self.uri_base = config.get("uri_base", False)
        self.uris_to_crawl = self.crawlpage.get_uris(
            base_uri=self.uri_base,
            filter_list=config.get("crawl_uri_filters", None)
        )
        self.is_consume_page = self.crawlpage.has_selector(
            config.get("consume_selector", False)
        )
