##############################METHOD_1###################################################################################

#importingdatetime function for calculating current date time and formatting date 
import datetime
#declaring class 
class Feed:
    #declaring class variable now to use it in the methods
    now = datetime.datetime.now()

    def __init__(self):
        #asking user to input the file name to know the file name which will be created in there local path
        data=input('Enter the text File name:')
        self.data=data
        print('Text file name:'+self.data+'.txt')
     
    #defining write_file method to write the data to the file
    def write_File(self,text):
        #using open file function to create a new file and using 'a' append mode to add the content to the file continously
        self.newfile = open(self.data+'.txt','a')
        self.newfile.write(str(text))
        self.newfile.close()

    #defining Input_text method to pass the news,advertisement and quote content 
    def Input_Text(self,data,content):
        #text=input("Input Text - Type the input text data")
        if(data=='News'):
            self.write_File('\n-----News-----------\n'+content+'\n')
        elif(data=='Ad'):
            self.write_File('\n----Private Advertisement-----------\n'+content+'\n')
        else:
            self.write_File('\n-----Quote of the day-----------\n'+content+'\n')

    #defining Input_City method to pass city            
    def Input_City(self,city):
        #text=input("Input city")
        self.write_File(city+',')
    
    #defining datetime method to process and publish current date and expiration days for the advertisement content    
    def datetime(self,data):
        now = datetime.datetime.now()
        if(data=='News'):
            #formating the date to string in the dd/mm/yyyy hh:mm format
            dt_string = now.strftime("%d/%m/%Y %H:%M")
            self.write_File(dt_string)
        else:
            dt_string = now.strftime("%Y-%m-%d")
            #below logic is used to calculate the days between expiration and current date
            exp_date=datetime.datetime.strptime(data, "%Y-%m-%d").date()
            date = datetime.datetime.strptime(dt_string,"%Y-%m-%d").date()
            Exp_date = exp_date-date
            self.write_File(str(Exp_date.days)+' days')

    #defining read_File to read the data when the user typed inputs are completed	        
    def read_file(self):
        file1=open(self.data+'.txt', 'r')
        print(file1.read())
        file1.close()
        
    def News(self,Newscontent,city):
        self.Input_Text('News',Newscontent)
        self.Input_City(city)
        self.datetime('News')
        self.read_file()
        
        
    def Ad(self,adcontent,city,exp_date):
               
        self.Input_Text('Ad',adcontent)
        self.Input_City(city)
        self.datetime(exp_date)
        self.read_file()
        
        
    def quote(self,quote):
        self.Input_Text('quote',quote)
        self.read_file()

#creating object for the class Feed
a=Feed()
#calling News method in class Feed
a.News('somethinghappened','London')
#calling Ad method in class Feed
a.Ad('advertisement','Delhi','2023-11-1')
#calling quote method in class Feed
a.quote('Everything will change')


##############################METHOD_2###################################################################################
# In Method 2 we  are prompting the user data when the program executes

#importingdatetime function for calculating current date time and formatting date 
import datetime
#declaring class 
class Feed:
    #declaring class variable now to use it in the methods
    now = datetime.datetime.now()

    def __init__(self):
        #asking user to input the file name to know the file name which will be created in there local path
        data=input('Enter the text File name:')
        self.data=data
        print('Text file name:'+self.data+'.txt')
    
    
     
    #defining write_file method to write the data to the file
    def write_File(self,text):
        #using open file function to create a new file and using 'a' append mode to add the content to the file continously
        self.newfile = open(self.data+'.txt','a')
        self.newfile.write(str(text))
        self.newfile.close()

    #defining Input_text method to pass the news,advertisement and quote content 
    def Input_Text(self,data):
        content=input("Type the input records for "+data+':\n')
        if(data=='News'):
            self.write_File('\n-----News-----------\n'+content+'\n')
        elif(data=='Ad'):
            self.write_File('\n----Private Advertisement-----------\n'+content+'\n')
        else:
            self.write_File('\n-----Quote of the day-----------\n'+content+'\n')

    #defining Input_City method to pass city            
    def Input_City(self):
        city=input("Input city")
        self.write_File(city+',')
    
    #defining datetime method to process and publish current date and expiration days for the advertisement content    
    def datetime(self,data):
        now = datetime.datetime.now()
        if(data=='News'):
            #formating the date to string in the dd/mm/yyyy hh:mm format
            dt_string = now.strftime("%d/%m/%Y %H:%M")
            self.write_File(dt_string)
        elif(data=='Ad'):
            expdata=input('Enter the expiration date for the adverstisement in YYYY-MM-DD format\n')
            dt_string = now.strftime("%Y-%m-%d")
            #below logic is used to calculate the days between expiration and current date
            exp_date=datetime.datetime.strptime(expdata, "%Y-%m-%d").date()
            date = datetime.datetime.strptime(dt_string,"%Y-%m-%d").date()
            Exp_date = exp_date-date
            self.write_File(str(Exp_date.days)+' days')

    #defining read_File to read the data when the user typed inputs are completed	        
    def read_file(self):
        file1=open(self.data+'.txt', 'r')
        print(file1.read())
        file1.close()
        
    def News(self):
        self.Input_Text('News')
        self.Input_City()
        self.datetime('News')
        self.read_file()
        
        
    def Ad(self):
               
        self.Input_Text('Ad')
        self.Input_City()
        self.datetime('Ad')
        self.read_file()
        
        
    def quote(self):
        self.Input_Text('quote')
        self.read_file()


#creating object for the class Feed
a=Feed()
#calling News method in class Feed
a.News()
#calling Ad method in class Feed
a.Ad()
#calling quote method in class Feed
a.quote()