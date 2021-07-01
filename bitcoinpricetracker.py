
# @author: Luis 


import requests
from bs4 import BeautifulSoup
import pandas as pd
import time


def getPriceData():
    #Send get() request and fetch webpage contents
    response = requests.get('https://coinmarketcap.com/de/currencies/bitcoin/')
    webpage = response.content

    #check status code (optional)
    #print(response.status_code)

    #create beautiful soup object
    soup = BeautifulSoup(webpage, "html.parser")

    #extract current price, lowest day price and highest day price
    price = soup.find('div', class_='priceValue___11gHJ').text.strip()
    lowestDayValue = soup.find('div', class_='sc-16r8icm-0 gMZGhD nowrap___2C79N').contents[1].text.strip()
    highestDayValue = soup.find('div', class_='sc-16r8icm-0 HwsGY nowrap___2C79N').contents[1].text.strip()

    #append data to data list
    data = []
    data.append(price)
    data.append(highestDayValue)
    data.append(lowestDayValue)
    return data


while(True):
    #get price data from function
    pricedata = getPriceData()

    #create dataframe
    df = pd.DataFrame({"Bitcoin Price" : pricedata})

    #names of columns
    df.index = ['Price', 'Highest day value', 'Lowest day value']

    #exporting data into excel
    df.to_csv('Bitcoinprice.csv')

    #print out dataframe
    print(df)

    #wait 1 hour, then repeat process
    time.sleep(60 * 60)