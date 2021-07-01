#import necessary libraries
import enum
import requests
from bs4 import BeautifulSoup


#create user agent (optional)
useragent = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.106 Safari/537.36'}


#Send get() request and fetch webpage contents
response = requests.get('https://pythonjobs.github.io/', headers=useragent)
webpage = response.content


#check status code (optional)
#print(response.status_code)


#create beautiful soup object
soup = BeautifulSoup(webpage, "html.parser")



# navigate and extract content we want
for job in soup.find_all('section', class_='job_list'):
    title = [a for a in job.find_all('h1')]
    for n,tag in enumerate(job.find_all('div', class_='job')):
        company = [x for x in tag.find_all('span', class_='info')]
        print("Jobtitle: ", title[n].text.strip())
        print("Location: ", company[0].text.strip())
        print("Company: ", company[3].text.strip())
        print()