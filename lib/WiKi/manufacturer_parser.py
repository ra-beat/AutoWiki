import requests
from bs4 import BeautifulSoup
from Entity.WiKi.manufacturer import Manufacturer as ManufacturerEntity
from typing import List


class Manufacturer:
    def __init__(self):
        self.manufacturer_url = "https://ru.wikipedia.org/wiki/%D0%9A%D0%B0%D1%82%D0%B5%D0%B3%D0%BE%D1%80%D0%B8%D1%8F:%D0%90%D0%B2%D1%82%D0%BE%D0%BC%D0%BE%D0%B1%D0%B8%D0%BB%D0%B8_%D0%BF%D0%BE_%D0%BC%D0%B0%D1%80%D0%BA%D0%B0%D0%BC"
        self.category_list_class = "mw-category mw-category-columns"
        self.category_group_class = "mw-category-group"

    def get_html_content(self) -> str:
        response = requests.get(self.manufacturer_url)
        return response.text

    @staticmethod
    def get_manufacturer(content: BeautifulSoup) -> ManufacturerEntity:
        link_element = content.find('a', href=True)

        link = link_element.get('href')
        name = link_element.text.strip()

        name = name.replace('Автомобили', '').strip()

        return ManufacturerEntity(link, name)

    @staticmethod
    def parse(html_content) -> List[BeautifulSoup]:
        soup = BeautifulSoup(html_content, 'html.parser')
        return soup.find_all('div', class_='mw-category-group')

    def manufacturers(self) -> List[ManufacturerEntity]:
        html_content = self.get_html_content()
        categories = self.parse(html_content)
        manufacturers = []

        for category in categories:
            manufacture = self.get_manufacturer(category)
            manufacturers.append(manufacture)

        return manufacturers
