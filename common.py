# -*- coding: utf-8 -*-
"""
Created on Mon Dec 30 17:39:53 2019

@author: ogulcan.karakullukcu
"""
import os
import pandas as pd

#Create directory for each subHeaders
def create_project_dir(directory):
    if not os.path.exists(directory):
       os.makedirs(directory)
       print('Directory created: ' + directory)

#Write a new file with given data
def write_file(path, data):
    f = open(path, 'w')
    f.write(data + '\n')
    f.close()   
        
#Add data onto an existing file
def append_to_file(path, data):
    with open(path, 'a') as file:
        file.write(data + '\n')
        
#Turn each line of file into set
def file_to_set(file_name):
    results = set()
    with open(file_name, 'rt') as file:
        for line in file:
            results.add(line.replace('\n',''))
    return results

#Create link file
def create_links_file(file_name):
    if not os.path.isfile(file_name):
        write_file(file_name,'More Stats Menu')
        print('Links file created: ' + file_name)

#Create excel file onto a defined folder        
def create_excel_file(folder_name,file_name,data):
    file = folder_name + '/' + file_name + '.xlsx'
    if not os.path.isfile(file):
        df = pd.DataFrame(data)
        df.to_excel(file)
        print('Excel file created: ' + file)