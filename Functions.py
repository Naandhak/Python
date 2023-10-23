# -------------------------------writing the Module 2 Collection (Dictonaries) task using function--------------------------------



# importing string and random function
import random
import string



# using below for loop created 3 dictonaries
def create_dict(n):
    for i in range(0, n):
        d = {random.choice(string.ascii_lowercase): i for i in range(11)}
        #print('Dict', i + 1, '\n', d)
        # inserting each dictonary into the list 'value'
        values.insert(i, d)
    return n, values


def empty_dict(new_dict):
    # and copying the empty dictonary to master
    a = new_dict.copy
    return a


def compare(values, n):
    # using below for loop comparing first 2 dictonary in the list and inserting into new dictornary 'new_dict'

    for i in range(0, n):
        if (i < 1):
            for key, value in values[i].items():
                for key1, value1 in values[i + 1].items():
                    if (key == key1):
                        if (values[i][key] >= values[i + 1][key1]):
                            new_dict.setdefault(key + '_' + str(i + 1), value)
                        else:
                            new_dict.setdefault(key1 + '_' + str(i + 2), value1)
                    else:
                        new_dict.setdefault(key, value)
                        new_dict.setdefault(key1, value1)
    #print(new_dict)
    #master=empty_dict(new_dict)
    master=new_dict.copy()
    # comparing 3rd list with newly created dict 'new_dict'
    if (i > 1):
        for key, value in master.items():
            for key1, value1 in values[i].items():
                    if key.split('_')[0] == key1:
                        if (master[key] < values[i][key1]):
                            new_dict.setdefault(key1 + '_' + str(i + 1), values[i][key1])
                            new_dict.pop(key)
                        else:
                            continue
                    else:
                        new_dict.setdefault(key1,value1)
        return new_dict


# calling Function
if __name__ == '__main__':
    # create a list of random number of dicts (from 2 to 10)
    # empty List is created to have dictonaries created in it
    values = []
    # creating empty dictonary
    new_dict = {}

    n, values = create_dict(3)
# Compare user defined function which takes the output of Create_Dict produces the list of dictonaries and the total number of dictonaries to be compared
    compare(values, n)

# -------------------------------------------------writing the Module 3 strings task using function----------------------------------------------------------
# import string library function
import string
# import regular expression function
import re

# copying the sentence to variable a

# using decorator to add AFTER CHANGE before calling each function for readability
def test_decorator(func):
    def wrapper(a):
        print('\n')
        print('------------------------------------AFTER CHANGE---------------------------------------\n')
        returned_value=func(a)
        print(returned_value)
        return returned_value

    return wrapper



# function to change from letter CASEs point of view
def case_change(a):
    return a.title()


# function to find the whitespace characters in the sentence
@test_decorator
def whitespace_count(a):
    c = 1
    for i in a:
        # using string whitespace function to find the whitespace characters in the sentence
        if i in string.whitespace:
            c = c + 1
    return 'Total number of whitespace characters ' + str(c)

@test_decorator
def replace(a):
    x = re.sub("iz|iZ|Iz|IZ", "is", a)
    return x


@test_decorator
def add_words_to_paragraph(a):
    # regular expression library findall function to extract last words from each sentence
    match = re.findall(r'\w+\.', a)
    # for loop to add the words from above list to the paragraph
    for m in match:
        a = a + ' ' + m.replace('.', '')
    # create one MORE senTENCE witH LAST WoRDS of each existING SENtence and add it to the END OF this Paragraph.
    return a


if __name__=='__main__':
    a = '''	tHis iz your homeWork, copy these Text to variable. 

	You NEED TO normalize it fROM letter CASEs point oF View. also, create one MORE senTENCE witH LAST WoRDS of each existING SENtence and add it to the END OF this Paragraph.

	it iZ misspeLLing here. fix“iZ” with correct “is”, but ONLY when it Iz a mistAKE. 

	last iz TO calculate nuMber OF Whitespace characteRS in this Text. caREFULL, not only Spaces, but ALL whitespaces. I got 87.
    '''


# calling functions
# function to change the case in the paragraph
    print("\n-------------------Case Change----------------------------\n")
    a=case_change(a)
    print("\n------------------Iz replace is---------------------------\n")
    c=replace(a)
# function to count the number of whitespaces in the paragraph
    #whitespace_count=test_decorator(whitespace_count)
    print("\n-----------------Whitespace count-----------------------------\n")

    b=whitespace_count(c)
#function to replace 'iz' to 'is'

# function to append the last word from each sentence to the last paragraph
    print("\n----------------add words to paragraph------------------------\n")
    add_words_to_paragraph(c)


