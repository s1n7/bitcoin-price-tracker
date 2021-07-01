import requests

#own user agent, prevents 503 error code, shows we are not a bot
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.106 Safari/537.36'}
response = requests.get('https://www.google.com/', headers=headers)

#whole web page content
webpage = response.content
#print(webpage)  



#headers
page_headers = response.headers

for key,value in page_headers.items():
    print(key, ':', value)




#get user-agent info
print(response.request.headers)




#status code
print(response.status_code)