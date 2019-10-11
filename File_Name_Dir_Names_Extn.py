import os
import shutil
import pprint
filenames=[]
dirnames=[]
extn=[]
count={}

#input_frm_user=input("Please enter a directory path make sure to provide \\ : ")


os.chdir(r'C:\Users\charan.teja\Downloads')#Directory switch to Downloads

def dir_names():            #Function to list directory names
  for dir in os.listdir():
     if os.path.isdir(dir):
        dirnames.append(dir)

def file_names():           #Function to list filename in a given directory
  for filename in os.listdir():
     if os.path.isfile(filename):
        filenames.append(filename)
        name,file_extension = os.path.splitext(os.path.join(r'C:\Users\charan.teja\Downloads',filename))#To split filename and extension and store extension in an empty list
        extn.append(file_extension)
        

def count_type():           #Function to count number of files with each extension
   for item in extn:
     count.setdefault(item,0)
     count[item]=count[item]+1

def create_dir():           #Function to create directories based on file extensions
    for item in count:
        try:
            os.makedirs(item[1:])
        except FileExistsError:
            print('Directory alredy exsists : ' + item[1:])



#Below are function calls for above functions
     
dir_names()
file_names()
count_type()
create_dir()



print('List of Directories in Downloads'.center(100,'='))#provides output like =======Text========
pprint.pprint(dirnames)
print('List of Files in Downloads'.center(100,'='))
pprint.pprint(filenames)
print('List of File Extensions in Downloads'.center(100,'='))
pprint.pprint(extn)
print('Count of each File Extensions in Downloads'.center(100,'='))
pprint.pprint(count)



"""if filename.endswith('.xlsx'):
        print(filename)"""
      
