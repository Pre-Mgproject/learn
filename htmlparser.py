#!/usr/bin/env python
#from imooc
from bs4 import BeautifulSoup as bs
import urlparse
import re
class HtmlParser(object):
    def p(self,pageurl,htmlcount):
        #if pageurl is None or htmlconut is None:
        #    print 'none'
        #    return None
        print 'parse'
        soup=bs(htmlcount,'html.parser',from_encoding='utf-8')
        newurl=self._getNewUrl(pageurl,soup)
        #print newurl
        newdata=self._getNewData(pageurl,soup)
        return newurl,newdata
    def _getNewUrl(self,pageurl,soup):
        newurls=set()
        links=soup.find_all('a',href=re.compile(r"/item/*"))
        #print links
        for link in links:
            #print link
            newurl=link['href']
            #print newurl
            fullurl=urlparse.urljoin(pageurl,newurl)
            #print fullurl
            newurls.add(fullurl)
        return newurls
    def _getNewData(self,pageurl,soup):
        pydata={}
        pydata['url']=pageurl
        title=soup.find('dd',class_="lemmaWgt-lemmaTitle-title").find('h1')
        pydata['title']=title.get_text()
        summary=soup.find('div',class_="lemma-summary")
        pydata['summary']=summary.get_text() 
        return pydata
    def printNext(self):
        print 'next'
