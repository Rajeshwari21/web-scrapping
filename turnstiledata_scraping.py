# Import libraries
import requests
import urllib.request
import time
from bs4 import BeautifulSoup

url = "http://web.mta.info/developers/turnstile.html"

response = requests.get(url)
# print(response)

soup = BeautifulSoup(response.text, "html.parser")
line_count = 1
for a_tag in soup.findAll('a'):
    if (38 <= line_count < 48):
        data_link = a_tag['href']
        download_url = 'http://web.mta.info/developers/' + data_link
        urllib.request.urlretrieve(
            download_url, './'+data_link[data_link.find('/turnstile_')+1:])
        time.sleep(1)
    line_count += 1
