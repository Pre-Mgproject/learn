#!/usr/bin/env python
#from immoc
class UrlManager(object):
    def __init__(self):
        self.newurls=set()
        self.oldurls=set()
    def addNewUrl(self,url):
        #if url is None:
        #    return
        if url not in self.newurls and url not in self.oldurls:
            self.newurls.add(url)
    def addNewUrls(self,urls):
        #if url is None or len(urls)==0:
        #    return
        for url in urls:
            self.addNewUrl(url)
    def hasNewUrl(self):
        return len(self.newurls)!=0
    def getNewUrl(self):
        newurl=self.newurls.pop()
        self.oldurls.add(newurl)
        return newurl
            
