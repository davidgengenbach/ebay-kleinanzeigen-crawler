#!/usr/bin/env python3

import mechanicalsoup
from jinja2 import Template
import json

JSON_IN = 'data/results.json'


def main():
    with open(JSON_IN) as f:
        ads = json.load(f)
    template = Template(open('index.html.tpl').read())
    with open('data/index.html', 'w') as f:
        f.write(template.render(ads=ads))


if __name__ == '__main__':
    main()
