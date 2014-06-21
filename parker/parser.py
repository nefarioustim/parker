# -*- coding: utf-8 -*-
"""Parser abstraction that wraps PyQuery for Parker."""

from pyquery import PyQuery
import page
import parsedpage


def parse(page_to_parse):
    """Return a parse of page.content. Wraps PyQuery."""
    if not isinstance(page_to_parse, page.Page):
        raise TypeError("parser.parse requires a parker.Page object.")

    if page_to_parse.content is None:
        raise ValueError("parser.parse requires a fetched parker.Page object.")

    return parsedpage.ParsedPage(
        page=page_to_parse,
        parsed=PyQuery(page_to_parse.content, parser='html')
    )
