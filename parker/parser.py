# -*- coding: utf-8 -*-
"""Parser abstraction that wraps PyQuery for Parker."""

from pyquery import PyQuery
from parker import page, parsedpage

_parsedpages = dict()


def parse(page_to_parse):
    """Return a parse of page.content. Wraps PyQuery."""
    if not isinstance(page_to_parse, page.Page):
        raise TypeError("parser.parse requires a parker.Page object.")

    if page_to_parse.content is None:
        page_to_parse.fetch()

    return parsedpage.get_instance(
        page=page_to_parse,
        parsed=PyQuery(page_to_parse.content, parser='html')
    )
