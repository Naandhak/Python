#importing string and random function
import random
import string
#create a list of random number of dicts (from 2 to 10)
#empty List is created to have dictonaries created in it
values=[]
#using below for loop created 3 dictonaries
for i in range(0,3):
    d={random.choice(string.ascii_lowercase):i for i in range(11)}
    print(d)
    #inserting each dictonary into the list 'value'
    values.insert(i,d)
#creating empty dictonary
new_dict={}
#and copying the empty dictonary to master
master=new_dict.copy
#using below for loop comparing first 2 dictonary in the list and inserting into new dictornary 'new_dict'
for i in range(0,3):
    if(i<1):
        for key,value in values[i].items():
            for key1,value1 in values[i+1].items():
                if(key==key1):
                    if(values[i][key]>=values[i+1][key1]):
                        new_dict.setdefault(key+'_'+str(i+1),value)
                    else:
                        new_dict.setdefault(key1+'_'+str(i+2),value1)
                else:
                    new_dict.setdefault(key,value)
                    new_dict.setdefault(key1,value1)
#copying the comparsion values of dict 1 and dict 2 from the 'value' list into master to avoid iteration issue 
master=new_dict.copy()
 #comparing 3rd list with newly created dict 'new_dict'
    for i in range(0,3):
        
        if(i>1):
            
            for key,value in master.items():
                for key1,value1 in values[i].items():
                    if key.split('_')[0]==key1:
                        if(master[key]<values[i][key1]):
                            new_dict.setdefault(key1+'_'+str(i+1),values[i][key1])
                            new_dict.pop(key)
                        else:
                            
                            continue
                    else:
                        new_dict.setdefault(key1,value1)
                        