#!/usr/bin/env python3
import requests
from bs4 import BeautifulSoup


def parse(domen):

    url = 'https://'+domen
    r = requests.get(url)
    soup = BeautifulSoup(r.content, 'html.parser')
    for_table = {}
    for_table['url'] = url
    for_table['title'] = soup.find('title').get_text()
    for_table['keywords'] = ''
    for keyword in soup.find_all('keywords'):
        for_table['keywords'] += keyword.string + ' '
    if len(for_table['keywords']) > 1: for_table['keywords'].pop() 
    description = soup.find(attrs={'name': 'description'})
    for_table['description'] = ''
    if description: for_table['description'] = description.get('content')

    for i in for_table:
        if len(i) > 249:
            print('Warning: too long value')

    return for_table


if __name__ == '__main__':
    domen = 'ok.ru'
    p = parse(domen)
    r = requests.get('https://' + domen)
    soup = BeautifulSoup(r.text, 'html.parser')
    #print(soup.prettify())
    print(p)

