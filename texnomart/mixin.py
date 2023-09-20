# from bs4 import BeautifulSoup
#
# class Product_Detail_Mixin:
#
#     def get_detail_info(self, page):
#         characterisitcs = {}
#         soup = BeautifulSoup(page, 'html.parser')
#         sections = soup.find_all('div', class_='characteristic-wrap less-characteristic')
#         try:
#             for section in sections:
#                 title = section.find('div', class_='title text-base font-medium mb-4 letter-2 1024:mb-6').get_text(strip=True)
#                 info_list = section.find_all('div', class_='list')
#                 section_characteristics = {}
#                 for info in info_list:
#                     key = info.find('span', class_='mr-1.5').get_text(strip=True)
#                     value = info.find('div', class_='list__value letter-2 text-right').get_text(strip=True)
#                     section_characteristics[key] = value
#                 characterisitcs[title] = section_characteristics
#
#         except Exception as e:
#             print(e)
#
#         return characterisitcs





from bs4 import BeautifulSoup

class Product_Detail_Mixin:

    def get_detail_info_for_json(self, page):
        characterisitcs = {}
        soup = BeautifulSoup(page, 'html.parser')
        sections = soup.find_all('div', class_='characteristic-wrap less-characteristic')
        try:
            for section in sections:
                title = section.find('div', class_='title text-base font-medium mb-4 letter-2 1024:mb-6').get_text(strip=True)
                info_list = section.find_all('div', class_='list')
                characterisitcs[title] = {
                    i.find('span', class_='mr-1.5').get_text(strip=True): i.find('div', class_='list__value letter-2 text-right').get_text(strip=True)
                    for i in info_list
                }
        except:
            pass

        return characterisitcs














