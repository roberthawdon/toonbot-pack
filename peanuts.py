#!/usr/bin/env python
import time
import hashlib
import random
import urllib2
from BeautifulSoup import BeautifulSoup
from datetime import datetime, time, timedelta

def fetch_comic(comicname, fetch_timeout):
    comictitle = "Peanuts"

    try:
        url = 'http://www.gocomics.com/peanuts/'
        headers = { 'User-Agent' : 'Toonbot/1.0' }
        req = urllib2.Request(url, None, headers)
        site = urllib2.urlopen(req, timeout=fetch_timeout).read()
        soup = BeautifulSoup(site)
        comic = (soup.find("meta", attrs={'property':'og:image'})["content"]).encode('utf8')
        link = (soup.find("input", attrs={'title':'Get the Permalink'})["value"]).encode('utf8')
        prehash = comic
        hash = hashlib.md5()
        hash.update(prehash)
        comichash = hash.hexdigest()
        title = None
        text = None
        return (True, comichash, title, comic, text, link, comicname, comictitle)

    except Exception, e:
        return (False, None, None, None, None, None, comicname, comictitle)
