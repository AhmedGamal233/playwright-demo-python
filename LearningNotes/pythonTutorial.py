import re
from playwright.sync_api import Page, expect

def test_homepage_has_Playwright_in_title_and_get_started_link_linking_to_the_intro_page(page: Page):
    page.goto("https://playwright.dev/")

    # Expect a title "to contain" a substring.
    expect(page).to_have_title(re.compile("Playwright"))

    # create a locator
    get_started = page.get_by_role("link", name="Get started")

    # Expect an attribute "to be strictly equal" to the value.
    expect(get_started).to_have_attribute("href", "/docs/intro")

    # Click the get started link.
    get_started.click()

    # Expects the URL to contain intro.
    expect(page).to_have_url(re.compile(".*intro"))

"""
this is NOT multi line commnent its multi line string
"""
print(type(10))
print(type(10.9))
print(type("str"))
print(type([1,2,3])) #list
print(type((1,2,3))) #tuple
print(type({"name":"ahmed","age":23})) #dict
print(type(True))
_g =5
myName="ff"
koko1 =33
happy_birthDay="thanks"
x=10
x="dd"  #normal causepython is interpreted language
a,b,c=1,2,"ff"
#escape chars
#============
#\b like back space
#\newline 
cc="gggg\
gggg"
cc="ggg\"koko\"" #\\ or \' or \"
#\n like Enter
#\t make tab
print(cc+' '+x)

Mystring ='fffff'
Mystring ="dddddd"
Mystring ="dddddd 'fffff'" # or 'ddddddd "tttt"'
Mystring =""" fgfdgdfg
dfgdfgdf
fgfdgdf
fgdgf""" #trible qoute for multi line

#all data type are objects
#zero indexing for strings ,lists,tuple
##can make operators with strings and lists and tuples
print(Mystring[0])
Mystring[-1] #negative from last
#slicing
#Mystring[Start:End] #end not include
#Mystring[Start:End:step]
#Mystring[index:] from index till end
#Mystring[:] all data
#Mystring[0::1] all data
#Mystring[::1] all data

#string Methods
len(Mystring) #length
Mystring.rstrip() #remove spaces from right only
Mystring.lstrip() #remove spaces from left only
Mystring.strip() #remove all spaces right and left (not removing middle spaces)
Mystring.strip("d") #remove d all spaces right and left

Mystring.title() # all first letters will be capital even (3g => 3G)
Mystring.capitalize() # all first letters will be capital but what after num will be same 

a,b,c ="1","11","111"
a.zfill(3) #001
Mystring.upper() #make all capital
Mystring.lower() #make all small

Mystring.split() #convert string to list splitted by space by default
Mystring.split("-",2) #seperator is - and 2 is max split will be two times
Mystring.rsplit() #reverse split mn el a5er ll awel
Mystring.center(5) #if str is 3 chars it will be space+str+space
Mystring.center(5,"#") #+str+#
Mystring.count("d",0,5) #num of occurance of str 0 start 5 end not counted
Mystring.swapcase() #all capital become small and viseversa
Mystring.startswith("")
Mystring.endswith("")
#Mystring.index("substring",0,3) #start(optional) ,end(optional) for searching on string ,if not found will gives error
Mystring.find("")  #start(optional) ,end(optional) for searching on string ,if not found will gives -1 DE A7SAN
Mystring.istitle()
Mystring.isspace()
Mystring.islower()
Mystring.replace("old","new",2) #2 is num of replacment optional
"seperator".join(Mystring)
# formatting at old way like c language
c=1.3445
x=2
print("my is %s and %d and %.3f" %(Mystring,x,c))

#formatting new way
print("my is {} and {} and {}".format(Mystring,x,c))

print("my is {:s} and {:d} and {:.3f}".format(Mystring,x,c))

#truncate {:5s} will take only 5 chars

#formatting from version 3.6+

print(f"my is {Mystring} and {x} and {c}")

z=100
float(100) # to convert to float
a=12.55
int(a)

