import re
import os
from os import path

from scraper import conf

def savecontents(contents, pathname):
    """ Write contents to a file, creating necessary directories.
    """
    _maybe_mkdir(pathname)
    with open(pathname, 'w') as htmlfile:
        htmlfile.write(contents)

def userpage_path(address):
    """ Returns a path to the user page file where address would be saved.
    """
    return path.join(conf.userpagedir, match_userpage(address))

def userlist_path(address):
    """ Returns a path to the user list file where address would be saved.
    """
    return path.join(conf.userlistdir, match_userlist(address))

def match_userpage(address):
    """ Get the output path for an individual user's page.

    Returns the user's name if successful, None if we didn't find a match.
    """
    user_page_fmt = re.compile(r'^.*stackoverflow\.com\/users\/\d+\/\(.*\)$')
    username = user_page_fmt.match(address)
    if username:
        return username.group(0)
    else:
        return None

def match_userlist(address):
    """ Get the output path for a user list page.

    Returns the user's name if successful, None if we didn't find a match.
    """
    userlist_subpage = re.compile(r'^.*stackoverflow\.com\/users?page=\(\d+\).*$')
    top_userlist = re.compile(r'^.*stackoverflow\.com\/users$')

    subpage = userlist_subpage.match(address)
    if subpage:
        return subpage.group(0)

    top = top_userlist.match(address)
    if top:
        return conf.mainpagename

    else:
        return None

def _maybe_mkdir(pathname):
    dirpath = path.basename(pathname)
    if not path.exists(dirpath):
        os.makedirs(dirpath)
