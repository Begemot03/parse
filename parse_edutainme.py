import requests
import bs4
import re
import json

url = 'https://edutainme.timepad.ru/events/'
headers = {
    'user-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:89.0) Gecko/20100101 Firefox/89.0'
}

events_info = []

def get_data(url):
    response = requests.get(url, headers)
    src = response.text
    soup = bs4.BeautifulSoup(src, 'lxml')
    events = soup.find_all('div', class_='t-card t-card_event t-card_event-public t-card_event__passed')

    for event in events:
        event_name = event.find('a').text.strip()
        try:
            event_background_img_style = event.find('div', class_='__poster').get('style')
            event_background_img_reference = event_background_img_style[event_background_img_style.find('(') + 1:len(event_background_img_style) - 1]
        except Exception:
            event_background_img_reference = 'no reference'
        
        try:
            event_time_start = event.find('p', class_='t-card_event__info').text.strip()
        except Exception:
            event_time_start = 'no start time'
        
        try:
            event_description = event.find('p', 't-description').text.strip()
        except Exception:
            event_description = 'no description'

        try:
            event_mainlink = event.find('div', class_='__c').find('a').get('href')
        except Exception:
            event_mainlink = 'no link'

        events_info.append({
                'event_name': event_name, 
                'event_background_img': event_background_img_reference, 
                'event_start_time': event_time_start, 
                'event_description': event_description, 
                'event_link': event_mainlink
            }
        )

get_data(url)

with open('parse/edutainme_data,json', 'w', encoding='utf-8') as file:
    json.dump(events_info, file, indent=4, ensure_ascii=False)
#print(events_info)
    