day 8  19/03/2024
B. ERMIYA KUMAR


2.find the uncommon words from 2 strings
s1="hello  how are you"
s2="hellow how is"


Eg:3
def profile(name,age,place):
    txt="my name is {}.iam {}years old.iam from ():
    print(txt.format(name,age,place))
profile("sid",29,"cbe")    


Eg:4
# ? Function with return sytment
1. a variable declared inside the function can be accessed  outside the functionb using return
2.return does not print anything
3.we cannot  write any code below return statment


def f1():
    z=8
f()
print(z)#error--->cannot use outside the function

def f1(a,b):
    c=a*b
    return c
print(f1(6,8))
obj=f1(6,8)
obj=f1(4,6)

def gracemark(object):
    print(output+4)
gracemark(obj)
gracemark(obj1)    

# problem--1
def palindrome(n):
    string=str(n)
    rev=str(n)[::-1]
    if string==rev:
        print(n, "palindrome")
    else:
        print("not palindrome")
a=int(input("enter the valiue:"))
palindrome(a)


# ? Based on the declatration of parameter and args
# ? function are divided into 5 catagories

*Positional args
*keyword args
*default args
*variable length args
*keyword variable length args


# ***Positional args-----------1
Eg:1
def profile(name,phone,mark):
    txt="my name is {}.my phone number is {}.i I got {}mark."
    print(txt.format(name, phone, mark))

profile(9550271412,"ermiya",97)-->unexpected output

# ***keyword args--------------2
Eg:1
? To overcome the disadvantage of position args, we use keyword args
It is the process  of initialising the paremeter with the args while
calling the function

def profile(name,phone,mark):
    txt="my name is {}.my phone number is {}.i I got {}mark."
    print(txt.format(name, phone, mark))

profile(name="sid", mark=6, phone=123456789)

# todo-->expection of  keyword args functionn
def profile(name, phone, mark):
    txt="my name is {}.my phone number is {}.i I got {}mark."
    print(txt.format(name, phone, mark))

profile(name="sid", 123456789, mark=98) error-->positional args follow keyword
profile(123456789, name="sid", mark=98) error--> name has multiple values
profile("sid", mark=98, phone=123456789)

# ***default args--------------3
The method of assigning the argument to the paremeter while declaring the function

Eg:1
def profile(name, phone, place="kadapa"):
    txt="my name is {}.my phone number is {}.I am from{}."
    print(txt.format(name, phone, place))

profile
("sid", 12346789)

Eg:2
def profile(name,phone,place="kadapa"):
    if place =="kadapa" or place=="KADAPA" or place=="kadapa"
        txt="my name is {}.my phone number is {}.I am from{}."
        print(txt.format(name, phone, place))
    else:
        print("you are not eligible to signup")        
profile("sid", 123456789)


# !exception
def profile(name,place="KADAPA",phone): #error -->coz defalut args should not follow
                                        #positional param 
if place =="kadapa" or place=="KADAPA" or place=="kadapa"
    txt="my name is {}.my phone number is {}.I am from{}."
    print(txt.format(name, phone, place))
else:
    print("you are not eligible to signup")        
profile("sid", 123456789)


# ***veriable length params---------------4
To pass more then 1 args to a paremeter means we use variable length args
to convert normal paremeter to variable length param, add * to there prefix of param

Eg:1
name="sid", "name2", "name3"
def prifile(*name):
    for val in name:
        print("my name is", val)
profile("sid", 'name2', 'name3')

EG:2
def prifile(*name, age):
    for val in name:
        print("my name is", val, "my age is", age)
profile("sid", 'name2', 'name3', 28) error-> age has no args

def prifile(age,*name):
    for val in name:
        print("my name is", val, "my age is", age)
profile(28, "sid", 'name2', 'name3')

# ***keywoed variable length args----------5
kwargs-->which is used to provide the args in the form of key value pair.
Eg:1
def price(**price_list):
    print(price_list)

price(shirt=1000, iphone=80000)


n=5
{1:1, 2:4, 3:9, 4:16, 5.25}

n=int(input("enter the number:"))

def dict1(n):
    d1={}
    for val in ranger(1, n+1):
        d1[val]=val**2
    print(d1)
dict1(5)

# !--------->object oriented programming
the paradings of objected programming are

1.class
2.objects
3.inheritance
4.polymorphism
5.absraction
6.encapsulation

# ! class is a blue print of an object

l1=[1,2,3,4,5,6]

#?Eg:------------------1
class c1:
    name1="sidhu"
    print(name1)
    
#?Eg:------------------2
class person:
    name="sidhu"

c=person() c os object
The process of creation of an object is called as instantition
print(c.name)

#?Eg:------------------3
create of a method
when the function is created with a class  is called as method

class person:
    def display(person):
        print("hello welcome to classes")

p=person()
p.display()

#?Eg:-------------------4
method with parameter
class person:
    def display(person, name, age):
        print(name, age)

p=person()
p.display("sidhu", 28)

#?Eg:-------------------5
class person:
    fname = "sidhu" #attribute or static variable
    fname = "T"
   
    def first_name(self):
        print(self.fname)
             
    def full_name(self):
        print(self fname+" "+self.fname)


p = person1()
p.first_name()
p.full_name()

#?Eg:------------------------6
constructors-->_init_()
this is a special method which has the ablity to execute iotself without
calling it manually through the process of instaliation

class profile:
    def_init_(self): -->constructor method
        print("hey")

p = profile() excution of constructor  through this process




d1{"a":100, "b":200, "c":300}
d1=dict(a=100, b=200, c=300)
print(d1)



























    
