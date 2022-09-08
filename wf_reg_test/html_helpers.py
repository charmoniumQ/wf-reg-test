import itertools
from pathlib import Path
from typing import Mapping, Optional, Sequence, TypeAlias

import domonic  # type: ignore
import domonic as html  # so tags like html.a work.

TagLike: TypeAlias = domonic.dom.Element | str


def html_table(
    elems: Sequence[Mapping[TagLike, Sequence[TagLike]]],
    headers: Optional[Sequence[TagLike]] = None,
) -> domonic.dom.Element:
    if headers is None and elems:
        headers = elems[0]
    if headers is not None:
        thead = [html.thead(html.tr(*[html.td(header) for header in headers]))]
    else:
        thead = []
    return html.table(
        *thead,
        html.tbody(*[html.tr(*[html.td(elem) for elem in row.values()]) for row in elems]),
    )


def html_list(
    elements: Sequence[TagLike], ordered: bool = False
) -> domonic.dom.Element:
    list_factory = html.ol() if ordered else html.ul()
    return list_factory(*[html.li(element) for element in elements])


def html_link(text: TagLike, target: str) -> domonic.dom.Element:
    return html.a(text, _href=target)


def html_fs_link(path: Path) -> domonic.dom.Element:
    return html_link(text=html.code(str(path)), target=f"file://{path.resolve()}")


def highlighted_head(languages: Sequence[str]) -> Sequence[domonic.dom.Element]:
    # for supported langs https://cdnjs.com/libraries/highlight.js
    return [
        html.link(
            _rel="stylesheet",
            _href="https://cdnjs.cloudflare.com/ajax/libs/highlight.js/11.3.1/styles/default.min.css",
        )(),
        html.script(
            _src="https://cdnjs.cloudflare.com/ajax/libs/highlight.js/11.3.1/highlight.min.js",
        )(""),
        *[
            html.script(
                _src=f"https://cdn.jsdelivr.net/gh/highlightjs/cdn-release@11.3.1/build/languages/{lang}.min.js",
            )("")
            for lang in languages
        ],
        html.script("hljs.highlightAll();"),
    ]


def css_rule(selector: str, declarations: Mapping[str, str]) -> str:
    return selector + " {" + css_attribute(**declarations) + "}"


def css_attribute(**declarations: str) -> str:
    return ";".join(
        [
            f"{property.replace('_', '-')}: {value}"
            for property, value in declarations.items()
        ]
    )


def highlighted_code(lang: str, code: str, width: int = 60) -> domonic.dom.Element:
    # see https://highlightjs.org/usage/
    return html.pre(
        html.code(
            **{
                "class": f"language-{lang}",
                "style": css_string(
                    max_width=f"{width}ch",
                    max_height="20vw",
                    resize="both",
                ),
            }
        )(code)
    )


def collapsed(
    summary: TagLike, *details: TagLike, open: bool = False
) -> domonic.dom.Element:
    return html.details(**({"open": ""} if open else {}))(
        html.summary(summary),
        *details,
    )


def html_emoji_bool(val: bool) -> domonic.dom.Element:
    return html.span(
        {
            False: "❌",
            True: "✅",
        }[val]
    )


def br_join(lines: Sequence[TagLike]) -> domonic.dom.Element:
    return html.span(
        *itertools.chain.from_iterable((line, html.br()) for line in lines)
    )


def small(text: str) -> domonic.dom.Element:
    return html.span(text, _style=css_string(font_size="8pt"))