#List []
#======
#List is not array
#ordered and indexed
#mutable
#duplicated not unique
#can be with different data type
#can be sliced like strings
##can make operators with strings and lists and tuples
ListStudent=[1,"fff",1.55,True]
ListStudent[0]
ListStudent[-1]

#ListStudent[Start:End] #end not include
#ListStudent[Start:End:step]
#ListStudent[index:] from index till end
#ListStudent[:] all data
#ListStudent[0::1] all data
#ListStudent[::1] all data

#can edit list with assgin one element or with slice 
ListStudent[0]="11"
ListStudent[1:3] =[123,"gg"]
#Method
ListStudent.append("alaa") #any type add at last of list (you can appened list in list with for loop)
ListTeacher=[1,"ffww1f",1.5335,True]
ListStudent.append(ListTeacher) #[1,"fff",1.55,True,[1,"ffww1f",1.5335,True]] 

ListStudent[4][0] #1

# (you can appened list in list with for loop will not put as list put element by elemnet)
# OR
ListStudent.extend(ListTeacher) #[1,"fff",1.55,True,1,"ffww1f",1.5335,True]

ListStudent.remove(1) #will remove first matching elemnt
#Sorting must on list have same data type
listo =["a","g","K"]
listo.sort() #Asend
listo.sort(reverse=True) #Decend

ListStudent.reverse() #just reversing not concern on data type
ListStudent.clear() #[]
a= ListStudent.copy()

ListTeacher.count(1) #occurance of elemnt
ListTeacher.index(1) # get index of fist element match

ListStudent.insert(3,"object need to be insert") #where 3 is index
ListStudent.insert(-1,"object need to be insert") #insert at last

ListTeacher.pop(2) #get element in index 2
ListStudent.pop(-1)

#tuple ()
#======
# ordered indexed
# immutable can't be changed (add or edit or delete)
#duplicated not unique
#can be with different data type
TupleStudent =(1,"ee",True,[1,4,5])
TupleTeacher=(1,"ffww1f",1.5335,True)
TupleStudent[0]
#to change in tuple you can use operators but you can operate with immutable data tupes only (int,sets,strings) Not applicable with lists and Dict
Newtuple =TupleStudent+TupleTeacher+(3,4,"ff")
TupleStudent*3 
##can make operators with strings and lists and tuples

#Set {}
#======
# NOT  ordered NOT indexed NOT SLICING
# mutable 
#to change in tuple you can use operators but you can operate with immutable data tupes only (int,sets,strings) Not applicable with lists and Dict
#Set must be with unique items (remove any dublication by default)
Set1 ={3,"r",True}
Set2={55,"H",False}
Set1.union(Set2) # == Set1 | Set2 or Set1.update(Set2) 
Set2.clear()
Set2.add("dd")
Set2.remove("dd") #if not exist raise an error
Set2.discard("Dd") #if not exist will NOT raise error
Set2.difference(Set1) #just difference set1-set2
Set2.difference_update(Set1) # will update original set(Set2) with values of difference
Set2.intersection(Set1) #just common values
Set2.intersection_update(Set1) # will update original set(Set2) with values of common
Set2.symmetric_difference(Set1) #not common
Set2.symmetric_difference_update(Set1)  # will update original set(Set2) with NOT common values

#Dictionary {"key": value}
#=======================
#key should bt immutable type (string tuble int)
#key should be unique if duplicate will take last key
#values any data type
#access element with key
#dict it self is mutable
user ={
    "name":"ahmed",
    ("e","v"):"ee",
    1:2,
    "skills" :["dd","ff"]
    
}
user["skills"]
#or
user.get("name")
user.keys()
user.values()

