import requests
from bs4 import BeautifulSoup
import csv  # встроенная библиотека для работы с CSV

url = 'https://habr.com/ru/rss/articles/'
response = requests.get(url)

if response.status_code != 200:
    print('Ошибка загрузки RSS:', response.status_code)
    exit()

soup = BeautifulSoup(response.text, 'xml')
items = soup.find_all('item')

# Открываем файл для записи CSV
with open('habr_articles.csv', 'w', encoding='utf-8-sig', newline='') as file:
    writer = csv.writer(file, delimiter =';')
    # Пишем заголовки столбцов
    writer.writerow(['Заголовок', 'Ссылка', 'Дата'])

    for item in items:
        title = item.find('title').text.strip()
        link = item.find('link').text.strip()
        pub_date = item.find('pubDate').text.strip()
        
        print(title)          # для контроля
        writer.writerow([title, link, pub_date])

print('Готово! Данные сохранены в habr_articles.csv')
