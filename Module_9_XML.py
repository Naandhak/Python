# importing datetime function for calculating current date time and formatting date
import datetime
import sys
import os
import json
import shutil
#Importing Functions python program to use case normaliztation logic
import Functions
import re
import csv
import xml.etree.ElementTree as ET

# declaring class
class Feed:
    # declaring class variable now to use it in the methods
    now = datetime.datetime.now()

    def __init__(self,inputfile,content='None',city='None',type='None',exp_date='2023-12-31',json_dict={}):

        self.inputfile=inputfile
        self.content=content
        self.city=city
        self.type=type
        self.exp_date=exp_date
        self.format=inputfile.split('.')[1]
        self.json_dict={}
        self.outputfile=inputfile.split('.')[0]+'.txt'
    def write_File(self, text):

        # using open file function to create a new file and using 'a' append mode to add the content to the file continously
        if(self.format=='txt'):
            self.newfile=open(str(self.inputfile), 'a')
            self.newfile.write(str(text))
            self.newfile.close()
        elif(self.format=='json'):

            self.newfile = open(str(self.outputfile), 'a')
            self.newfile.write(str(text))
            self.newfile.close()

        elif(self.format=='xml'):

            self.newfile = open(str(self.outputfile), 'a')
            self.newfile.write(str(text))
            self.newfile.close()

    def Input_Text(self):
        if (self.type == 'News'):
             self.write_File('\n-----News-----------\n' + self.content + '\n')
        elif (self.type == 'Ad'):
            self.write_File('\n----Private Advertisement-----------\n' + self.content + '\n')
        elif(type == 'quote'):
            self.write_File('\n-----Quote of the day-----------\n' + self.content + '\n')
        elif (type == 'joke'):
            self.write_File('\n-----Joke-----------\n' + self.content + '\n')
    def Input_City(self):
        if(self.format=='txt'):
            self.write_File(self.city + ',')
        elif(self.format=='json'):
            self.write_File(self.city + ',')

    def datetime(self):
        if (self.type == 'News'):

                # formating the date to string in the dd/mm/yyyy hh:mm format
                dt_string = Feed.now.strftime("%d/%m/%Y %H:%M")
                if (self.format == 'txt'):
                    self.write_File(dt_string)
                else:
                    self.write_File(dt_string)
        else:

            dt_string = Feed.now.strftime("%Y-%m-%d")
            # below logic is used to calculate the days between expiration and current date
            exp_date = datetime.datetime.strptime(self.exp_date, "%Y-%m-%d").date()
            date = datetime.datetime.strptime(dt_string, "%Y-%m-%d").date()
            Exp_date = exp_date - date
            exp_days=str(Exp_date.days)+' days left'
            if(self.format=='txt'):
                self.write_File(exp_days)
            else:
                self.write_File(exp_days)
                # defining read_File to read the data when the user typed inputs are completed
    def read_file(self):

        if (self.format == 'txt'):
            file1 = open(str(self.inputfile),'r')
            print(file1.read())
            file1.close()
        elif(self.format == 'json'):
            file1 = open(str(self.outputfile), 'r')
            print(file1.read())
            file1.close()

        elif(self.format == 'xml'):
            file1 = open(str(self.outputfile), 'r')
            print(file1.read())
            file1.close()


    def remove_File(self):
        if(self.format=='txt'):
            print('\n----Removing The '+self.format+' file---------------\n')
            print(self.inputfile+'.txt')
            os.remove(inputfile+'.txt')
        else:
            print('\n----Removing The '+path+self.inputfile + ' file---------------\n')
            print(self.inputfile)
            os.remove(path+self.inputfile)

class News(Feed):
    def __init__(self, inputfile):
        self.inputfile = inputfile
        self.content = input('Input News content:')
        self.city = input('Input city:')
        self.type = 'News'
        a=Feed(self.inputfile,self.content,self.city,self.type)
        a.Input_Text()
        a.Input_City()
        a.datetime()
        a.read_file()