user={
    "One":{ "name":"ahmed",
    ("e","v"):"ee",
    1:2,
    "skills" :["dd","ff"] },

    "two":{ "name":"ahmed",
    ("e","v"):"ee",
    1:2,
    "skills" :["dd","ff"] }
    
}
user["two"]["name"]
len(user)
#value can be assgin dict
DictOne={ "name":"ahmed", ("e","v"):"ee", 1:2,"skills" :["dd","ff"] }
Dicttwo={ "name":"ahmed", ("e","v"):"ee", 1:2,"skills" :["dd","ff"] }
user={
    "one":DictOne,
    "two":Dicttwo
}

user.clear()
user.update({"country":"Egy"})
newDict =user.copy()
# dictoo ={"key":None} #None like none
# dictoo.setdefault({"key":"default"})

user.popitem() #return last item added on dict
user.items() #return all pairs in dict (all keys and values) --> returns as [(key1,value1),(key2,value2),(key3,value3)]

a=("key1","key2","key3")
b="value"
user.fromkeys(a,b) # {"key1":"value","key2":"value","key3":"value"}

#Boolean isKaza
#======
bool(0) #or [] or '' or "" () or {}or None all is false 
#Operator
age=30
age >23 and age<0 or age<-1 
not age<20
#asginment and comparasion operator same as all languages

#type converison
a=10
str(10) #=>"10"
tuple("string or list or set or dict") #number cant be ,dict takes only key
list("")#dict takes only key
set("") 
dict("") #string not ,set not,tuple must be nested((,),(,),(,)),list must be nested 

#user input
input()
vero =input("put your input")
vero.strip().capitalize()

if(True): #or if True without parentethes 
    print("ff")
    if a<100:
        print("ff")
elif(False):
    print("dd")
else:
    print("fff")

print("movie is sutible" if age >18 else "move is forbbiden") #ternanry

#match like switch
lang="Python"
match lang:
    case "JavaScript":
        print("You can become a web developer.")

    case "Python":
        print("You can become a Data Scientist")
    case "Java":
        print("You can become a mobile app developer")
    case _:
        print("The language doesn't matter, what matters is solving problems.")

#mempership operators

l =["osama","ahmed","mohamed"]
if "osama" in l:
    print("ok")  #true
if "sayed" not in l:
    print("ok") #true

a=0
while a<len(l) :
    print("koko")
    a+=1

myNums =[1,3,4,6,4,33,2,2,33,4]

for numbers in myNums:
    print(numbers)
    if numbers %2 ==0:
        print("even")
    else:
        print("odd")
else:
    print("this else used at end of for loop")

nums =range(0,100)
for num in nums :
    print(num)

#dictionary
DictOne={ "name":"ahmed", ("e","v"):"ee", 1:2,"skills" :["dd","ff"] }
for diko in DictOne:
    print(DictOne[diko])
    print(DictOne.get(diko))
    for skill in DictOne["skills"]:
        print(DictOne.get("skills"))

for name,nameValue in DictOne.items(): #here you don't need to make key.get(value)
    print(nameValue)

DictOne={ "name": {"CSS" :"44","HTML":"55"} ,"add": {"ff" :"44","kk":"55"}  }
for name,nameValue in DictOne.items(): 
    print(nameValue)
    for childKey,childValue in nameValue.items():
        print(childValue)

#break(stop),continue(skip),pass(accept)

#pass use with any think not coded yet

if a<100:
    pass

def printValue():
    print("gjgjgj")

printValue()  #you must invoke function after definition

def getValue(NUMBERValue,StringValue):
    return StringValue+str(NUMBERValue)

print(getValue(20,"ffff"))
Value =getValue(20,"ffff")

#Packing and unpacking
#=====================

#make function accept any number of parameters (*KAWrgs)

def multiParamtersFun(*parameters):
    for items in parameters:
        print(items)

multiParamtersFun("d","r",1)

# to make defualt 
def defaultParam (name="dd"): #default value should be form last one to left Or all parameters have default values
    return name

#**KWArgs for any number of key,value of dictionary 
def multidictFun(**dictionaries):
    for key,value in dictionaries.items():
        print(f"{key} and its {value}")
        for valueKey,Valuevalue in value.items():
            print(f"{valueKey} and its {Valuevalue}")


