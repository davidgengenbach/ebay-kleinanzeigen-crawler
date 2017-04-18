#!/usr/bin/env python3

from attrdict import AttrDict
import mechanicalsoup
import json

JSON_OUT = 'data/results.json'


def main():
    args = get_args()
    browser = mechanicalsoup.Browser()
    results = []
    for page_num in range(args.page_start, args.page_end):
        results += get_results(browser, args.url, page_num)
    with open(args.json_out, 'w') as f:
        json.dump(results, f, indent=4, sort_keys=True)

    render(results)


def get_args():
    import argparse
    parser = argparse.ArgumentParser(description='Crawl ebay kleinanzeigen', formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('--url', default='https://www.ebay-kleinanzeigen.de/s-64283/%s/l4896', help='The start url. Must have a [percent-sign]s portion in the url to insert the "options" like the page num, price etc.')
    parser.add_argument('--page-start', default=1, type=int, help='The page number to start at')
    parser.add_argument('--page-end', default=10, type=int, help='The page number to end at')
    parser.add_argument('--json-out', default=JSON_OUT, help='The path for the output json.')
    parser.add_argument('--options', default='preis:0:20/', help='Options for kleinanzeigen. Get from the site')
    args = parser.parse_args()
    args.url = args.url % (args.options + '/%s')
    return args


def render(ads):
    from jinja2 import Template
    template = Template(open('index.html.tpl').read())
    with open('data/index.html', 'w') as f:
        f.write(template.render(ads=ads))


def get_results(browser, url, page):
    page = browser.get(url % ('seite:' + str(page)))
    # Dirty
    domain = '/'.join(url.split('/')[0:3])
    results = []
    for el in page.soup.select('article.aditem'):
        out = AttrDict()
        out.link = domain + el.select('a[href^="/s-anzeige"]')[0].attrs['href']
        out.title = el.select('.text-module-begin a')[0].text.strip()
        out.desc = el.select('.aditem-main p')[0].text.strip()
        addetails = el.select('.aditem-details')[0]
        out.price = addetails.select('strong')[0].text.strip()
        out.added = el.select('.aditem-addon')[0].text.strip()
        img = el.select('[data-imgsrc]')
        out.img = img[0].attrs['data-imgsrc'] if len(img) else None
        results.append(out)
    return results

if __name__ == '__main__':
    main()
