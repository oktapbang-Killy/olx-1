import requests
from bs4 import BeautifulSoup

for page in range(1, 4):
    print(f'Парсим {page} страницу:')
    url = f'https://www.olx.kz/list/q-елки/{page}/'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    items = soup.find_all('a', class_='css-rc5s2u')[:5] # <a class="css-rc5s2u" href="/d/obyavlenie/elki-novogodnie-IDnk6Gh.html">
    for index, item in enumerate(items, start=1):
        item_url = 'https://www.olx.kz' + item.get('href')
        item_response = requests.get(item_url)
        item_soup = BeautifulSoup(item_response.text, 'html.parser')
        description_tag = item_soup.find('meta', {'name': 'description'})
        if description_tag:
            description = description_tag.get('content', '').strip()
            print(f"{index}. {description}")