DictOne={ "name": {"CSS" :"44","HTML":"55"} ,"add": {"ff" :"44","kk":"55"}  }
multidictFun(**DictOne)

#convert local var to global

x=2
def convert():
    global x
    return x

'''Anynomousfunction 
(has no name ,
can call inline without define ,
can call it in return data from another func,
not block of code)'''

anynou = lambda age : age*2
anynou2 = lambda name,age: f"{age*2} {name}ee"
print(anynou2("ff",10)) #20 ffee

#file handling
#=============
# "a" -> open file for append values ,create file if not exist
# "r "->[Deafult value if not written in method] read file , if not exist will give error
# "w" -> open file to write , create file if not exist
# "x" -> create file ,gives error if file exist 

#path absolute or relative
import os
print(os.getcwd()) #current working directory #/Users/ahmed-abdelhaliem/Downloads/pythonLearning
print(os.path.abspath(__file__)) #directory of oppened file (firstest.py)
path=os.path.abspath(__file__) #/Users/ahmed-abdelhaliem/Downloads/pythonLearning/.vscode/re/firsttest.py
print(os.path.dirname(path)) #/Users/ahmed-abdelhaliem/Downloads/pythonLearning/.vscode/re
file =open(r"filepath.txt","r")
print(file.name) #details of file
print(file.encoding) #details of file
# print(file.read())
# print(file.readline())
# print(file.readlines())
# print(file.readlines(5))
#note read take all inside file if you run read lines after it will gives empty list
file.close()
file =open(r"filepath.txt","w")
file.write("Ahmed in the house\n") # in write it will override all in the file and put new values of write
l=["ff",'gg',"dd"]

file.writelines(l)
file =open(r"filepath.txt","a") #old not removed

file.truncate(5) #5 chars
file.tell() #tell me numbers of characters ,enter(\n) =4

# import os
# os.remove("file path")

#built in function

x=[1,2,4,5,[]]
if all(x): #return true if all list value is itretable
    print("kaka")

if any(x): #return true if at least one of list values is  itretable
    print("kakaa")
xx=[1,2,4,3,5,6]
print(sum(xx))
g=12.44554
print(round(g)) #12 if .6 or higher 13
print(round(g,3)) #12.445
print(list(range(0))) #[]
print(list(range(10))) #[0,1,2,3,4,5,6,7,8,9] not 10 cause its range-1
print(list(range(0,10,2))) #[0,2,4,6,8] not 10 cause its range-1  (start,range,step)

print("hello","Ahmed","how","are","you",sep='@') #default seperator space hello@Ahmed@how@are@you

print("hello",end="") # deafult end is \n
print("Ahmed")

abs(-12) #any int or float to positive
min(xx) #any iterator
max(xx) #any iterator

#linke slicing item[:] [2:5]
slice(5) #from 0 to 5 wehere 5 (end) not including
slice(2,5) #start int

#map takes function ,iterator
#==
#can map function on all items of iterator
#can use lambda or normal function
def addEnter(text):
    return f"{text}"

l=["ff",'gg',"dd"]
dataAfter =map(addEnter,l)
print(dataAfter)
for data in dataAfter:
    print(name)
#with ananymous
dataAfter =map(lambda text:f"{text}",l)

#filter takes function ,iterator
#====
#can filter out all element of iterator that  function gives true on them (boolean value)
#can use lambda or normal function


def checkNum(num):
    if num>10:
        return True 
    #or return num>10 direct
s=[34,56,1,2,3,8]   
filter(checkNum,s)
for filteredData in filter(checkNum,s):
    print(filteredData)

#with ananymous
filter(lambda num : num if(x >10) else False,l)

#if you filtered on values like 0 it will return false so but result of condition as True not value itself

#reduce takes function ,iterator
#======
#takes first and second element and make operation on them -> result taken with third and make operation -> result with fourth and so on
#can use lambda or normal function



