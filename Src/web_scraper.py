#***********************************************************************************************************
# Summary: Read all the scripts and stores into one file
#          
# Requirements: Python Verison 3.7
#
# Author : Anto 
#***********************************************************************************************************

from bs4 import BeautifulSoup
from movielist import movie_name
import requests

for i in range(len(movie_name)):
    api_request = requests.get('https://imsdb.com/scripts/{}.html'.format(movie_name[i])).text
    soup = BeautifulSoup(api_request, 'lxml')
    script = soup.find('pre')
    output = script.text


    with open('scripts.txt', 'a') as f:
        f.write(output)

#TODO: Convert this into a functions with try & expect error catching
#TODO: Add a way selecting different genres for the script.txt dataset
#TODO: Fix the path to where script.txt file is created 