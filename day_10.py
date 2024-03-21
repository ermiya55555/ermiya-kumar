#DAY _10--->21/03/2024 
B. ERMIYA KUMAR

POLYMORPHOISM IN CLASSES
@ we can achieve polymorphism in 2 ways
1.method overloading---->it is not possible in python
2.method overriding

# ! METHOD OVER RIDING
**POLYMORPHISM IN CLASSES

EG:1
class bank:
    def ratio(self):
        print("all bamks has repo rate")

class SBI(bank):
    def ratio(self):
        print("SBI rate is 9%")

class IOB(bank):
    def ratio(self):
        print("IOB rate is 7.5%")

i=IOB()
i.ratio()

s=SBI()
s.ratio()

EG:2
class USA:
    def iangauge(self):
        print("English")
        
     def capital(self):
         print("Washington DC")
         
class india(USA):
    def iangauage(self):
        print("None")
        
     def capital(self):
         print("New delhi")
                 
I=India()
I.langaung()
I.capital()
        

EG:3
polymorphism using objects

c1, c2-->c1=print(c1), print(c2)
f1, f2

class c1:
    def f1(self):
        print("class 1")

class c2(c1):
    def f2(self):
        super().f1()
        print("class 2")

obj1=c2()
obj1.f1()

obj2=c1()
obj2.f1()

EG:4
class c1:
    def f1(self):
        print("class 1")

class c2(c1):
    def f2(self):
        print("class 2")

obj1=c2()
obj2=c1()

def.display(a):
    a.f1()
display(obj1)
display(obj2)

# *changing the functionality of builth functions
EG:5
class shoping:
    def__init__(self, l1):
        self.items=l1
        
    def__len__(self):
        length=len(self.items)
        return length
s=shoping([1,2,3,4,5])
print(len(s))

# ! method overloding
EG:1
class suming:
    def add(self, a, b):
        print(a+b)

    def add(self, a, b, c):
        print(a+b+c)

s=suming()
s.add(4,3) # !---->error
s.add(4,5,1)

EG:2
class summing:
    def add(self, a=None, b=None, c=None):
        if a!=None and b!=None and c!=None:
            print(a+b+c)
        elif a!=None and b!=None:
            print(a+b)
        else:
            print(a)
        
obj=summing()
obj.add(2)
obj.add(3,4)
obj.add(1,2,3)


# !----->abstractioned 
The process of hiding the implimentation details is abstraction

EG:1

from abc import ABC,abstractmethod
class shapes(ABC):
    @abstractmethod
    def sides(self):
        print('All shapes have sides except circle')

class triangle(shapes):
    def triangle_sides(self):
        print("3 sides")

    def name(self):
        print("Iam triangle")
        
    def sides(self):
        pass
    
class square(shapes):
    def square(self):
        print("4 sides")

    def sides(self):
        pass

tr=triangle()
tr.triangel_sides()
tr.name()


#1 RULES TO DEFIND ABSTRACT CLASS1
1.Abstract class cannot be instantiated
2.From abc import ABC, abstractmethod
3.Subclass the normal class with ABC
4.Convert the normal method inside the abstract class to abstract method
5.All the child classes have to be subclassed with abstract class
6.The abstract method should be present in the child classes

EG:2
#*super()-----> used to access the parent class method from child class method
from abc import ABC, abstractmethod
class c1(ABC):
    @abstractmethod
    def m1(self):
        print("this is abstract class")

class c2(c1):
    def m2(self):
        super().m1()
        print("Iam child 1")

    def m1(self):
        pass
    
class2=c2()
class2.m2()


EG:3
from abc import ABC, abstractmethod
class password(ABC):
    @abstractmethod
    def pwd(self):
        pswd="sidd994$"
        return pswd

class login(password):
    def ped(self):
        pass
         
Login=login()
name=input("Enter the name:")
pwd=input("Enter the password:")
Login.validate(name, pwd)

# !**ENCAPSULATION
EG:1
class car:
    __name="BMW" #private variable
    print(__name)
    
c1=car()
print(c1.name) #error
c1.name="Audi"
print(c1.name) #error

EG:2
#? Accessing private data outside the class
class c1:
    __phone='9956473688'

    def display(self):
        print(self.__phone)
        
c=c1()
c.display()

EG:3
#? declare private method
class class1:
    def __m1(self): -->private method
        print("Iam private method")

    def __init__(self):
        self.__m1()
c=class1()
c.__m1() #error

#? nested class
class class1:
    class class2:
        name="sidhu"

        def display(self):
            print(self.name)
    obj1=class2()

obj=class1()
obj.obj1.display()







































