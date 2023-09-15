#create list of 100 random numbers from 0 to 1000

import random
#Importing the random library package
l=[]
i=0
while i<100:
    l.append(random.randrange(0,1000))
    i+=1
print(l) #print the random number between 0 and 1000


#sort list from min to max (without using sort())

for i in range(0,len(l)):
    for j in range(i,len(l)): #to compare 1 value with multiple values in the list
        if(i==j):
            continue #skip to avoid comparsion on the same value
        elif(l[i]>l[j]): #to compare 1 value with multiple values in the list
            m=0 #define m=0 value to store the value for temporary
            m=l[i]
            l[i]=l[j]
            l[j]=m
        else:
            continue

print(l)


#calculate average for even and odd numbers and print both average result in console 

es=0 # define es value to store even numbers total on each iteration
os=0 # define os value to store odd numbers total on each iteration
ce=0 # define ce value to count the total number of even numbers on each iteration
co=0 # define co value to count the total number of odd numbers on each iteration
for i in range(0,len(l)):
    if(l[i]%2==0): # to check if the number is divisible by 2 to determine it is even number or not
        e=l[i]+es
        es=e
        ce=ce+1
    
    else:
        o=l[i]+os
        os=o
        co=co+1
print("Length of List",len(l))
print("Count of even numbers",ce)
print("Count of odd numbers",co)
print("Average of even numbers",es/ce)
print("Average of odd numbers",os/co)

