#!/usr/bin/env python
class Person(object):
    def __init__(self,name,score):
        self.name=name
        self.score=score
    def __repr__(self):
        return '(Person:%s,%s)'%(self.name,self.score)
   
    def __cmp__(self,s):
        if self.score==s.score:
            return cmp(self.name,s.name)
        return -cmp(self.score,s.score)
class Student(object):
    def __init__(self,*args):
        self.names=args
    def __len__(self):
        return len(self.names)
p=Person('bob',20)
p1=Person('andy',30)
p2=Person('bluce',80)
p3=Person('alice',10)
p4=Person('char',20)
s=Student('bob','andy')
print len(s)
l=[p,p1,p2,p3,p4]
print sorted(l)
print p

