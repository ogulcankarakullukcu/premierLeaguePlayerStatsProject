# -*- coding: utf-8 -*-
"""
Created on Tue Dec 31 20:15:47 2019

@author: ogulcan.karakullukcu
"""
from urllib.request import urlopen
import bs4 as bs
from common import *

class linkHandler:
    html_string = ''
    soup = ''
    folder_names = []
    domain_name = 'premierleague.com'
    link_file = 'links.txt'
    
    #Constructor
    def __init__(self, url):
        response = urlopen(url)
        html_bytes = response.read()
        linkHandler.html_string = html_bytes.decode('utf-8')
        linkHandler.soup = bs.BeautifulSoup(linkHandler.html_string, 'html.parser')
        create_links_file(linkHandler.link_file)
        linkHandler.create_folders()
        
    #Create folders with subheaders    
    @staticmethod    
    def create_folders():
        linkHandler.get_folder_names()
        for folder in linkHandler.folder_names:
            create_project_dir(folder)    
    
    #Get subheaders as folder names
    @staticmethod    
    def get_folder_names():
        folders = linkHandler.soup.find_all('nav', class_='moreStatsMenu')
        for f in folders:
            subHeader = linkHandler.get_links(f)
            linkHandler.folder_names.append(subHeader)        
    
    #Create links text file,append links with subheaders and returns subheader
    @staticmethod        
    def get_links(folder):
        subHeader = folder.find('h3').text.replace('\n','').strip()
        links = folder.find_all('a')
        for link in links:
            line = subHeader + ': ' + linkHandler.domain_name + link.get('href')
            append_to_file(linkHandler.link_file, line)
        return subHeader
    #Get html string from given url    
    @staticmethod            
    def get_html_string(url):
        response = urlopen(url)
        html_bytes = response.read()
        html_string = html_bytes.decode('utf-8')
        return html_string