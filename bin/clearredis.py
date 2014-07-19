#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Command-line interface to clear Redis."""

import argparse
from parker.redisset import get_instance
from parker.queues import crawl_q, consume_q

parser = argparse.ArgumentParser(
    description=(
        'Clear up the Redis stuff for the specified site.'
    )
)
parser.add_argument(
    'site',
    type=str,
    help='the name of the site'
)
args = parser.parse_args()
site = args.site

crawl_q.empty()
consume_q.empty()

visited = get_instance(
    "%s:%s" % (site, 'visited')
)
consume = get_instance(
    "%s:%s" % (site, 'consume')
)

visited.destroy()
consume.destroy()
