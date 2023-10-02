import re
import requests
import time
from bs4 import BeautifulSoup
from AirportDataScraper.getListOfURLs import getIATAURLs
import pandas as pd


def scrapeAirportData():
    '''
    Function to scrape each airport page for:
            - IATA code
            - Country the Airport is in
            - City the Airport is in
            - Name of the Airport
            - Latitude
            - Longitude
            
    Returns: data -- A diction that contains the scraped data for each airport, grouped by IATA code.
    '''
    #Get List of URLs
    url_list = getIATAURLs()
    url_count = len(url_list)
    counter = 0
    data = {}
    headers = {'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36'}
    est_time = 2247
    for url in url_list:
        page = requests.get(url, headers)
        soup = BeautifulSoup(page.text, "html.parser")
        #Get IATA Code
        code_div = soup.find('div', class_='views-field views-field-title-2')
        code = code_div.find('p').text[11:]
        #Get Country Name
        country_div = soup.find('div', class_='views-field views-field-field-strana-eng')
        country = country_div.find('p').text[9:].replace("&#039;","'")
        #Get City Name
        city_div = soup.find('div', class_='views-field views-field-field-gorod-eng')
        city = city_div.find('p').text[6:]
        #Get Airport Name
        airport_div = soup.find('div', class_='views-field views-field-field-name-eng-1')
        airport = airport_div.find('p').text[14:]
        #Get Latitude and Longitude
        coor_div = soup.find('div',class_='views-field views-field-field-geo')
        coor_p = coor_div.find_all('p')
        for p in coor_p:
            lat_check = re.search('^Latitude:.*',p.text)
            lon_check = re.search('^Longitude:.*',p.text)
            if lat_check:
                lat_str = p.text[10:]
                lat_float = float(lat_str)
            elif lon_check:
                lon_str = p.text[11:]
                lon_float = float(lon_str)
        #Update the data dictionary with the scraped data
        data[code] = {'Airport Name':airport, 'Country':country, 'City':city, 'Latitude':lat_float, 'Longitude':lon_float}
        #Add one to counter and sleep for a second every 5 urls
        counter += 1
        rest_check = counter%5
        long_rest_check = counter%100
        if rest_check == 0:
            print('{}/{} urls scraped. Estimated time remaining: {}s'.format(counter, url_count, est_time))
            est_time -= 1
            time.sleep(1)
        if long_rest_check == 0:
            est_time -= 4
            time.sleep(4)
    return data

def saveAirportDataAsCSV(data):
    '''
    Function to convert the dictionary of scraped data into a pandas DataFrame and save it as a csv
    
    Parameters: data -- Dictionary containing the scraped data grouped by IATA code
    '''
    df = pd.DataFrame.from_dict(data, orient='index')
    df.to_csv('airport_data.csv')
    
if __name__ == '__main__':
    data = scrapeAirportData()
    saveAirportDataAsCSV(data)
    print('Code was executed successfully. Poggers.')