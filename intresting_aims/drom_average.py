import requests
import re
from bs4 import BeautifulSoup


class Response:

    def result(self, link: str):
        res = requests.get(link)
        if res.status_code == 200:
            return res
        return None

class Execute:
    MILES = []
    PRICE = []
    CITY = []
    YEAR = []

    def boiled_soup(self, html: str):
        self.soup = BeautifulSoup(html, 'lxml')
        self.div = self.soup.find(attrs={'class': 'css-1nvf6xk eqhdpot0'})
        self.cards = self.div.findAll('a')

    def execute_milege_page(self):
        for iter in self.cards:
            try:
                content = iter.find(attrs={'data-ftid': 'component_inline-bull-description'}).findAll('span')[-1].text
                formatter = re.findall(r'\d*\.\d+|\d+', content)[0]
                self.MILES.append(int(formatter))
            except:
                pass
    def execute_price_page(self):
        for iter in self.cards:
            try:
                content = iter.findAll(attrs={'data-ftid':'bull_price'})[0].text
                formatter = content.replace('\xa0', '')
                self.PRICE.append(int(formatter))
            except:
                pass

    def execute_city_page(self):
        for iter in self.cards:
            try:
                content = iter.find(attrs={'data-ftid': 'bull_location'}).text
                formatter = content.strip()
                self.CITY.append(str(formatter).lower())
            except:
                pass

    def execute_year_page(self):
        for iter in self.cards:
            try:
                content = iter.find(attrs={'data-ftid': 'bull_title'}).text
                formatter = content.split(',')[-1].strip()
                self.YEAR.append(int(formatter))
            except:
                pass

    def execute_next_page(self):
        try:
            link = self.soup.find(attrs={'data-ftid': 'component_pagination-item-next'}).get('href')
            return link
        except:
            return None

class Parse(Response, Execute):
    def __init__(self, filter_link: str):
        self.link = filter_link
        self.PAGE_COUNT = 1

    def content_from_response(self):
        res = self.result(self.link)
        if res is not None:
            print(f'Страница {self.PAGE_COUNT}')
            self.boiled_soup(res.content)
            self.execute_milege_page()
            self.execute_price_page()
            self.execute_city_page()
            self.execute_year_page()
            link = self.execute_next_page()
            if link is not None:
                self.PAGE_COUNT += 1
                self.link = link
                self.content_from_response()

    def average(self) -> tuple[int, int, int]:
        miles_ave = int(sum(self.MILES) / len(self.MILES)) * 1000
        price_ave = int(sum(self.PRICE) / len(self.PRICE))
        year_ave = int(sum(self.YEAR) / len(self.YEAR))
        return miles_ave, price_ave, year_ave

    def max_min(self) -> tuple[int, int, int, int]:
        miles_min = min(self.MILES) * 1000
        miles_max = max(self.MILES) * 1000

        price_min = min(self.PRICE)
        price_max = max(self.PRICE)

        return miles_min, miles_max, price_min, price_max

    def city_popular(self) -> tuple[str, list]:
        filter_count = []
        city = ''
        qty_most_common = 0
        city_set = set(self.CITY)
        for item in city_set:
            qty = self.CITY.count(item)
            filter_count.append(f'{str(item).upper()} = {qty} штук')
            if qty > qty_most_common:
                qty_most_common = qty
                city = item
        return city, filter_count

if __name__ == '__main__':
    link = input('Ссылка: ')
    print('\nСчитаю...\n')
    w = Parse(link)
    w.content_from_response()
    m, p, y = w.average()
    m_min, m_max, p_min, p_max = w.max_min()
    c, c_l_f = w.city_popular()

    print(f'\nЦена:\nСредняя = {p} руб\nМинимальная = {p_min} руб\nМаксимальная = {p_max} руб\n\nПробег:\nСредний = {m} км\nМинимальный = {m_min}\nМаксимальный = {m_max}\n\nСредний год = {y}\n\nПопулярный город продажи = {c.upper()}')