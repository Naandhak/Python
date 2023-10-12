# import string library function
import string
#import regular expression function
import re 
#copying the sentence to variable a
a='''	tHis iz your homeWork, copy these Text to variable. 

	You NEED TO normalize it fROM letter CASEs point oF View. also, create one MORE senTENCE witH LAST WoRDS of each existING SENtence and add it to the END OF this Paragraph.

	it iZ misspeLLing here. fix“iZ” with correct “is”, but ONLY when it Iz a mistAKE. 

	last iz TO calculate nuMber OF Whitespace characteRS in this Text. caREFULL, not only Spaces, but ALL whitespaces. I got 87.
'''
#Converting the sentence to proper case using title function
r=a.title()
#print(r)
#Intializing c variable for counting
c=1
for i in a:
    #using string whitespace function to find the whitespace characters in the sentence
    if i in string.whitespace:
        c=c+1
print('Total number of whitespace characters '+str(c))

#regular expression findall function to search for last words in each existing sentence
match=re.findall(r'\w+\.', a)
# for loop to add the words from above list to the paragraph
for m in match:
    a=a+' '+ m.replace('.','')
#create one MORE senTENCE witH LAST WoRDS of each existING SENtence and add it to the END OF this Paragraph.
print('\n ADDING NEW LINE \n'+a)