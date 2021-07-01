#import necessary libraries
import requests
from bs4 import BeautifulSoup


#create user agent (optional)
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.106 Safari/537.36'}


#Send get() request and fetch webpage contents
response = requests.get('https://shubhamsayon.github.io/python/demo_html.html', headers=headers)
webpage = response.content


#check status code (optional)
#print(response.status_code)


#create beautiful soup object
soup = BeautifulSoup(webpage, "html.parser")


# navigate and extract content we want
for tr in soup.find_all('tr'):
    topic = "TOPIC: "
    url = "URL: "
    values = [data for data in tr.find_all('td')]
    for value in values:
        print(topic, value.text)
        topic = url
    print()