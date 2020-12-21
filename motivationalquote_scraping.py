import requests
from bs4 import BeautifulSoup

url = 'https://www.briantracy.com/blog/personal-success/26-motivational-quotes-for-success/'
headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86 64; rv:77.0) Gecko/20100101 Firefox/77.0'
}

web_content = requests.get(url, headers=headers)
soup = BeautifulSoup(web_content.text, 'html.parser')
# main_div = soup.find('div', class_='fl-post-content clearfix')
main_div = soup.find('div', class_='mainbar')
quotes_tags = main_div.findAll('h3')
quotes = []
for quote_tag in quotes_tags:
    quote = quote_tag.text
    if quote != '':
        quote = quote.split(')', 1)
        if len(quote) > 1:
            quotes.append((f'{quote[1]}').strip())
            print((f'{quote[1]}').strip())
