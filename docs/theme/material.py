import os

import sass
from bs4 import BeautifulSoup


def get_stylesheet() -> str:
    base_path = os.path.abspath(os.path.dirname(__file__))
    style = ""
    for src in ["../css/extra.css"]:
        filename = os.path.join(base_path, src)

        with open(filename, 'r') as f:
            style += f.read()
    return style


def get_script_sources() -> list:
    base_path = os.path.abspath(os.path.dirname(__file__))
    return list(map(lambda src: os.path.join(base_path, src),
                    ['../js/mermaid.min.js', '../js/mermaid_window.js', '../js/mermaid_loader.js']))


def inject_link(html: str, href: str) -> str:
    soup = BeautifulSoup(html, 'html.parser')

    footer = soup.select('.md-footer-copyright')
    if footer and footer[0]:
        container = footer[0]

        container.append(' ... ')
        a = soup.new_tag('a', href=href, title='PDF',
                         download=None, **{'class': 'link--pdf-download'})
        a.append('download PDF')

        container.append(a)

        return str(soup)

    return html

