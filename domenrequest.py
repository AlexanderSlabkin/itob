#!/usr/bin/env python3
import requests
from bs4 import BeautifulSoup


def parse(domen):

    url = 'https://'+domen
    r = requests.get(url)
    soup = BeautifulSoup(r.content, 'html.parser')
    title = ''
    if soup.title:
        title = soup.title.get_text()
    title = soup.find('title').get_text()
    keywords = ''
    for keyword in soup.find_all('keywords'):
        keywords += keyword.string + ' '
    description = soup.find(attrs={'name': 'description'})
    if description: description = description.get('content')
    return url, title, description, keywords[:-1]


if __name__ == '__main__':
    domen = 'ok.ru'
    p = parse(domen)
    r = requests.get('https://' + domen)
    soup = BeautifulSoup(r.text, 'html.parser')
    #print(soup.prettify())
    print(p)

