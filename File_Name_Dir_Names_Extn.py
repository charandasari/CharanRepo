import os
import pprint
filenames=[]
dirnames=[]
extn=[]
count={}

os.chdir(r'C:\Users\charan.teja\Downloads')#Directory switch to Downloads

def dir_names():            #Function to list directory names
  for dir in os.listdir():
     if os.path.isdir(dir):
        dirnames.append(dir)

def file_names():           #Function to list filename in a given directory
  for filename in os.listdir():
     if os.path.isfile(filename):
        name,file_extension = os.path.splitext(os.path.join(r'C:\Users\charan.teja\Downloads',filename))#To split filename and extension and store extension in an empty list
        extn.append(file_extension)
        filenames.append(filename)

def count_type():           #Function to count number of files with each extension
   for item in extn:
     count.setdefault(item,0)
     count[item]=count[item]+1 
        
#Below are function calls for above functions
     
dir_names()
file_names()
count_type()

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
      
