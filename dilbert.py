#!/usr/bin/env python
import time
import hashlib
import random
import urllib2
from BeautifulSoup import BeautifulSoup
from datetime import datetime, time, timedelta

def fetch_comic(comicname, fetch_timeout):
    dateformat = '%Y-%m-%d'
    comictitle = "Dilbert"

    now = datetime.now()
    today = now.today()
    today_str = today.strftime(dateformat)

    try:
        url = 'http://dilbert.com/strip/' + today_str
        headers = { 'User-Agent' : 'Toonbot/1.0' }
        req = urllib2.Request(url, None, headers)
        site = urllib2.urlopen(req, timeout=fetch_timeout).read()
        soup = BeautifulSoup(site)
        title = (soup.find("img", attrs={'class':'img-responsive img-comic'})["alt"]).encode('utf8')
        comic = 'https:' + (soup.find("img", attrs={'class':'img-responsive img-comic'})["src"]).encode('utf8')
        link = url
        prehash = comic
        hash = hashlib.md5()
        hash.update(prehash)
        comichash = hash.hexdigest()
        text = None
        return (True, comichash, title, comic, text, link, comicname, comictitle)

    except Exception, e:
        return (False, None, None, None, None, None, comicname, comictitle)
