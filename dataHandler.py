# -*- coding: utf-8 -*-
"""
Created on Tue Dec 31 18:33:52 2019

@author: ogulcan.karakullukcu
"""
import bs4 as  bs
from common import *

class dataHandler:     
    html_string = ''
    soup = ''
    column_names = []
    data = []
    #Constructor
    def __init__(self, html_string):
        dataHandler.column_names.clear()
        dataHandler.data.clear()         
        dataHandler.html_string = html_string
        dataHandler.soup = bs.BeautifulSoup(dataHandler.html_string, 'html.parser')
        dataHandler.file_name = dataHandler.get_file_name()
        dataHandler.create_data_table()
    
    #Get stat type as file name
    @staticmethod    
    def get_file_name():
        data_metric = dataHandler.soup.find('div', class_ = 'currentStatContainer')
        file_name = str(data_metric.text.replace('\n','').strip())
        return file_name
    
    #Create data table with column names and rows
    @staticmethod
    def create_data_table():
        stat_table = dataHandler.soup.find('div', class_ = 'table')
        dataHandler.get_column_names(stat_table)
        dataHandler.data.append(dataHandler.column_names)
        dataHandler.insert_player_stats(stat_table)
    
    #Get column names from the header of stat table    
    def get_column_names(stat_table):
        header = stat_table.find_all('th')
        for h in header:
            dataHandler.column_names.append(h.text.replace('\n','').strip())
    
    #Create rows which include player data       
    def insert_player_stats(stat_table):
        body = stat_table.find_all('tr')
        for b in body:
            row = []
            rows = b.find_all('td')
            for r in rows:
                row.append(r.text.replace('\n','').strip())
                if len(row) == len(dataHandler.column_names):
                    dataHandler.data.append(row)
                    row = []