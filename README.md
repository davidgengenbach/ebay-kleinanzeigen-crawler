# eBay Kleinanzeigen Crawler

Just a little project to waste some time.

## Instructions
```bash
pip3 install -r requirements.txt
./crawl.py
open data/index.html
```

## Usage
```
usage: crawl.py [-h] [--url URL] [--page-start PAGE_START]
                [--page-end PAGE_END] [--json-out JSON_OUT]
                [--options OPTIONS]

Crawl ebay kleinanzeigen

optional arguments:
  -h, --help            show this help message and exit
  --url URL             The start url. Must have a [percent-sign]s portion in
                        the url to insert the "options" like the page num,
                        price etc. (default: https://www.ebay-
                        kleinanzeigen.de/s-64283/%s/l4896)
  --page-start PAGE_START
                        The page number to start at (default: 1)
  --page-end PAGE_END   The page number to end at (default: 10)
  --json-out JSON_OUT   The path for the output json. (default:
                        data/results.json)
  --options OPTIONS     Options for kleinanzeigen. Get from the site (default:
                        preis:0:20/)
```