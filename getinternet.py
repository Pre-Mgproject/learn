#!/usr/bin/env python
#most from immoc
from bs4 import BeautifulSoup as bs
import urlmanager
import htmldownload 
import htmlparser
import htmlout
class SpiderMan(object):
    def __init__(self):
        self.urls=urlmanager.UrlManager()
        self.download=htmldownload.HtmlDownLoad()
        self.parser=htmlparser.HtmlParser()
        self.output=htmlout.HtmlOut()
        
    def crow(self,url):
        count=1
        self.urls.addNewUrl(rooturl)
        while self.urls.hasNewUrl():
            try:
                newurl=self.urls.getNewUrl()
                print 'crow %d : %s' %(count,newurl)
                htmlcontent=self.download.download(newurl)
                #print 'next'
                #self.parser.printNext()
                newurls,newdata=self.parser.p(newurl,htmlcontent)
                #print 'next'
                #print newurls
                #print newdata
                self.urls.addNewUrls(newurls)
                self.output.collectData(newdata)
                
            except:
                print 'filed'
            count=count+1
            if count==20:
                break
        self.output.outHtml()
if __name__=='__main__':

    rooturl='http://baike.baidu.com/item/Python'
    spider=SpiderMan()
    spider.crow(rooturl)
