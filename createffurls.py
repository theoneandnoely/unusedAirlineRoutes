import pandas as pd

def getURLs():
    '''
    Function to create a list of urls for the flightsfrom.com site for each airport.

    Returns: url_list -- list of urls in the form of 'flightsfrom.com/<iata code>/destinations'
    '''
    df = pd.read_csv('airport_data.csv')
    iata_list = list(df['Unnamed: 0'])
    url_start = 'https://www.flightsfrom.com/'
    url_end = '/destinations'
    url_list = []
    for iata in iata_list:
        url = url_start + iata + url_end
        url_list.append(url)
    return url_list


## -- Seperated into smaller sections to be increase speed --

def getAlist():
    df = pd.read_csv('airport_data.csv')
    iata_list = list(df['Unnamed: 0'])
    url_start = 'https://www.flightsfrom.com/'
    url_end = '/destinations'
    url_list = []
    for iata in iata_list:
        if iata[0] == 'A':
            url = url_start + iata + url_end
            url_list.append(url)
    return url_list

def getBlist():
    df = pd.read_csv('airport_data.csv')
    iata_list = list(df['Unnamed: 0'])
    url_start = 'https://www.flightsfrom.com/'
    url_end = '/destinations'
    url_list = []
    for iata in iata_list:
        if iata[0] == 'B':
            url = url_start + iata + url_end
            url_list.append(url)
    return url_list

def getClist():
    df = pd.read_csv('airport_data.csv')
    iata_list = list(df['Unnamed: 0'])
    url_start = 'https://www.flightsfrom.com/'
    url_end = '/destinations'
    url_list = []
    for iata in iata_list:
        if iata[0] == 'C':
            url = url_start + iata + url_end
            url_list.append(url)
    return url_list

def getDlist():
    df = pd.read_csv('airport_data.csv')
    iata_list = list(df['Unnamed: 0'])
    url_start = 'https://www.flightsfrom.com/'
    url_end = '/destinations'
    url_list = []
    for iata in iata_list:
        if iata[0] == 'D':
            url = url_start + iata + url_end
            url_list.append(url)
    return url_list

def getElist():
    df = pd.read_csv('airport_data.csv')
    iata_list = list(df['Unnamed: 0'])
    url_start = 'https://www.flightsfrom.com/'
    url_end = '/destinations'
    url_list = []
    for iata in iata_list:
        if iata[0] == 'E':
            url = url_start + iata + url_end
            url_list.append(url)
    return url_list

def getFlist():
    df = pd.read_csv('airport_data.csv')
    iata_list = list(df['Unnamed: 0'])
    url_start = 'https://www.flightsfrom.com/'
    url_end = '/destinations'
    url_list = []
    for iata in iata_list:
        if iata[0] == 'F':
            url = url_start + iata + url_end
            url_list.append(url)
    return url_list

def getGlist():
    df = pd.read_csv('airport_data.csv')
    iata_list = list(df['Unnamed: 0'])
    url_start = 'https://www.flightsfrom.com/'
    url_end = '/destinations'
    url_list = []
    for iata in iata_list:
        if iata[0] == 'G':
            url = url_start + iata + url_end
            url_list.append(url)
    return url_list

def getHlist():
    df = pd.read_csv('airport_data.csv')
    iata_list = list(df['Unnamed: 0'])
    url_start = 'https://www.flightsfrom.com/'
    url_end = '/destinations'
    url_list = []
    for iata in iata_list:
        if iata[0] == 'H':
            url = url_start + iata + url_end
            url_list.append(url)
    return url_list

def getIlist():
    df = pd.read_csv('airport_data.csv')
    iata_list = list(df['Unnamed: 0'])
    url_start = 'https://www.flightsfrom.com/'
    url_end = '/destinations'
    url_list = []
    for iata in iata_list:
        if iata[0] == 'I':
            url = url_start + iata + url_end
            url_list.append(url)
    return url_list

def getJlist():
    df = pd.read_csv('airport_data.csv')
    iata_list = list(df['Unnamed: 0'])
    url_start = 'https://www.flightsfrom.com/'
    url_end = '/destinations'
    url_list = []
    for iata in iata_list:
        if iata[0] == 'J':
            url = url_start + iata + url_end
            url_list.append(url)
    return url_list

def getKlist():
    df = pd.read_csv('airport_data.csv')
    iata_list = list(df['Unnamed: 0'])
    url_start = 'https://www.flightsfrom.com/'
    url_end = '/destinations'
    url_list = []
    for iata in iata_list:
        if iata[0] == 'K':
            url = url_start + iata + url_end
            url_list.append(url)
    return url_list

def getLlist():
    df = pd.read_csv('airport_data.csv')
    iata_list = list(df['Unnamed: 0'])
    url_start = 'https://www.flightsfrom.com/'
    url_end = '/destinations'
    url_list = []
    for iata in iata_list:
        if iata[0] == 'L':
            url = url_start + iata + url_end
            url_list.append(url)
    return url_list

