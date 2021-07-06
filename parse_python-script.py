import csv
import requests
import bs4
response = requests.get('https://python-scripts.com/virtualenv')
soup = bs4.BeautifulSoup(response.text, 'lxml')

def writeData(data, file):
    writer = csv.writer(file)
    writer.writerow(['id', 'title'])
    for row in data:
        print(row)
        writer.writerow(row)


block = soup.find('div', class_='entry-content')
block_h2 = block.find_all('h2')

with open('ps_table.csv', 'w') as file:
    data = list()

    for i, item in enumerate(block_h2):
        data.append(
            [i, item.text]
        )
    print(data)

    writeData(data, file)