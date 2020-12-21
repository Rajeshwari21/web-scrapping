import requests
import urllib.request
import time
from bs4 import BeautifulSoup
import csv
import pandas as pd


def append_images(soup, image_urls, image_titles):
    for img_tag in soup.findAll('img'):
        img_src = img_tag.get('src')
        img_url = 'https://books.toscrape.com/' + img_src
        img_title = img_tag.get('alt')
        print(img_url + ':' + img_title)
        image_urls.append(img_url)
        image_titles.append(img_title)


website = "https://books.toscrape.com/index.html"
count = 1
web_split = website.split('/')
first, second, third, *other = web_split
image_urls = image_titles = []
next_link = ''

while (count <= 50):
    if count > 1:
        if "catalogue" in next_link:
            website = first+'//'+third+'/'+next_link
        else:
            website = first+'//'+third+'/catalogue/'+next_link
    response = requests.get(website)
    soup = BeautifulSoup(response.text, "html.parser")
    if soup.findAll('li', class_='next'):
        for link in soup.findAll('li', class_='next'):
            next_link = link.find('a').get('href')
            append_images(soup, image_urls, image_titles)
    else:
        append_images(soup, image_urls, image_titles)
    count += 1

images = pd.DataFrame({
    'URL': image_urls,
    'TITLE': image_titles
})

images.to_csv('images.csv')
