#!/usr/bin/python

import sys
import re
import requests
import time
import csv
from BeautifulSoup import BeautifulSoup
from requests.exceptions import ConnectionError

DOMAIN = 'beta.betfair.com'
HTTP_DOMAIN = 'http://' + DOMAIN
AGENT = 'Parker/0.5 TimboSpider -- My spidey sense is tingling...'

URLS = [
    u'http://beta.betfair.com/football'
]


def add_url(url, stack):
    if url and url not in stack:
        stack.append(url)


def get_href(link):
    for attr, value in link.attrs:
        if attr == 'href':
            if value[0] == '/':
                return HTTP_DOMAIN + value
            elif re.search(DOMAIN, value) != None:
                return value


def output_data(writer, url, success='SUCCESS', ttlb=0, size=0, configsize=0):
    if size > 0 and configsize > 0:
        perc = '{0:.2f}'.format(configsize / (size / 100))
    else:
        perc = 0

    row = [
        time.strftime('%d-%m-%Y %H:%m:%S'),
        url,
        success,
        ttlb,
        size,
        configsize,
        perc
    ]
    print row
    writer.writerow(row)


def process_url_stack(stack):
    writer = csv.writer(
        open('sportsng-spidered.csv', 'wb')
    )
    headers = {
        'User-Agent': AGENT
    }

    for url in stack:
        try:
            r = requests.get(url, headers=headers)
        except ConnectionError:
            output_data(
                writer,
                url,
                success='FAIL'
            )
            continue
        else:
            begin = time.time()
            soup = BeautifulSoup(r.raw.data)
            ttlb = '{0:.2f}'.format(time.time() - begin)
            for link in soup.findAll('a'):
                add_url(get_href(link), stack)

            scripts = soup.findAll('script')
            size = int(sys.getsizeof(r.raw.data))
            if len(scripts) > 0:
                configsize = int(sys.getsizeof(str(scripts[-1])))
            else:
                configsize = 0

            output_data(
                writer,
                url,
                ttlb=ttlb,
                size=size,
                configsize=configsize
            )


if __name__ == '__main__':
    process_url_stack(URLS)
