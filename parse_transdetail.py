import bs4
import requests

url = 'https://transdetail.ru/catalog/'

src = requests.get(url)

with open('ali_data.txt', 'w') as file:
    file.write(src.text)

