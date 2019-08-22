import requests
from bs4 import BeautifulSoup

r = requests.get('https://vk.com')
soup = BeautifulSoup(r.text, 'html.parser')
#print(r.text)
#print(soup.prettify())

def parse(domen):
    url = 'https://'+domen
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')
    title = soup.title.string
    keywords = ''
    for keyword in soup.find_all('keywords'):
        keywords += keyword + ' '
    description = soup.description.string

    return url, title, description, keywords[:-1]