#enumerate
l=["ff",'gg',"dd"]
enumerate(l) # will add counter on element enumerate(l,counter start optional)
for items in enumerate(l):
    print(items)
for counter,items in enumerate(l):
    print(f"{counter}:{items}")
    
#reversed
for items in reversed(l):
    print(items)
    
#help
help(enumerate) #give me info about method i dont understand it

#Modules
#file contain set of functions
#by import you can use this module
#can make multi modules
#can make your own module
import random
print(f"get random number {random.random()}")

#if i want to import one function or two from module
from random import randint
print (randint(0,1000)) #we write name of function only cause we import only randint

from random import randint,randrange 
from random import *  ## like import random

#to make your own module 

# 1- 
import sys
sys.path.append(r"path of module py file")

# 2-

# import yourModule as alisName  #as to give him alias name not contradict with any other modules

# if vs code can't see module from setting.json add "python.autoCompelete.extraPaths" :["module path"]

#external package
#===============
#Module vs package => module is single file with its own functions , package is number of modules
# to download package and its dependency from pip (package manager of python like npm in Js or maven/gradle in java) https://pypi.org/
# https://pip.pypa.io/en/stable/  pip manual
# pip instal <name od package> <name of another package and so on>
# pip install <name od package> == no. of package version  or >= this version or higher
#pip instal --user pip --upgrade
# if imported package gives unresolved package , it's bug in vs code -> solution from code palette - reload window

#date & time
#===========
import datetime

datetime.datetime.now()# => current date
datetime.datetime.now().year # => current year
datetime.datetime.now().day # => current day

datetime.datetime.now().min # => or max

datetime.datetime.now().time # => current time

datetime.datetime.now().time().hour # => current hour same sec same minute

#max/min at time only olso

# date formatted https://strftime.org/

#iterable vs iterator
#====================
#iterable :object contains Data , can be iterable like (String, list ,set ,tuple,dictionary) ,int and float not iterable
#========

#Iterator :what responsible for loop on iterable object using next()
#========
#to call iterator you can user iter()
#for loop have iter() and call it in BG

ss="Ahmed"
myIterator = iter(ss) #put iterable object inside

next(myIterator) #A  this is the method that keep calling at BG until last element

#so
#for letter in ss : #== for letter in iter(ss): 


#Generator
#=========
#function use yeild word instead of return ->why? return for returning data , yeild for producing data
#support iteration and return iterator by
#can have more than one yeild (but at return it's one)
#generator starts from the place that you call the yield
#not run automatically it just gives you control to make actions

def generator():
    yield 1
    yield 2
    yield 3
    yield 4

print(next(generator())) # wil print 1 and stop on it until you use next(generator() again it will resume from where i stopped)
for gen in generator():
    print(gen)

# #decorator (meta programing)
# #==========================
# #for butify functions and enhance its behaviours
# #takes function as a parameter(decorator is higher order function)

def my_decorator(function): #decorator no paramter
    '''m'''
    def nested_func(*args):
        print("before")
        function(*args)
        print("After")
    return nested_func

# @my_decorator
# def sayHello():
#     print(f"Hello")   
# # decUse =myDecorator(sayHello)    #this WRONG implementation instead put @my_decorator above method and call it normally
# # decUse()
# sayHello()

def sum_decorator(function): #decorator with paramter
    '''mm'''
    def neste_func(*nums):
        '''m'''
        for num in nums:
            if(num > 0 or num<0):
                function(*nums)
                break;
    return neste_func

@my_decorator
@sum_decorator
def sum_num(num1,num2):
    '''this is docstring for documentation '''
    print(num1+num2)

sum_num(0,9)
# #we can put morethan one decorator above func

#make docs
# '''this is docstring for documentation '''
#to call docs
# help(sum_num)
# dir(sum_num.__doc__)

#Exception
#---------
try:
    # code that may cause exception
    sum_num(0,9)
except ZeroDivisionError:
    print("Denominator cannot be 0.")
    
except IndexError:
    print("Index Out of Bound.")
