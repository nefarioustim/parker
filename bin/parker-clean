#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Command-line interface to clear Redis."""

import argparse
from parker.workers import killer

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

killer(args.site)