def getMlist():
    df = pd.read_csv('airport_data.csv')
    iata_list = list(df['Unnamed: 0'])
    url_start = 'https://www.flightsfrom.com/'
    url_end = '/destinations'
    url_list = []
    for iata in iata_list:
        if iata[0] == 'M':
            url = url_start + iata + url_end
            url_list.append(url)
    return url_list

def getNlist():
    df = pd.read_csv('airport_data.csv')
    iata_list = list(df['Unnamed: 0'])
    url_start = 'https://www.flightsfrom.com/'
    url_end = '/destinations'
    url_list = []
    for iata in iata_list:
        if iata[0] == 'N':
            url = url_start + iata + url_end
            url_list.append(url)
    return url_list

def getOlist():
    df = pd.read_csv('airport_data.csv')
    iata_list = list(df['Unnamed: 0'])
    url_start = 'https://www.flightsfrom.com/'
    url_end = '/destinations'
    url_list = []
    for iata in iata_list:
        if iata[0] == 'O':
            url = url_start + iata + url_end
            url_list.append(url)
    return url_list

def getPlist():
    df = pd.read_csv('airport_data.csv')
    iata_list = list(df['Unnamed: 0'])
    url_start = 'https://www.flightsfrom.com/'
    url_end = '/destinations'
    url_list = []
    for iata in iata_list:
        if iata[0] == 'P':
            url = url_start + iata + url_end
            url_list.append(url)
    return url_list

def getQlist():
    df = pd.read_csv('airport_data.csv')
    iata_list = list(df['Unnamed: 0'])
    url_start = 'https://www.flightsfrom.com/'
    url_end = '/destinations'
    url_list = []
    for iata in iata_list:
        if iata[0] == 'Q':
            url = url_start + iata + url_end
            url_list.append(url)
    return url_list

def getRlist():
    df = pd.read_csv('airport_data.csv')
    iata_list = list(df['Unnamed: 0'])
    url_start = 'https://www.flightsfrom.com/'
    url_end = '/destinations'
    url_list = []
    for iata in iata_list:
        if iata[0] == 'R':
            url = url_start + iata + url_end
            url_list.append(url)
    return url_list

def getSlist():
    df = pd.read_csv('airport_data.csv')
    iata_list = list(df['Unnamed: 0'])
    url_start = 'https://www.flightsfrom.com/'
    url_end = '/destinations'
    url_list = []
    for iata in iata_list:
        if iata[0] == 'S':
            url = url_start + iata + url_end
            url_list.append(url)
    return url_list

def getTlist():
    df = pd.read_csv('airport_data.csv')
    iata_list = list(df['Unnamed: 0'])
    url_start = 'https://www.flightsfrom.com/'
    url_end = '/destinations'
    url_list = []
    for iata in iata_list:
        if iata[0] == 'T':
            url = url_start + iata + url_end
            url_list.append(url)
    return url_list

def getUlist():
    df = pd.read_csv('airport_data.csv')
    iata_list = list(df['Unnamed: 0'])
    url_start = 'https://www.flightsfrom.com/'
    url_end = '/destinations'
    url_list = []
    for iata in iata_list:
        if iata[0] == 'U':
            url = url_start + iata + url_end
            url_list.append(url)
    return url_list

def getVlist():
    df = pd.read_csv('airport_data.csv')
    iata_list = list(df['Unnamed: 0'])
    url_start = 'https://www.flightsfrom.com/'
    url_end = '/destinations'
    url_list = []
    for iata in iata_list:
        if iata[0] == 'V':
            url = url_start + iata + url_end
            url_list.append(url)
    return url_list

def getWlist():
    df = pd.read_csv('airport_data.csv')
    iata_list = list(df['Unnamed: 0'])
    url_start = 'https://www.flightsfrom.com/'
    url_end = '/destinations'
    url_list = []
    for iata in iata_list:
        if iata[0] == 'W':
            url = url_start + iata + url_end
            url_list.append(url)
    return url_list

def getXlist():
    df = pd.read_csv('airport_data.csv')
    iata_list = list(df['Unnamed: 0'])
    url_start = 'https://www.flightsfrom.com/'
    url_end = '/destinations'
    url_list = []
    for iata in iata_list:
        if iata[0] == 'X':
            url = url_start + iata + url_end
            url_list.append(url)
    return url_list

def getYlist():
    df = pd.read_csv('airport_data.csv')
    iata_list = list(df['Unnamed: 0'])
    url_start = 'https://www.flightsfrom.com/'
    url_end = '/destinations'
    url_list = []
    for iata in iata_list:
        if iata[0] == 'Y':
            url = url_start + iata + url_end
            url_list.append(url)
    return url_list

def getZlist():
    df = pd.read_csv('airport_data.csv')
    iata_list = list(df['Unnamed: 0'])
    url_start = 'https://www.flightsfrom.com/'
    url_end = '/destinations'
    url_list = []
    for iata in iata_list:
        if iata[0] == 'Z':
            url = url_start + iata + url_end
            url_list.append(url)
    return url_list