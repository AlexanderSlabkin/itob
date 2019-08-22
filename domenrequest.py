import requests
from bs4 import BeautifulSoup

r = requests.get('https://vk.com')
soup = BeautifulSoup(r.text, 'html.parser')
#print(r.text)
#print(soup.prettify())

def parse(domen):
    url = 'https://'+domen
    r = requests.get(url)
    soup = BeautifulSoup(r.content, 'html.parser')
    title = ''
    if soup.title:
        title = soup.title.get_text()
    keywords = ''
    for keyword in soup.find_all('keywords'):
        keywords += keyword + ' '
    description = ''
    if soup.description:
        description = soup.description.get_text()

    return url, title, description, keywords[:-1]