class PrivateAd(Feed):
     def __init__(self,inputfile):
        self.inputfile = inputfile
        self.content = input('Input Advertisement content:')
        self.city = input('Input city:')
        self.exp_date = input('Input ad expiry date:')
        self.type='Ad'
        b=Feed(self.inputfile,self.content,self.city,self.type,self.exp_date)
        b.Input_Text()
        b.Input_City()
        b.datetime()
        b.read_file()

class Quote(Feed):
    def __init__(self,inputfile):
        self.content = input('Input quote content:')
        self.type = 'quote'
        self.inputfile = inputfile
        c=Feed(self.inputfile,self.content,self.type)
        c.Input_Text()
        c.read_file()

class Joke(Feed):
    def __init__(self, inputfile):
        self.content = input('Input joke content:')
        self.type='joke'
        self.inputfile = inputfile
        d=Feed(self.inputfile,self.content,self.type)
        d.Input_Text()
        d.read_file()

class json_feed(Feed):
    def __init__(self,inputfile,path):
        self.inputfile=inputfile
        self.path=path

    def read_json(self):
        # Opening JSON file
        f=open(self.path+self.inputfile)
        data = json.load(f)
        print('New output file from input json file ' + path + str(self.inputfile).split('.')[0]+'.txt')
        for i in range(len(data['News'])):
            self.type='News'
            self.content=data['News'][i]['content']
            self.city=data['News'][i]['city']
            c=Feed(self.inputfile,self.content,self.city,self.type)
            c.Input_Text()
            c.Input_City()
            c.datetime()
            c.read_file()
        #print(json_dict)
        for i in range(len(data['Ad'])):
            self.type='Ad'
            self.content=data['Ad'][i]['content']
            self.city=data['Ad'][i]['city']
            self.exp_date=data['Ad'][i]['exp_date']
            d=Feed(self.inputfile,self.content,self.city,self.type,self.exp_date)
            d.Input_Text()
            d.Input_City()
            d.datetime()
            d.read_file()
        #closing json file
        f.close()
        e=Feed(self.inputfile)
        e.remove_File()




class xml_feed(Feed):
    def __init__(self,inputfile,path):
        self.inputfile=inputfile
        self.path=path
        self.format='xml'
    def read_xml(self):
        # Opening XML file
        xml_file = ET.parse(self.path+self.inputfile)
        root = xml_file.getroot()
        for category in root.iter():
            if (category.get('type') == 'news'):
                self.type='News'
                for t in category:
                    if (t.tag == 'content'):
                        self.content=t.text

                    elif (t.tag == 'city'):
                        self.city=t.text
                # print(self.content,self.city)
                d = Feed(self.inputfile, self.content, self.city, self.type)
                d.Input_Text()
                d.Input_City()
                d.datetime()
                d.read_file()
            elif (category.get('type') == 'Ad'):
                self.type = 'Ad'
                for c in category:
                    if (c.tag == 'content'):
                        self.content=c.text
                    elif (c.tag == 'city'):
                        self.city=c.text
                    elif (c.tag == 'exp_date'):
                        self.exp_date = c.text
                e = Feed(self.inputfile, self.content, self.city, self.type, self.exp_date)
                e.Input_Text()
                e.Input_City()
                e.datetime()
                e.read_file()

        #
        print('\nNew output file from input Xml file ' + path + str(self.inputfile).split('.')[0]+'.txt')
        #

        e=Feed(self.inputfile)
        e.remove_File()



#
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

    if(inputfilename.split('.')[1]=='json'):
        print('Input file name:' + path + inputfilename)
        a=json_feed(inputfilename,path)
        a.read_json()

    elif(inputfilename.split('.')[1]=='xml'):
        print('Input file name:' + path + inputfilename)
        a = xml_feed(inputfilename, path)
        a.read_xml()

    else:
        print('Input file name:' + path+inputfilename)
        inputfile=path+inputfilename
        a=News(inputfile)
        b=PrivateAd(inputfile)
        c=Quote(inputfile)
        d=Joke(inputfile)
        a = input('\n\'Enter the Target File name to be copied:\'->')
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



