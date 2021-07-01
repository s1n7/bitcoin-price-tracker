#libraries
import requests
from bs4 import BeautifulSoup
import time


#create user agent (optional)
useragent = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.106 Safari/537.36'}


#Send get() request and fetch webpage contents
response = requests.get('https://www.alibris.com/search/books/subject/Computers', headers=useragent)
webpage = response.content


#check status code (optional)
#print(response.status_code)


#create beautiful soup object
soup = BeautifulSoup(webpage, "html.parser")


def findbooks():
    for parent in soup.find_all('ul', class_='primaryList'):    # parent element
        for n,tag in enumerate(parent.find_all('li')):
            title = [t for t in tag.find_all('p', class_='bookTitle')]
            author = [a for a in tag.find_all('p', class_='author')]
            price = [x for x in tag.find_all('a', class_='buy')]
            for item in title:
                print("Book title: ", item.text.strip())
            for a in author:
                print("Author: ", a.contents[1].text.strip())
            for p in price:
                print("Price: ", p.contents[1].text.strip())
            print()


if __name__ == '__main__':
    while True:
        findbooks()
        time_wait = 10
        print(f'Waiting {time_wait} minutes...')
        time.sleep(time_wait * 60)    #argument in seconds