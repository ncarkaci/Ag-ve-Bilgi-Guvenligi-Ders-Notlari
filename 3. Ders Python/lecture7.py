#!/usr/bin/env python
#-*-coding: utf-8-*-

import urllib2
import re


def getAllLinksFromWebSite(url):
    #connect to a URL
    website = urllib2.urlopen(url)

    #read html code
    html = website.read()

    #use re.findall to get all the links
    links = re.findall('"((http|ftp)s?://[a-z,A-Z,0-9]+.*?)"', html)

    resultLinkListesi = []
    
    for link, type in links:
        if not (link in resultLinkListesi):
            resultLinkListesi.append(link)
    
    return resultLinkListesi

linkler = getAllLinksFromWebSite("http://www.nytimes.com")

print linkler


def printLinkList(liste):
    
    for item in sorted(liste):
        print item


printLinkList(linkler)
