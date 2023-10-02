from createffurls import getURLs
import requests
import pandas as pd
from bs4 import BeautifulSoup
import time
import re
import json

def scrapeRouteData():
    '''
    Function to scrape the destination and operating airline data for each airport.

    Returns: routes -- A DataFrame with the Columns 'Source Airport','Destination','Operated By' for every active route.
    '''
    #Get list of all airport urls
    url_list = getURLs()
    counter = 0
    total_length = len(url_list)
    routes = pd.DataFrame(columns=['src_airport', 'dest_airport','operated_by','accurate_as_of'])
    no_direct_routes = []
    headers = {
        'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36'
    }
    for url in url_list:
        counter += 1
        # Create session to avoid 403 error
        session = requests.Session()
        session.headers.update(headers)
        # Get and parse page html using google cached version of site
        page = session.get('https://webcache.googleusercontent.com/search?q=cache:' + url)
        if page.status_code == 200 or page.status_code == 304:
            # Get source from the url
            source = url[28:]
            soup = BeautifulSoup(page.text, "html.parser")
            # Get datetime the site was cached
            cached_date = soup.find('div',attrs={'id':'bN015htcoyT__google-cache-hdr'}).find_next('span').find_next('span').text[47:71]
            # Get Destinations container
            dest_str = re.search('allDestinations: \[(.+?)\],', soup.find('script',attrs={'src':'/js/moment2294.min.js'}).find_next('script').string)
            if dest_str:
                found = '['+dest_str.group(1)+']'
                dest_list = json.loads(found)
                for dct in dest_list:
                    source = dct['iata_from']
                    dest = dct['iata_to']
                    airlines = []
                    for i in dct['airlineroutes']:
                        airlines.append(i['carrier_name'])
                    #Create a single line dataframe and append it to the routes dataframe
                    df = pd.DataFrame(data=[[source,dest,airlines,cached_date]], columns=['src_airport', 'dest_airport','operated_by','accurate_as_of'])
                    routes = routes.append(df,ignore_index=True)
            else:
                print('Error with {}\nNo allDestinations JSON in script tag.'.format(source))
        else:
            no_direct_routes.append(source)
        # Sleep for 1s every 5 urls, 5s every 100 urls, and 30s every 1000 to avoid connections aborted by the host.
        if counter%5 == 0:
            time.sleep(1)
            print('{}/{} urls scraped. {} urls remaining.'.format(counter, total_length, total_length-counter))
        if counter%100 == 0:
            time.sleep(4)
        if counter%1000 == 0:
            time.sleep(25)
    print('Errors with following codes:')
    print(no_direct_routes)
    return routes

if __name__ == '__main__':
    routes = scrapeRouteData()
    routes.to_csv('active_routes.csv')
    print('Your code is complete. Faze up.')