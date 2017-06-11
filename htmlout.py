#!/usr/bin/env python
#coding:utf8
import sys
#reload(sys)
#sys.setdefaultencoding('utf-8')
class HtmlOut(object):
    def __init__(self):
        self.datas=[]
    def collectData(self,data):
        #if data is None:
        #    return
        #print data
        self.datas.append(data)
    def outHtml(self):
        f=open('html.txt','w')
        reload(sys)
        sys.setdefaultencoding('utf-8')
        for data in self.datas:
            print data['url']
            f.write(data['url']+'\n'+data['title']+'\n'+data['summary']+'\n')
        f.close()
