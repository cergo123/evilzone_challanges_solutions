import requests
from bs4 import BeautifulSoup


def scrap(md5):
    r = requests.get(f'https://md5.gromweb.com/?md5={md5}')
    soup = BeautifulSoup(r.text, 'html.parser')
    # get the value of the input with the id form_string_to_hash_string
    return soup.find('input', {'id': 'form_string_to_hash_string'}).get('value')

print(scrap('32aac14decb8389ed210b7e8acb28fe7'))