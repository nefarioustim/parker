# -*- coding: utf-8 -*-
"""Worker methods for Parker."""

import os.path
from consumemodel import get_instance as get_consume
from crawlmodel import get_instance as get_crawl
from redisset import get_instance as get_redisset
from queues import crawl_q, consume_q
from configloader import load_site_config
from fileops import IMG_DIR, DATA_DIR

_get_instance = {
    'consume': get_consume,
    'crawl': get_crawl
}


def consumer(site, uri):
    """Consume URI using site config."""
    model = _get_model('consume', site, uri)
    model.save_media_to_file(IMG_DIR)
    model.save_to_file(
        os.path.join(
            DATA_DIR,
            model.classification,
            site + '.data'
        ) if model.classification is not None else os.path.join(
            DATA_DIR,
            site + '.data'
        )
    )


def crawler(site, uri=None):
    """Crawl URI using site config."""
    visited_set, visited_uri_set, consume_set = _get_site_sets(site)
    model = _get_model('crawl', site, uri)

    if not visited_set.has(model.hash):
        visited_set.add(model.hash)
        visited_uri_set.add(model.uri)

        if (
            model.is_consume_page
            and not consume_set.has(model.hash)
        ):
            consume_set.add(model.hash)
            consume_q.enqueue(
                consumer,
                site,
                model.uri
            )
        else:
            for crawl_uri in model.uris_to_crawl:
                if not visited_uri_set.has(crawl_uri):
                    crawl_q.enqueue(
                        crawler,
                        site,
                        crawl_uri
                    )


def killer(site):
    """Kill queues and Redis sets."""
    crawl_q.empty()
    consume_q.empty()

    for site_set in _get_site_sets(site):
        site_set.destroy()


def _get_site_sets(site):
    return (
        get_redisset(
            "%s:%s" % (site, 'visited')
        ),
        get_redisset(
            "%s:%s" % (site, 'visited-uri')
        ),
        get_redisset(
            "%s:%s" % (site, 'consume')
        )
    )


def _get_model(model_name, site, uri):
    config = load_site_config(site)
    model = _get_instance[model_name](
        uri if uri is not None else config.get('uri_start_crawl', None)
    )
    model.load_from_config(config)
    return model
