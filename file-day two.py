DAY TWO 12/3/2024
variable
eg:
  a,b=c=7,8
  print(a)
  print(b)
  print(c)
ans:
  7
  8
  (7,8)

#----> swapping of variables
a=7
b=5
eg:1
temp=a temp=7
a=b a=5
b=temp b=7
a=5, b=7
print(a,b)

eg:2
a=a+b a=12
b=a-b b=12-7=5
a=a-b a=12-5=7
print(a,b)

a,a=b,a only in python
print (a,b)


a=a*b #a=35
b=a/b #b=35/7=5.0
a=a/b #a=35/5=7.0
print(int(a),int(b))


id()-->used to find the memory address of the variable
a=7
b=8
print(id(a))
print(id(b))

--->keywords
keywords are reserved words which provides special meaning 
compiler or interpretor


import keyword
print(keyword.kwlist)
print(len(keyword.kwlist))
print(type(keyword.kwlist))

to check if the string is keyword or not
print (keyword.iskeyword("sib") false

!----> LITERALS
#literal is the constent value assigned to a variable
#a variable is considers to be constant when it is defines
#in caps


a=78 a is variable
A=78 a is constant

       
1.hash()--> it creates a hash value for constant datatype and
 provides error for non constant datatypes
       
n1=89*7j
print(hash(n1))

f1=[7,8,9]
print(hash(f1)) # error ---> list is non constant or mutable datatype

!----->OPERATORS
?OPEARTORS are symbols which is used to perfeorm various opeartions
?between 2 or more opeartors

#Arithmatic
#Assignment
#Logical       
#Relational or comparison
#Bitwisen
#Identity
#Membership

#1. TODO-->ARITHMATIC-->[+,-,*,/,%,//,**]       
EG;
a=8
b=6
c=9
print(a+b+c)

input()-->used to get the runtime input
n1=input ("enter the value:")
print(type(n1))       
       

n1=eval(input("enter the value"))
print(type(n1))    

a=4
b=2
print(a/b) is used to get the quotient value
print(a%b) is used to get the remainder value


AFTERNOON 12/03/2024

!  //--> floor devision
a=765433
b=19
print(a/b)-->the output will be in integer & the output will be
based on floor value 

!  **-->used for power of a number
print(a**b)-->16       

#2.ASSIGMENT--> +-=,-=,/=,*=,//=,**=,&=,|=,%=

a=8
a+=2      
print(a)

a=30
a-=5
print(a)

#3.comparsion-->  ==,>,<,!=,<=,>=
a=8       
b=7
print(a>b)

a=9
b=5
primnt(a==b)

#4.BITWISE OPERATOR---> &,|,^,~,<<,>>
a = 7
b = 4   
print(a&b)  

2^4 2^3 2^2 2^1 2^0
8   4   2   1

0   1   1   1  #-->7
0   1   1   0  #-->6&
---------------
0   1   1   1


~--->
       
a=9877
print(~a)  only for one compliment 1to0,0to1 conversion

a=9
128 64  32  16  8  4  2  1
 0   0   0   0  1  0  0  1 #-->9

 1   1   1   1  0  1  1  0 #--> -10


0  0  0  0  1  0  1  0--> 10
       
1  1  1  1  0  1  0  1-->1s compliment of 10
                     1-->2s compliment of 10
------------------------
1  1  1  1  0  1  1  0--> -10


 <<, >>
       
print(5<<1) left shift right shift opeartors

256  128  64  32  16  8  4  2  1
  0    0   0   0   0  0  1  0  1  3<
  0    0   0   1   0  1  0  0  0-->40
 107
       

#5.LOGICAL OPEARTORS (and, or, not)

a=6
print(a>3 and a<10)
print(a>7 or  a<30)
print(not(a>8 and a<10))


#6.IDENTITY OPEARTOR (is, is not)
    ?it is used to compare the memory location that the value is, is not
a=8
b=8
print(a is b)
print(a==b)

a=[1,1,1]
b=[1,2,3]
print(a is b) we get false

a=[1,2,3]
b=[1,2,3]       
print(a is not b) we get true

#7.MEMBERSHIP(in, not in)
11=[7,8,9,0,6,5]
num=5
print(num in 11)
print(num not in 11)

       
num=678
print(8 in num) we get error
       
#**CONDITIONAL STATEMENT(if, elif, else)

---->c syntax       
   if (condition){
       statement;
       statement;
       statement;
}
eg:1
   a=6
   if a:    
print("hello")

eg:2
   a=6
if a>3:   
print("hey")
else:
print ("no")

eg:3
if 7>8:
print("hello")

eg:4
a=0
a=none
a=false
a=""
if a:
    print("yes")
else:
    print("no")

a number is even or odd

n=int(input("enter the number:"))
if n%2==0
     print(n,"is even")
else;
     print(n,"is odd")
















       
