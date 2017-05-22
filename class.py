#!/usr/bin/env python
import types
def func(self,heigh):#this is a function
    return heigh

    
class Person(object):
    _state_='well down'#this is a class property
    count="class method"
    @classmethod
    def method(cla):
       return cla.count
    def __init__(self,name,age):
        self.name=name#this is a instance property
        self.age=age
        self.job='teacher'
    def jobs(self,score):#this is an method
        return score
#a method call who am i ,the fallowing instance all has the same method exthed from person 
    def whoami(self):
        return self.name
       
class Student(Person):
    def __init__(self,name,age,score):
        super(Student,self).__init__(name,age)
        self.score=score
    def whoami(self):
        return self.name
#create a class that does not extend from Person and has a methed call whoami()
class Book(object):
    def __init__(self,name):
        self.name=name
    def whoami(self):
        return self.name
#there is a function call who_am_i
def who_am_i(x):
    return x.whoami()
    
xiaoming=Person('haha','1')
print xiaoming.name
print xiaoming.age
print xiaoming.jobs(20)
print xiaoming.jobs
print Person._state_
xiaoming.get_heigh=types.MethodType(func,xiaoming,Person)
print xiaoming.get_heigh(172)
print "----------------this is a class method------------------"
print Person.method()
xiaohong=Student('xiaohong','2',50)
print xiaohong.score
print 'is xiaohong a instance of Person? '
print isinstance(xiaohong,Person)
book=Book('book')
print who_am_i(book)
print who_am_i(xiaoming)
