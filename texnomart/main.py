from base_parser import BaseParser
import time
from bs4 import BeautifulSoup
from mixin import Product_Detail_Mixin
import re
import pdb; pdb.set_trace()


class Parser_itself(BaseParser, Product_Detail_Mixin):
    def __init__(self):
        super(Parser_itself, self).__init__()
        self.DATA = {}


    def category_parser(self, html, link, save_place):
        html = self.get_html(html)
        soup = BeautifulSoup(html, 'html.parser')
        categories = soup.find_all('div', class_='content__item')
        for category in categories[:3]:
            category_title = category.find('a').get_text(strip=True)
            print(f'Парсится категория {category_title}')
            category_link = self.host + category.find('a').get('href')
            self.DATA[category_title] = []

            category_page = self.get_html(category_link)
            self.category_page_parser(category_page, category_title, link, save_place)



    def category_page_parser(self, category_page, category_title, link, save_place):
        global product_title
        soup = BeautifulSoup(category_page, 'html.parser')
        container = soup.find('div', class_='products-box')
        try:
            products = container.find_all('div', class_='col-3')

            for product in products[:3]:
                product_title_element = product.find('a', class_='product-name f-14 c-373 mb-2 btn-link w-normal')
                if product_title_element:
                    product_title = product_title_element.get_text(strip=True)
                    print(f'Парсится продукт {product_title}')
                product_price = product.find('div', class_='f-16 w-bold-700 f-16 w-bold-700 mb-2.5').get_text(strip=True)
                product_image = product.find('img', class_='product-image').get('src')
                product_page_link = self.host + product.find('a', class_='product-link').get('href')

                product_detail_page = self.get_html(product_page_link)
                characteristics = self.get_detail_info_for_json(product_detail_page)
                inner_dict = characteristics["Основные характеристики"]
                characteristics_string = ", ".join([f'"{key}": "{value}"' for key, value in inner_dict.items()])

                self.DATA[category_title].append({
                    'Product_Name': product_title,
                    'Product_Price': product_price,
                    'Product_Image': product_image,
                    'Product_Page_Link': product_page_link,
                    'Characteristics': characteristics
                })

                pattern = r"/([^/]+)$"
                match = re.search(pattern, link)
                file_name = match.group(1)

                if save_place == 'JSON':
                    self.save_to_json(file_name, self.DATA)
                elif save_place == 'Database_MySQL':
                    self.save_to_database_MySQL(product_title, product_price, product_image, product_page_link, characteristics_string)
                elif save_place == 'Database_PG':
                    self.save_to_database_PostGres(product_title, product_price, product_image, product_page_link)




        except Exception as e:

            print(f"An error occurred while parsing: {e}")

            print(f'Категория {category_title} не имеет продуктов')


def start_parser():
    parser = Parser_itself()

    # https://texnomart.uz/ru/katalog/bytovaya-tehnika-dlya-doma-i-kuhn
    user_input = input('Введите ссылку: ')
    how_to_save = input('Введите куда сохранить (JSON, Database_MySQL, Database_PG): ')

    print('Парсер начал работу')
    start = time.time()

    parser.category_parser(user_input, user_input, how_to_save)

    finish = time.time()

    print(f'Парсер закончил работу за {round(finish - start, 2)} секунд')


start_parser()








