#!/usr/bin/env python3

from attrdict import AttrDict
import mechanicalsoup
import json

PRICE = 'preis:0:20'
URL = 'https://www.ebay-kleinanzeigen.de/s-64283/{}/seite:{}/l4896'.format(PRICE, '{}')
JSON_OUT = 'data/results.json'


def main():
    browser = mechanicalsoup.Browser()
    page_num = 1
    page_max = 10
    results = []
    for i in range(page_num, page_max):
        results += get_results(browser, URL, i)
    with open(JSON_OUT, 'w') as f:
        json.dump(results, f, indent = 4, sort_keys = True)

def get_results(browser, url, page):
    page = browser.get(url.format(page))
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