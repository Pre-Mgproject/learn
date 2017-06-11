#!/usr/bin/env python
#from immoc
import urllib2
class HtmlDownLoad():
        
    def download(self,url):
        if url is None:
            return None
        res=urllib2.urlopen(url)
        if res.getcode()!=200:
            return None
        #print res.read()
        return res.read()

