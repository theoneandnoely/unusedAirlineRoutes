from string import ascii_lowercase as alphabet
import re
import requests
import time
from bs4 import BeautifulSoup


def getLetterURLs():
    '''
    Function to create list of URLs ending in every letter of the alphabet from a base url
    
    Returns url_list -- list of urls with a different letter appended to the same base url
    '''
    url_base = 'https://airports-list.com/iata-code'
    url_list = []
    for c in alphabet:
        url = url_base + '/' + c
        url_list.append(url)
    return url_list

def getIATAcodes():
    '''
    Function to create a list of IATA code appendices for creating URLs
    
    Returns: iata_list -- a list of strings in the form "/airport/<IATA code>"
    '''
    #import list of URLs
    url_list = getLetterURLs()
    #initiate list of codes
    iata_list = []
    #Parse the html for each of the urls
    for url in url_list:
        page = requests.get(url)
        soup = BeautifulSoup(page.text, "html.parser")
        #find only the links that use the "/airport/<IATA code>" format
        tags = soup.find_all('a', {"href" : re.compile('^/airport/.*')})
        #Check the link isn't already in the list and append it
        for t in tags:
            link = t.attrs['href']
            if link in iata_list:
                pass
            else:
                iata_list.append(link)
        #sleep for a second so website doesn't think I'm spamming
        time.sleep(1)
    return iata_list

def getIATAURLs():
    '''
    Function to create a list of URLs for each IATA code
    
    Returns: url_list -- A list of the url for each airport's page on the site
    '''
    iata_list = getIATAcodes()
    url_base = 'https://airports-list.com'
    url_list = []
    for code in iata_list:
        url = url_base + code
        url_list.append(url)
    return url_list