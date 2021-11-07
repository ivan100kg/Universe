import requests
from bs4 import BeautifulSoup
import re


def main():
    """Getting constellations' names and links"""
    url = 'https://ru.wikipedia.org/wiki/%D0%A1%D0%BE%D0%B7%D0%B2%D0%B5%D0%B7%D0%B4%D0%B8%D0%B5'
    headers = {
        'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36'}
    resp = requests.get(url, headers=headers)
    soup = BeautifulSoup(resp.text, 'html.parser')
    table = soup.find('table', {'class': 'wikitable'})
    rows = table.find_all('tr')
    constellations = []
    for row in rows:
        tag_a = row.find('a')
        cleaned_data = {}
        if tag_a and 'wiki' in tag_a['href']:
            cleaned_data['name_ru'] = tag_a.text.strip()
            cleaned_data['link'] = 'https://ru.wikipedia.org/'+tag_a['href']
            slug = tag_a.find_next('td')
            cleaned_data['slug'] = slug['data-sort-value'].strip().replace(' ', '_').lower()
            cleaned_data['name'] = slug['data-sort-value'].strip()
            short_name = slug.find_next('td').find_next('td')
            cleaned_data['short_name'] = short_name.text.strip()
            square = short_name.find_next('td')
            cleaned_data['square'] = int(re.sub(r"\[.*?\]", "", square.text.strip()))
            total_stars = square.find_next('td')
            cleaned_data['total_stars'] = int(total_stars.text.strip())
            symbol = re.sub('thumb/', '', 'https:'+total_stars.find_next('img')['src'])
            symbol = re.sub('/20px-.*', '', symbol)
            cleaned_data['symbol'] = symbol
            constellations.append(cleaned_data)
    return constellations


if __name__ == '__main__':
    print(len(main()))
