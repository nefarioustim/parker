#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Command-line interface to kick off the crawl process."""

import argparse
from parker.workers import crawler

parser = argparse.ArgumentParser(
    description=(
        'Set-up a URI to crawl with the '
        'relevant site configuration.'
    )
)
parser.add_argument(
    'site',
    type=str,
    help='the name of the site (used to load the site config)'
)
parser.add_argument(
    '--uri',
    type=str,
    help='the URI we wish to crawl'
)

args = parser.parse_args()

crawler(args.site, args.uri)
