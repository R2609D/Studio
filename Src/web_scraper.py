#***********************************************************************************************************
# Summary: Read all the scripts and stores into one file
#          
# Requirements: Python Verison 3.7
#
# Author : Anto 
#***********************************************************************************************************

from bs4 import BeautifulSoup
import requests

api_request = requests.get('https://imsdb.com/scripts/Blade.html').text
soup = BeautifulSoup(api_request, 'lxml')
script = soup.find('pre')
output = script.text
with open('scripts.txt', 'w') as f:
    f.write(output)