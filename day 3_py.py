DAY THREE 13/03/2024
ermiya kumar

eg:3
? take the value of length and breadth of a
? from user and check if it is square or not

length=int(input())
breadth=int(input())
if length ==breadth:
    print("its not square")
else:
    print("its not square")
    
eg;4
? python program to check whether the
? given integer is a multiple of both 5 and 7

n=int(input("enter the number:")
if n%5==0 and n%7==0:
      print("yes")
else:
    print("no")

eg:5
? write a program to accept the cost price of a bike and display the
? road tax to be paid
? according to the following criteria:

cost price (in RS)              Tax
>100000                         15% + discount 6%
<100000                         5%


price = int(input("enter the price:")) 
amount = 0
if price>=100000:
    disccount=price*(6/100)
    value=price-discount
    tax=value*(15/100)
    total=value+tax
else:
    tax=price*(5/100)
    total=price+tax
    print("the onroad cost of bike is:",total)


!----> if elif else
eg:1
a=7
b=9
c=3

if a>b and a<c:
    print("A is greater")
elif b>a and b>c:
    print("B is greater")
elif c>a and c>b:
    print("C is greater")
    

A school has following rules for grading system:
a. below 25-f    
b. 25 to 45-e
c. 45 to 50-d
d. 50 to 60-c
e. 60 to 80-b
f. above 80-a
ask user to enter marks and print the corresponding grade.

mark=int(input("enter mark:"))
if mark>=80 and mark<=100:
    print("A")
elif mark>=60 and mark<=80:
    print("B")
elif mark>=50 and mark<=60:
    print("C")
elif mark>=40 and mark<=50
    print("D")
else:
    print("fail")

    
    
eg:6
? accept the age of 4 people and display the oldesgt one.

!--> short hand if else
eg:1
a=9
b=60
if a>b:
    print("A")
else:
    print("B")
?--> using short hand if else
* rules
1.statement inside the if condition have to be present at frist
2.elif cannot be uesd in short hand if else
3.always it have to end with else

print("A") if a>b else print("B")

# ! code to check the given char is vowel or consonent
char=input("enter the char:")
if char=="a" or char=='e' or char=='1' or char=='0' or char=='u':
    print("is a vowle")
else:
    print("its consonent")


# ? or
str1="aeiouAEIOU"
if char in str1:
    print("vowle")
else:
    print("consonent")
    
# ! shorthand if else
char=input("enter the char")
str1="aeiouAEIOU"
print("vowles") if char in str1 else print("consonent")


# !--> elif ladder using short hand if else
eg:
? find greatest among 3 variables using short hand if else
a=8
b=5
c=9

print("A is greater") if a>b and a>c else print("B is greater")
if b>a and b>c else print ("C is greater")


[**---AFTER NOON 13/03/2024---**] 1:00pm to 5:00pm 

# !---->{LOOPING CONCEPT}
1. looping can be implimented using
2. for loop
3. while loop

#--> for loop
?for loop is used for itertion, if we know the number of times the loop have to run
?it is used to iterayte the iterables eg(string, list, tuple, ect..)


# todo---> syntax for loop

! for syntax in c
for(i=0;i<10;i++){
    printf("hello");
  }
! for syntax in python
for userdefine variable in rtange(start,end,step): default step value is 1
  statement
  statement
  statement
   
eg;1
to print the value from 1 to 10 using for loop

for i the range(0,10): (n,n-1)
     print(i)
     print("hello")

eg:2
for val in range (1,15,2):
    print(val)
    
eg:3
to decrement the value 

for val in range(10,0,-2):
    print(val) 

for val in range(10,0,1):
    print(val) no output
    

eg:4
# ? print the output of 7th multiplication table from 21 to 43

for val in range(1,10+1,):
    print (val*7)

for val in range(1,10+1,):
    print ('7','x',val,'=', val*7)--> method:1
      
for val in range(1,10+1,):  
    ans="7 x {}={}"
      print(ans.format(val,val*7)---->method:2

for val in range(1,10+1,):
    print(f" x {val}={val*7}")--->method:3

for val in range(1,10):
            if val==6:
            break
        print(val)

eg:6
for val in range(1,10):
        print(val)
        if val==6:
        break
eg:7
for val in range(1,10):
            if val==6:
        print(val)
        break
    
# ! continue
eg:1
for val in range(1,10):
    if val==6:
        continue
    print(val)
        
# ! practise problems
print the even number beytween 20 to 40

for val in range(20,40):
    if val %2==0:        
       print(val)

# !--->while loop
?while is used when we do not know the number of times the loop have to run
?to iterate the non iterable elements while is used

# todo syntax
 
1. initialisation
2. while condition
3.  statement
4.  incre or decre

eg:1
to interate number from 1 to 10

i=0
while i<11:
    print(i)
    i=i+1 or i+=1

eg:2
to decrement using while loop
i=10
while i>0:
    print(i)
    i-=1 

# for loop practise
?write a program to display sum of odd numbers and even
 numbers that fall between
 12 and 37(including both numbers)

#---> assesment
1. cats and mous:hacker rank
2. print the factorla of 8 using for loop
3. write a program to display sum of odd numbers and even numbers that
   fall between 12and37(including both numbers)
4. write code to print 





















                      
























    
