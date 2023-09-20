import requests
from bs4 import BeautifulSoup
import sqlite3

user_input_link = 'https://www.themoscowtimes.com/news'
user_input_category = 'https://www.themoscowtimes.com/news'


def news_parser(link, category, data_dict):
    html = requests.get(link).text
    soup = BeautifulSoup(html, 'html.parser')
    news_blocks = soup.find_all('div', class_='col-4 col-12-md col-4-sm')

    for news_block in news_blocks:
        news_title = news_block.find('a').get('title')
        news_publisher = news_block.find('span').get_text(strip=True)
        news_image = news_block.find('img').get('src')
        news_link = news_block.find('a').get('href')

        data_dict[category] = {
            'Title': news_title,
            'Publisher': news_publisher,
            'Image': news_image,
            'Link': news_link
        }

        db = sqlite3.connect('news.db')
        cursor = db.cursor()

        try:
            cursor.execute('''
            INSERT INTO news(Title, Publisher, Image, Link) 
            VALUES (?, ?, ?, ?) 
            ''', (news_title, news_publisher, news_image, news_link))

            db.commit()
        except sqlite3.OperationalError:
            print('Error inserting data into database.')

        db.close()


news = {}
news_parser(user_input_link, user_input_category, news)















