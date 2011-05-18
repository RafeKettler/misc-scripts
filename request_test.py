#!/usr/bin/env python
"""
CDN tester for SO. Designed to make lives easier.

Usage:
python request_test.py # for default number of tries, 20
python request_test.py 100 # for a specific number of tries

Rafe Kettler, 2011
See the file LICENSE for the license.
"""
import sys
import urllib2
from time import time

sites = {'sstatic'  : 'http://sstatic.net/js/full.js',
         'NetDNA'   : 'http://sstatic.stackexchange.netdna-cdn.com/js/full.js',
         'Amazon'   : 'http://d1d5ue6vu5b30i.cloudfront.net/js/full.js',
         'EdgeCast' : 'http://wac.43df.edgecastcdn.net/8043DF/sstatic/js/full.js',
        }

def measure_response_time(url, requests):
    total_time = 0
    for i in range(requests):
        start = time()
        urllib2.urlopen(url).read()
        elapsed = time() - start
        total_time += elapsed
    return float(total_time * 1000) / requests

if __name__ == '__main__':
    try:
        tries = int(sys.argv[1])
    except IndexError:
        tries = 20
    for name, url in sites.items():
        average_response = measure_response_time(url, tries)
        print "%s: %fms average over %d tries" % (name, average_response, tries)
