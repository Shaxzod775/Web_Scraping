from configs import host, url
import requests
import json
import sqlite3
import psycopg2


class BaseParser:
    def __init__(self):
        self.host = host
        self.url = url

    def get_html(self, link):
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
        }
        response = requests.get(link, headers=headers)
        try:
            response.raise_for_status()
            return response.content
        except requests.HTTPError:
            print(f'Произошла ошибка {response.status_code}')

    @staticmethod
    def save_to_json(path, data):
        with open(f'{path}.json', mode='w', encoding='UTF-8') as file:
            json.dump(data, file, ensure_ascii=False, indent=4)


    def save_to_database_MySQL(self, title, price, image, link, characteristics):
        db = sqlite3.connect('products.db')
        cursor = db.cursor()

        cursor.execute('''
        INSERT INTO texnomart_products(product_name, product_price, product_image, product_page_link, characteristics)
        VALUES (?, ?, ?, ?, ?)''', (title, price, image, link, characteristics))

        db.commit()
        db.close()

    def save_to_database_PostGres(self, title, price, image, link):
        database = psycopg2.connect(
            dbname='Sr-Sub-15-00',
            host='localhost',
            user='postgres',
            password='123456',
            port='5432'
        )
        cursor = database.cursor()

        cursor.execute('''
        INSERT INTO texnomart_products(product_title, price, image, product_page_link) 
        VALUES (%s, %s, %s, %s, %s) ''', (title, price, image, link))

        database.commit()
        database.close()











