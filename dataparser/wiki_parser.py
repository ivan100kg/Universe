import requests
from bs4 import BeautifulSoup


def main():
    """Getting constellations' names and links"""
    url = 'https://en.wikipedia.org/wiki/IAU_designated_constellations'
    headers = {
        'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36'}
    resp = requests.get(url, headers=headers)
    soup = BeautifulSoup(resp.text, 'html.parser')
    table = soup.find('table', {'class': 'wikitable'})
    rows = table.find_all('tr')
    constellations = []
    for row in rows:
        tag_a = row.find('a')
        if tag_a and 'wiki' in tag_a['href']:
            constellations.append((tag_a.text, 'https://en.wikipedia.org/'+tag_a['href']))
    return constellations


if __name__ == '__main__':
    print(main())
