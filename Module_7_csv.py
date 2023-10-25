# importing datetime function for calculating current date time and formatting date
import datetime
import sys
import os
import shutil
#Importing Functions python program to use case normaliztation logic
import Functions
import re
import csv
# declaring class
class News:
    # declaring class variable now to use it in the methods
    now = datetime.datetime.now()

    def __init__(self,Newscontent,city,inputfile):

        self.inputfile = inputfile
        self.content=Newscontent
        self.city=city
        self.type='News'

        # asking user to input the file name to know the file name which will be created in there local path

    # defining write_file method to write the data to the file
    def write_File(self, text):
        # using open file function to create a new file and using 'a' append mode to add the content to the file continously
        self.newfile=open(str(inputfile), 'a')
        self.newfile.write(str(text))
        self.newfile.close()
        # defining Input_text method to pass the news,advertisement and quote content
    def Input_Text(self):
        # text=input("Input Text - Type the input text data")
        if (self.type == 'News'):
             self.write_File('\n-----News-----------\n' + self.content + '\n')
        elif (self.type == 'Ad'):
            self.write_File('\n----Private Advertisement-----------\n' + self.content + '\n')
        elif(self.type == 'quote'):
            self.write_File('\n-----Quote of the day-----------\n' + self.content + '\n')
        elif (self.type == 'joke'):
            self.write_File('\n-----Joke-----------\n' + self.content + '\n')
    # defining Input_City method to pass city
    def Input_City(self):
        # text=input("Input city")
        self.write_File(self.city + ',')
    # defining datetime method to process and publish current date and expiration days for the advertisement content
    def datetime(self):
        now = datetime.datetime.now()
        if (self.type == 'News'):

            # formating the date to string in the dd/mm/yyyy hh:mm format
            dt_string = now.strftime("%d/%m/%Y %H:%M")
            self.write_File(dt_string)
        else:
            dt_string = now.strftime("%Y-%m-%d")
            # below logic is used to calculate the days between expiration and current date
            exp_date = datetime.datetime.strptime(self.exp_date, "%Y-%m-%d").date()
            date = datetime.datetime.strptime(dt_string, "%Y-%m-%d").date()
            Exp_date = exp_date - date
            self.write_File(str(Exp_date.days) + ' days left')

    # defining read_File to read the data when the user typed inputs are completed
    def read_file(self):

        file1 = open(str(inputfile),'r')
        print(file1.read())
        file1.close()

    def remove_File(self):
        print('\n----Removing The file---------------\n')
        print(inputfile+'.txt')
        os.remove(inputfile+'.txt')

    def Feed(self):


        if(self.type=='News' or self.type=='Ad'):
            self.Input_Text()
            self.Input_City()
            self.datetime()
            self.read_file()
        else:
            self.Input_Text()
            self.read_file()





class PrivateAd(News):
    def __init__(self, content, city, exp_date,inputfile):
        self.content = content
        self.city = city
        self.exp_date = exp_date
        self.type='Ad'
        self.inputfile=inputfile


class Quote(News):
    def __init__(self, quote,inputfile):
        self.content = quote
        self.type = 'quote'
        self.inputfile = inputfile

class Joke(News):
    def __init__(self, joke,inputfile):
        self.content = joke
        self.type='joke'
        self.inputfile = inputfile


#New class to remove the input file and create new file with case normaliztation
class remove_copy:
    def __init__(self,inputfile,tgtfile):
        self.inputfile=inputfile
        self.tgtfile=tgtfile
    def copyfile(self):
        src=self.inputfile
        dst=self.tgtfile
        Source_file = open(src, 'r')
        destination_file = open(dst, 'w')
        #calling Functions python script using import Functions module and using case_change function to normalize the records which we have entered
        destination_file.write(Functions.case_change(Source_file.read()))
        destination_file.close()
        Source_file.close()
        print('New File Created '+'->\''+dst+'\'')

    def removefile(self):
        os.remove(self.inputfile)
        print('Input file \''+self.inputfile+'\''+" removed")


class wordcountcsv:
    def __init__(self,csvfile1,csvfile2,tgtfile):
        self.csv1=csvfile1
        self.csv2=csvfile2
        self.tgtfile=tgtfile
    def writecsvfile1(self):
        d = dict()
        with open(self.tgtfile, 'r') as file:
            for letter in file:
                line1 = letter.strip()
                lines = line1.lower()
                line = re.sub('[^A-Za-z0-9 ]+', '', lines)
                str(line)
                words = line.split(" ")
                # print(words)
                for word in words:
                    #         # print(word)
                    if word in d:
                        d[word] = d[word] + 1
                    else:
                        d[word] = 1

        with open(self.csv1, 'w', newline='') as file:
            headers = ["words", "total_count"]
            test_writer = csv.DictWriter(file, fieldnames=headers,delimiter=',')  # ,quotechar="'",quoting=csv.QUOTE_ALL)
            test_writer.writeheader()
            for k, v in d.items():
                test_writer.writerow({"words": k, "total_count": v})
        print('Wordcount csv created->',self.csv1)

    def writecsvfile2(self):
        d = dict()
        with open(self.tgtfile, 'r') as file:
            for letter in file:
                line1 = letter.strip()
                lines = line1.lower()
                line = re.sub('[^A-Za-z0-9]+', '', lines)
                w = 0
                for word in line:
                    # print(word)
                    w = w + 1
                    if word in d:
                        d[word] = d[word] + 1

                    else:
                        d[word] = 1
            with open(self.csv2, 'w', newline='') as file:
                file.write("letter,letter_count,total_count,percentage\n")
                new = []

                for key, value in d.items():
                    new.append(str(key) + ',' + str(value) + ',' + str(w) + ',' + str(round((value / w) * 100)) + '%')
                for i in range(len(new)):
                    file.write(new[i] + '\n')
                    i = i + 1
            print('Letter count csv created->', self.csv2)


if __name__=='__main__':
    inputfilename=sys.argv[1]
    a = (sys.argv[0].split("\\"))
    b = a[len(sys.argv[0].split("\\")) - 1]
    path = sys.argv[0].replace(b, '')
    print('Text file name:' + path+inputfilename + '.txt')
    inputfile=path+inputfilename+'.txt'
    a=News('important news global warming killing the world climate are changing rapdily ', 'London',inputfile)
    b=PrivateAd('new male sales Representative is required urgently', 'bangalore','2023-10-28',inputfile)
    c=Quote("cleanliness is next to godliness",inputfile)
    d=Joke('why did the kid bring a ladder to school? because she wanted to go to high school.',inputfile)
    a.Feed()
    b.Feed()
    c.Feed()
    d.Feed()
    a = input('\n\'Enter the Target File name:\'->')
    tgtfile=path + a + '.txt'
    e=remove_copy(inputfile,tgtfile)
    e.copyfile()
    e.removefile()
    csvfilename=input('\'Enter the csv file name for words count\'->')
    csvfile2=input('\'Enter the csv file name for letter count\'->')
    csvfile1=path+csvfilename+'.csv'
    csvfile2=path+csvfile2+'.csv'
    sv=wordcountcsv(csvfile1,csvfile2,tgtfile)
    sv.writecsvfile1()
    sv.writecsvfile2()

