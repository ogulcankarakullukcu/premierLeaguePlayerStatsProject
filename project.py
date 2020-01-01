# -*- coding: utf-8 -*-
"""
Created on Tue Dec 31 12:28:41 2019

@author: ogulcan.karakullukcu
"""
from common import *
from dataHandler import dataHandler
from linkHandler import linkHandler

base_url = 'https://www.premierleague.com/stats/top/players/goals?se=274'
domain_name = 'premierleague.com'
folder_name = ''

link = linkHandler(base_url)

links_list = file_to_set(link.link_file)

for line in links_list:
    
    if line.find(domain_name) > 0: 
       spl = line.split(':',1)
       folder_name = spl[0].strip()
       page_url = 'https://www.' + spl[1].strip()
       html_string = linkHandler.get_html_string(page_url)       
       dh = dataHandler(html_string)      
       file_name = dh.file_name       
       data = dh.data       
       create_excel_file(folder_name,file_name,data)