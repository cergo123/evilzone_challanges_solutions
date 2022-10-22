import requests


def scrape():
    r = requests.get('https://evilzone.org/challenges/you_validated_it_where/')
    # get text between 'The solution flag is:' and ';
    res = r.text.split('The solution flag is:')[1].split("';")[0].strip()
    return res.strip()


print(scrape())
