from createFFURLs import getURLs
import requests
import re
import pandas as pd
from bs4 import BeautifulSoup

def scrapeRouteData():
    '''
    Function to scrape the destination and operating airline data for each airport.

    Returns: routes -- A DataFrame with the Columns 'Source Airport','Destination','Operated By' for every active route.
    '''
    #Get list of all airport urls
    url_list = getURLs()
    routes = pd.DataFrame(columns=['src_airport', 'dest_airport','operated_by'])
    for url in url_list:
        #Get the source airport for the url in question
        source = url[28:31]
        #Get and parse page html
        page = requests.get(url)
        soup = BeautifulSoup(page.text, "html.parser")
        #Get Destinations container
        container = soup.find('ul',{'id':'airport-destination-items'})
        if container is None:
            print('Error with: ' + source)
            print('-- No ul tag')
        else:
            line_items = container.find_all('li')
            #Iterate through destinations
            for li in line_items:
                dest = li.attrs['data-iata'] #destination IATA code
                airlines = []
                #Iterate through all Airlines Operating the route
                logo_wrapper = li.find_all('div', class_ = re.compile('^airport-content-destination-logowrapper.*'))
                for l in logo_wrapper:
                    i = l.find('img')
                    airline = i.attrs['title']
                    airlines.append(airline)
                #Create a single line dataframe and append it to the routes dataframe
                df = pd.DataFrame(data=[[source,dest,airlines]], columns=['src_airport', 'dest_airport','operated_by'])
                routes = routes.append(df,ignore_index=True)
    return routes

if __name__ == '__main__':
    routes = scrapeRouteData()
    routes.to_csv('active_routes.csv')
    print('Your code is complete. Faze up.')