except:
    # code to run when exception occurs, put at last after specific exceptions
    print("Denominator cannot be 0.")
else:
        print("used if there is no error mlhash lazma awy")
finally:
    print("This is finally block.")
    
# to put my own exception => raise Exception(my code) or put specific error raise IndexError(code)


#type hint
def sum_num(num1,num2) ->int:
    '''this is docstring for documentation '''
    print(num1+num2)
    
#Regular expression
#=================
#sequence of characters to define search/validation pattern 
#https://www.debuggex.com/cheatsheet/regex/python regx cheat sheet
# to test regex https://pythex.org/

#\d ==> highlight all digits
#\D ==> highlight all NON digits
#\s ==> highlight all spaces
#\S ==>highlight all not spaces
#\w ==>highlight all words(numbers and chracters and _)
#\W ==>highlight all Non words (symboles and special characters and spaces)
#\d\d ===>highlight digits 2digits by 2digits  == \d{2}
#\d\s ==> highlight digit+space
#\d\s\d ==>highlight digit+space+digit
# .=> any chrachter except newLine(with enter)
#charachter+\w ==> highlight needed char+one after   or vice versa \w+char
#charachter+\s ==> highlight needed char+space   or vice versa \s+char
#[a-<character from a to z>] ==> all chracter matches till this specific character  for capital [A-<character from a to Z>]
#[^a-<character from a to z>] ===>NOT chracter matches till this specific character for capital [^A-<character from a to Z>]
#[0-9]
#[^0-9]
#[a-zA-z] == [A-z]
#^	Start of string
#$  End of string

#\w* ==> * means 0 or more
#\w+ ==> + means one or more
#\w? ==> ? means 0 or 1
#\d{2} \anysympbol{no.of occurance} => no. of thing depend on w d s .etc
#\anysympbol{no.of occurance,no.of occurance } => range of ex: {2,4} 2 or 3 or 4
#{2,} =>2 or more
#{,2} ==> up to 2 

#regex for phonr number ^\d{3}-?\s?\d{4}-?\s?\d{3}$

#| or   ex com|net
#\ escape characters like \. to get dot in .com
#() group ex ^(https?://)(www\.)(\w+)(\.)(com|net|org)$

#note : grouping not prefered if you want full value of website as example https?://www\.\w+\.net|com|org

#use regex at python

import re

result=re.search(r"regex","what i search on it") #find first mach only
result.group() #return match result

def checkPattern():
    if result:
        return True
    else:
        return False

re.findall("regex","what i search on it") #return a list of all match results if not will return empty list []

result=re.search(r"regex","what i search on it",re.DOTALL) #will match newline also

result=re.search(r"regex","what i search on it",re.IGNORECASE) #not care about capital or small letter

result=re.search(r"regex","what i search on it",re.MULTILINE) #will search on all lines


#####################################################################################################
#OOP
####
#__init__ its dunder/majic method Loke consructor in java
#self is like this in java ,points to instance(object) of class (init must have self and must be first parameter) (can be with any name)
# def __init__(self,other parametersif it will be parametrized object):
#constructor in python its pramatrized (self,parameters) OR non-parameterized (self) ##can't be BOth##
class Employee:
    not_allaowed_Names=["toto","koko","soso"] #this is class attribute ,be outside constructor 
    counterUsers =0
    empList=[]
    # def __init__(self):
    #     print("hello object")
    def __init__(self,name,address,gender):
        self.name =name #name is instance attribute be inside constructor
        self.address=address
        self.gender=gender
        for empo in Employee.not_allaowed_Names:
            if self.name==empo:
                raise ValueError("not allowed")
            else:
                print(f"hello {name}")
                break
                    
    def getInfo(self):
        return self.address,self.gender
        
    def work(self):   #work is method attribute  ,must add self
        print(f"{self.name} who is info {self.getInfo()} works hard") 
    @classmethod   
    def addUser(cls,*emps):
        for emp in emps:
            Employee.counterUsers+=1
            Employee.empList.append(emp)
    @classmethod 
    def deleteUser(cls,*emps):
        for emp in emps:
            Employee.counterUsers-=1
            Employee.empList.remove(emp)
    @classmethod
    def check_counter(cls):
        return cls.counterUsers
    @staticmethod
    def isEmpexist(emp):
        if emp in Employee.empList:
            return 'True'
        else:
            return 'False'
    def __str__(self):
        return f"this is class represent company employees"

