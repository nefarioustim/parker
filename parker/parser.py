# -*- coding: utf-8 -*-
"""Parser abstraction that wraps PyQuery for Parker."""

from pyquery import PyQuery
from parker import page, parsedpage


def parse(page_to_parse):
    """Return a parse of page.content. Wraps PyQuery."""
    if not isinstance(page_to_parse, page.Page):
        raise TypeError("parser.parse requires a parker.Page object.")

    if not page_to_parse.content:
        page_to_parse.fetch()

    return parsedpage.get_instance(
        page_to_parse,
        page_to_parse.content,
        PyQuery(page_to_parse.content, parser='html')
    )
