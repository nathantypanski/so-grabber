# Scrapes user lists with BeautifulSoup

from bs4 import BeautifulSoup
from os import path
import requests

from scraper import conf
from scraper import htmlfiles

def snatch_user_list(pageaddress):
    outfile = htmlfiles.userlist_path(pageaddress)
    if not outfile:
        raise ValueError('The URL did not match my expected format')

    if path.exists(outfile):
        print(str.format('Reading {} from saved file.', pageaddress))
        with open(outfile, encoding='utf-8') as f:
            contents = f.read()
        return contents
    else:
        print(str.format('Did not have {}; downloading it ...', pageaddress))
        reqlist = requests.get(pageaddress)
        print(str.format('Contents written to {}', outfile))
        htmlfiles.savecontents(reqlist.text, outfile)
        return reqlist.text