'''
Class method vs Static Method

The difference between the Class method and the static method is:

A class method takes cls as the first parameter while a static method needs no specific parameters.
A class method can access or modify the class state while a static method can’t access or modify it.
In general, static methods know nothing about the class state. They are utility-type methods that take some parameters and work upon those parameters. On the other hand class methods must have class as a parameter.
We use @classmethod decorator in python to create a class method and we use @staticmethod decorator to create a static method in python.

When to use the class or static method?

We generally use the class method to create factory methods. Factory methods return class objects ( similar to a constructor ) for different use cases.
We generally use static methods to create utility functions.
'''
        
        
#instantiate object
#=================
#emp= Employee()

emp=Employee("samy","cairo","male")
emp1=Employee("ge","cairo","male")
emp2=Employee("samy","cairo","male")
Employee.addUser(emp,emp1,emp2)
print(Employee.isEmpexist(emp))
print(Employee.check_counter())
Employee.deleteUser(emp,emp1)
print(Employee.isEmpexist(emp))
print(Employee.check_counter())
emp.name
emp.work()

#Magic method
#============
#__init__ type of magic methods
emp.__class__ #to know which class that the object 
mySTR ="fffff"
print(emp) #tocheck __str__
#print(dir(Employee))

#inheretance
#===========
class Baseclass:
    def __init__(self,name):
        self.name=name
        print("base")
    def eat(self):
        print("Base to eat")
        
class DerivedClass(Baseclass):
    def __init__(self,name,price):
        # Baseclass.__init__(self,name) #to inhert base clase attrbutes 
        # #or
        super().__init__(name)
        self.price =price
        print("dervied")
    # def eat(self): #override method 
    #     print("derived to eat")
    def eat(self):   
        return super().eat()
    @property #if you have method with self only and just return value you can use @property to call it as attribute line
    def drink(self):
        print("dervid")
        

der =DerivedClass("dodo",88)
der.eat()
#der.drink() #this will gives error if you put @property decorator
#or
der.drink #if you put @property decorator
    
#multi inheretance
#=================
class BaseOne:
    def __init__(self):
        print("baseOne")
        
class BaseTwo:
    def __init__(self):
        print("basetwo")
        
class Derived(BaseOne,BaseTwo): #inheretance done by order of base classes
    pass

my_Der= Derived()  #==> print base one caues of order of inheritance
print(Derived.mro()) #to see order of execution of init [<class '__main__.Derived'>, <class '__main__.BaseOne'>, <class '__main__.BaseTwo'>, <class 'object'>]

class Baso:
    pass
class Devo1(Baso):
    pass
class Devo2(Devo1): #will inherite both of Devo1 and baso also
    pass

#overloading

#overriding


#encapsulation in python just naming convention its not restrict from call method or attri. like java as example
class encaps:
    def __init__(self,__private,_protected):
        self.__private=__private #two__
        self._protected=_protected #one_
        print("baseOne")


en =encaps("DD","gg")
en.__private ="ff"
print(en.__private)

#also getter and setters just concepts for private att.

#absract class is class with one or more abstract method ,can NOT be instantiate

from abc import ABC, abstractmethod

class Abs (ABC):
    
    @abstractmethod
    def absMethod(self):
        pass
    
class used(Abs):
    def __init__(self) -> None:
        super().__init__()
    def absMethod(self): #must be created or it will gives TypeError: Can't instantiate abstract class used with abstract method absMethod
        print("abstracted")
    
u=used()

