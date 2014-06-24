#!/usr/bin/env python

from os import path
import argparse

from scraper import listscraper

argsparser = argparse.ArgumentParser(description='Download user pages from Stack Overflow.')
argsparser.add_argument('-s', '--scrape',
                  action='store_true',
                  help='scrape the website for user pages')

def main():
    args = argsparser.parse_args()

    userlistdir = 'userlists'
    userpagedir = 'userpages'

    if args.scrape:
        listscraper.snatch_user_list('http://stackoverflow.com/users')

if __name__ == '__main__':
    main()
