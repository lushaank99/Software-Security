import os
from xml.dom.minidom import parseString
import csv

def extract_permission(file):
 data = '' # string data from file
 with open(file, 'r') as f:
    data = f.read()
 dom = parseString(data) # parse file contents to xml dom
 nodes = dom.getElementsByTagName('uses-permission') # xml nodes named "uses-permission"
 permissions = [] 
 for node in nodes:
    permissions += [node.getAttribute("android:name")] 
 return (sorted(permissions)) 

def write_to_csv(permission,appname):
    with open(filename, 'a', newline="") as file:
          csvwriter = csv.writer(file)
          csvwriter.writerow([appname] + permission)
          file.close()

path = '/Users/teja/Desktop/selectedAPKs-decoded'
filename = '/Users/teja/Desktop/test/Permission_Data.csv'
with os.scandir(path) as entries:
    for entry in entries:
     if(os.path.isdir(entry)):
      for f_name in os.scandir(entry):
       if f_name.name.endswith('.xml'):
         permission=(extract_permission(f_name))
         write_to_csv(permission,entry.name)