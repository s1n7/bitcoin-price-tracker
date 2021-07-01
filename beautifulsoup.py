import requests as re
from bs4 import BeautifulSoup

#create user-agent
useragent = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.106 Safari/537.36'}


#get() request
response = re.get('https://shubhamsayon.github.io/python/demo_html.html', headers=useragent)


#Store new webpage contents
webpage = response.content


#Check status code
#print(response.status_code)


#Create BeautifulSoup object out of the webpage content
soup = BeautifulSoup(webpage, 'html.parser')


#Print webpage HTML in a pretty way
#print(soup.prettify())


#access tags using tag names, only prints out first appearance of tag
head_tag = soup.head

chrildren_of_headtag = soup.head.contents
first_child_headtag = soup.head.contents[1]
name_child_headtag = soup.head.contents[1].name


#using .children
"""
for child in soup.body.children:
    if child!="\n":
        print(child.name)
"""


# descendants
children = [child for child in soup.body.children if child != "\n"]
descendent = [x for x in soup.head.descendants if x != "\n"]
print(children)


#parent
parent_element = soup.title.parent.name


#parents
"""
for parent in soup.p.parents:   #iterate over all parents from p tag
    print(parent.name)
"""


#next sibling/previous siblings
#prev_sibling = soup.b.previous_sibling

"""for sibling in soup.head.next_siblings:
    print(sibling)
"""


#Navigable strings
title_string = soup.title.string
#print(title_string) #doesn't work for tag with children

    #lots of white spaces
"""     
for string in soup.body.strings:
    print(string)
"""


"""
for string in soup.body.stripped_strings:
    print(string)
"""


# find() and find_all()
all_ptags = soup.find_all('p')       #find all p-tags in document, prints out list

second_ptag = soup.find_all('p')[1].text    #access second p-tag as text
first_two_ptags = soup.find_all('p', limit=2)


div_byclass = soup.find_all('div', class_ = 'myDiv')     #get div tag but only with the class name
div_byclass_alternative = soup.find_all('div', {'class':'myDiv', 'class':'myDiv2'})     #with dictionary for div tags with multiple classes

tag_byid = soup.find_all('table', id ='blogs')

multiple_tags = soup.find_all(['div', 'img'])


first_appearance_ptag = soup.find('p')  #similar to soup.p, difference: find can find specific p tag

specific_ptag = soup.find('p', class_= 'myDiv2')    
#print(specific_ptag)
