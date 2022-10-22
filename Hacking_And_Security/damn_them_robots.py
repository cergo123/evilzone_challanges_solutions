import requests
from bs4 import BeautifulSoup


def scrape():
    r = requests.get('https://evilzone.org/challenges/damn_them_robots/robots.txt')
    res = r.text.splitlines()
    secret_page = res[1].split(':')[1].strip()
    r2 = requests.get(f'https://evilzone.org{secret_page}')
    # remove html tags
    soup = BeautifulSoup(r2.text, 'html.parser')
    res2 = soup.text
    res2 = res2.splitlines()
    result = res2[1].split(':')[1].strip()
    return result

print(scrape())
