dat_9-------->20/03/2024
b. ermiya kumar

2.find the uncommon word from 2 strings
s1="hello how are you"
s2="hello how is"

s1="hello how are you"
s2="hello how is"

s1=s1.split(" ")
s2=s2.split(" ")

for val in s1:
    if val not in s2:
        print(val)
for val in s2:
    if val not in s1:
        print(val)

3.write a code print the 8th fibanochi number
0,1,1,2,3,5,8

num=5
n1=0
n2=1
ans=0+1==>1

n1=1
n2=1
ans=1+1==>2

n1=1
n2=2
ans=1+2==>3

n1=2
n2=3
ans=2+3==>5

for val in range(5):
    ans=n1+n2
    print(ans)

    
#find the 8th fibanochi number
num=8
n1=0
n2=1

for val in range(num):
    ans=n1+n2
    n1=n2
    n2=ans
print(ans)


# ! CONSTRUCTORS

? Eg:2
class profile:
    def_init_(self):
       print("hello world")
obj=profile()
obj._init_()

?Eg:3
# *parametarised constructor
class profile:
    def_init_(self, id, name, age):
       print(id, name, age)

obj=profile(1, "sid", 29)

?Eg:4
class c1:
    email="sid@gmail.com
    name="sid"
    place="cbe"

    def m1(self):
        name="sid"
        place="cbe"
        print(name, place)
        print(self.email)
        
object=c1()
object.m1()

?Eg:5
class c1:
    def m1(self):
        name="sid"
        age=28
        return name, age
    def display(self):
        print(self.m1())

object=c1()
object.display()


?Eg:6---->To use the variable inside the constructor in another method
class class1:
    email=:"sid@gmail.com"-->#static variable
    def_init_(self):
        self.name="sid" -->#instance variable
        self.email="sid@gmail.com"
        return name, email #error-->cannot use return with constructor

    def display(self):
        print(self.name, self.email)

    
c1=class1()
c1.display()

# ! ------->INHERITANCE
The process of utilising the methods and attributes of parent class
throught the object of child class it is called as inheritance

# ? 5 types of Inheritance
1.single inheritance
2.multilevel inheritance
3.multiple inheritance
4.Hybrid inheritance
5.Heirarichal inheritance


# **SINGLE INHERITANCE--------->1
it has only one parent class and only one child class
?Eg:1
class parent:
    def m1(self):
        print("iam parent class")

class child(parent):
    def m2(self):
        print("iam  child class")

obj=child()
obj.m1()

?Eg:2
class c1:
    def_init_(self):
        parent("iam constructor from parent class")

class child1(c1):
    pass

obj=child1()


?Eg:3
class parent:
    name="sidhu"

class child(parent):
    name="name1"
    
    def display(self):
        print(self.name)
        
d=child()
d.display()

#**MULTILEVEL INHERITANCE------------>2
?Eg:1

class voice:
    def sound(self):
        print("all the animal have their own voices")

class dog(voice):
    def dog_voice(self):
        print("bark")
        
class cat(dog):
    def cat_voice(self):
        print("meow")

class parrot(cat):
    def parrot_vioce(self):
        print("speak")
        
all=parrot()
all.dog_vioce()
all.cat_vioce()
all.sound()
all.parrot_voice()


# ! Eg:2
# MRO --> Method resolution Order
class addition:
    def add(self, a, b):
        print(a+b)
        
    def mul(self, a, b):
        print(a%b)
        
class subract:
    def sub(self, a, b):
        print(a-b)
class multiply:
    def mul(self, a, b):
        print(a*b)
class division(addition, subract, multiply):
    def div(self, a, b):
        print(a/b)
        
calc = division() 
# calc.add(3, 4)
calc.mul(4, 2)
        
! heirarical inheritance
the one parent class will acts as parent for all the child class
class catagory:
    def cat_name(self,weight):
        print("weight")

class Tomato:
    def tomato_specs(self):
        color="black"
        taste="neutral taste"


        self.

class carrot (category):
    def tomato_specs(self):

class carrot(category):
    def carrot_specs(self):
        color="green"
        taste="sweet"

c = carrot()
c.carrot_specs()
c.weight("30gms")


#! Hybrid inheritance
The combination of above 4 inheritance is called Hybrid inheritance
class c1:
    def m1(self):
        print("class1")

class c2(c1):
    def m2(self):
        print("class2")

class c3(c2):
    def m3(self):
        print("class3")

class c4(c2):
    def m4(self):
        print("class4")

    def m3(self):
        print("iam m3 from c4")
       

class c5(c4):
    def m5(Self):
        print("class c4")


obj = c6()
obj.m3()

#---->polymorphism

poly - many,morph-->
A function which has the ability to perform more than 1 functionality
then it is considered to be as polymorphism


ploymorphism in built in functions
len()-->which is used to find the length of list,tuple,dict etc..
index()
max()
min()
count()
pop()
and more...

polymorphism in operators
+
print(8+8)
print("k" +'1')
print([1,2,3]+[5,6])



print(6*7)
l1 = {12,3,4,5,6}
print(*11)
def f1(*args)
l1 = [1,2,3,4]
print(l1*10)


polymorphism in classes
we can achieve polymorphism in 2 ways
1.method overloading---->it is not possible in python
2.method overriding











































































        














 











        












