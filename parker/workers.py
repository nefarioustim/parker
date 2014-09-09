# -*- coding: utf-8 -*-
"""Worker methods for Parker."""

import os.path
from consumemodel import get_instance as get_consume
from crawlmodel import get_instance as get_crawl
from consumestore import get_instance as get_consumestore
from redisset import get_instance as get_redisset
from queues import crawl_q, consume_q
from configloader import load_site_config, load_config
from fileops import IMG_DIR, DATA_DIR

_config = load_config("parker")

_get_instance = {
    'consume': get_consume,
    'crawl': get_crawl
}


def consumer(site, uri):
    """Consume URI using site config."""
    config = load_site_config(site)
    model = _get_model('consume', config, uri)
    consumestore = get_consumestore(
        model=model,
        method=_config.get('storage', 'file')
    )
    consumestore.save_media()
    consumestore.save_data()


def crawler(site, uri=None):
    """Crawl URI using site config."""
    config = load_site_config(site)
    model = _get_model('crawl', config, uri)
    visited_set, visited_uri_set, consume_set, crawl_set = get_site_sets(
        site, config
    )

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
                if (
                    not visited_uri_set.has(crawl_uri)
                    and not crawl_set.has(crawl_uri)
                ):
                    crawl_set.add(crawl_uri)
                    crawl_q.enqueue(
                        crawler,
                        site,
                        crawl_uri
                    )


def killer(site):
    """Kill queues and Redis sets."""
    config = load_site_config(site)
    crawl_q.empty()
    consume_q.empty()

    for site_set in get_site_sets(site, config):
        site_set.destroy()


def get_site_sets(site, config=None):
    config = config or {}
    return (
        get_redisset(
            "%s:%s" % (site, 'visited'),
            config.get('seconds_until_expire', None)
        ),
        get_redisset(
            "%s:%s" % (site, 'visited-uri'),
            config.get('seconds_until_expire', None)
        ),
        get_redisset(
            "%s:%s" % (site, 'consume'),
            config.get('seconds_until_expire', None)
        ),
        get_redisset(
            "%s:%s" % (site, 'crawl'),
            config.get('seconds_until_expire', None)
        )
    )


def _get_model(model_name, config, uri):
    model = _get_instance[model_name](
        uri if uri is not None else config.get('uri_start_crawl', None)
    )
    model.load_from_config(config)
    return model
