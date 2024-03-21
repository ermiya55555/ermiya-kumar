day_4  14/03/2024


#---->while loop

#---->break using while loop

eg:1
1.iterate from 20 to 30 and break the loop in 27

i=20
while i<31:
    if i==27:
       break
    print(i)
    i+=1

eg:2
i=20
while i<31:
    print(i)
    i+=1
    if i==27:
       break
    
eg:3
i=20
while i<31:
    print(i)
     if i==27:
        break
     i+=1

eg:4
i=20
while i<31:
    if i==27:
        print(i)
       break
    i+=1

# !----> continue
eg:1
i=20
while i<31:
    if i==27:
       continue
    print(i)
    i=i+1
    
eg:2
i=20
while i<31:
     i=i+1
    if i==27:    
       continue
    print(i)

eg:5
# while to iterate from 12 to 22
# find the sum of all numbers 

i=12
sum=0
while i<23:
    sum=sum+i
    i+=1
print(sum)


# ! eg;6
find the averange of value from 20 to 30

i=20
sum=0
count=0
while i<=30:
    sum=sum+i
    count+=1
    i+=1
print(sum/count)


#---->Nested for loop
eg:1

for i in range(1,3):
 for j in range(1,4):
    print(i,j)


for row in range(1,3+1):
 for col in range(1,4+1):
    print(row,col)


eg:2
*  *  *  *
*  *  *  *
*  *  *  *
*  *  *  *

for row in range(4):
 for col in range(4):
    print(row, col)
    

for row in range(1,4):
 for col in range(1,4):
    print("*")


for row in range(4):
    for col in range(4):
        print("*", end=" ")
    print()


rows=int(input("enter the rows:"))
cols=int(input("enter the cols:"))        

for row in range(rows):
    for col in range(cols):
        print("*", end=" ")
    print()
    

AFTERNOON 14/03/2024

#! to print stars in right angled triangle

for row in range(0,6):
    for col in range(0,row+1):
        print("*", end=" ")
    print()

#----> list

---->data types
primary

1,numbers-->int,float,complex
2,string
3,boolean
4,none

collection
1,list
2,tuple
3,set
4,dictionary

--->list

1.if the collection of elements are surrounded by square brackets,it is considered
to be list
eg:
    11=[4,7,9,9,89,"hello",7+9j,[8,9,0]]

characteristics of list
1.list have to be surrounded by[]
2.it is mutiple (the elements in the list are changable)
3.every element inside list is indexed
4.the elements inside list will be ordered format
5.it can hold duplicate values
6.its heterogenous

To access the elements in list
11=[1,4,1,7,89,7,7,5,"p","i"]
   print(l1)

#----> list

---->data types
primary

1,numbers-->int,float,complex
2,string
3,boolean
4,none

collection
1,list
2,tuple
3,set
4,dictionary

--->list

1.if the collection of elements are surrounded by square brackets,it is considered
to be list
eg:
    11=[4,7,9,9,89,"hello",7+9j,[8,9,0]]

characteristics of list
1.list have to be surrounded by[]
2.it is mutiple (the elements in the list are changable)
3.every element inside list is indexed
4.the elements inside list will be ordered format
5.it can hold duplicate values
6.its heterogenous

To access the elements in list
11=[1,4,1,7,89,7,7,5,"p","i"]
   print(l1)

--->indexing
in the collection datatypes like list,tuple,string,the elements will be alloted
with pre-defined unique value called index value

we have 2 types of indexing
positive indexing -->starts with 0 from left hand side
Negitive indexing-->starts with -1 from left to right


positive indexing
print(lst1[0])
print(lst1[4])
print(lst1[20])--> error


#? ---->negative indexing
lst1=[1, 4, 1, 7, 89.7, 7.5, "p", "i"]
print(lst1[-1])
print(lst1[-5])


# ?----> SLICING
lst1=[1, 4, 1, 7, 89.7, 7.5, "p", "i"]
lst1[start_index:end_index:step]

print(lst1[0:4])
print(lst1[6:8])
print(lst1[3:6])
print(lst1[:5])
print(lst1[3:])
print(lst1[:])

print(lst1[0:7:1]) lst1[0:7]--> both are same
print(lst1[0:7:2])

trail=int(input())
lst1=[1, 4, 1, 7, 89.7, 7.5, "p", "i"]
print(lst1[-4:-1])
print(lst1[-1:-4])--> []
print(lst1[-7:-1])
print(lst1[-7:-1:2])

#! to insert at add element inside list 

append()-->used to add element at last position of list 
l1=[9, 8, 0, 6]
l1.append("car")
print(l1)


        
 


















    
s1="hello world to all"














