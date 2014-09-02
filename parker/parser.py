# -*- coding: utf-8 -*-
"""Parser abstraction that wraps PyQuery for Parker."""

from pyquery import PyQuery
import page
import parsedpage

_parsed = dict()


def parse(page_to_parse):
    """Return a parse of page.content. Wraps PyQuery."""
    global _parsed
    if not isinstance(page_to_parse, page.Page):
        raise TypeError("parser.parse requires a parker.Page object.")

    if page_to_parse.content is None:
        raise ValueError("parser.parse requires a fetched parker.Page object.")

    try:
        parsed = _parsed[page_to_parse]
    except KeyError:
        parsed = parsedpage.ParsedPage(
            page=page_to_parse,
            parsed=PyQuery(page_to_parse.content, parser='html')
        )
        _parsed[page_to_parse] = parsed

    return parsed
