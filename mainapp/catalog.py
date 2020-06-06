from abc import ABC, ABCMeta, abstractmethod
from random import randrange
from datetime import date
import requests

from database import GetState, SetState


class CurrencyRateService(metaclass=ABCMeta):
    @abstractmethod
    def get_currency_rate(self, currency):
        pass


class CbrCurrencyRateService(CurrencyRateService):
    def get_currency_rate(self, _now):
        try:
            resp = requests.get(
                'https://www.cbr-xml-daily.ru/daily_json.js')
        except Exception:
            return self.currency_rate['previous']
        else:
            spam = resp.json()["Valute"]["USD"]
            Catalog.currency_rate[_now] = spam["Value"]
            Catalog.currency_rate['_now'] = spam["Value"]
            Catalog.currency_rate['previous'] = spam["Previous"]
            return spam["Value"]


class ProxyCurrencyRateService(CurrencyRateService):
    def __init__(self):
        self.currencyRateService = CbrCurrencyRateService()
        self.rate = Catalog.currency_rate
        self._now = str(date.today())

    @property
    def get_currency_rate(self):
        try:
            spam_date = self.rate[self._now]
        except KeyError:
            self.rate[self._now] = self.currencyRateService.\
                get_currency_rate(self._now)
            return self.rate[self._now]
        else:
            return spam_date


class Catalog:
    currency_rate = dict()
    currency_rate['_now'] = 70.0
    category_list = list()

    def __init__(self):
        pass

    def __str__(self):
        return str({'currency_rate': ProxyCurrencyRateService().get_currency_rate,
                    'category_list': Catalog.category_list})

    def show_category(cls, category_id):
        return cls.category_list[category_id]

    def show_all_categories(cls):
        return {'categories': cls.category_list}

    def search(self):
        pass


class Category:
    def __init__(self, category_id, name, price_modifier=1.0):
        self.category_id = category_id
        self.category_name = name
        self._price_modifier = price_modifier
        self.category_items = list()
        self._is_active = True

    def __str__(self):
        dict_to_json = {'category_id': self.category_id,
                        'category_name': self.category_name,
                        'category_items_qty': len(self.category_items),
                        'category._is_active': self._is_active}
        return str(dict_to_json)

    def add_category_item(self, item_style, item_name, item_size):
        item_idx = len(self.category_items)
        new_item = Item(self.category_id, item_idx, item_style, item_name,
                        item_size)
        self.category_items.append(new_item)
        return new_item

    def show_items(self):
        return self.category_items

    def update_category(self, category_id, name='', price_modifier=0):
        if name:
            self.category_name = name
        if price_modifier != 0:
            self._price_modifier = price_modifier
        dict_to_json = {'category_id': self.category_id,
                        'category_name': self.category_name,
                        'category_items_qty': len(self.category_items),
                        'category._is_active': self._is_active}
        return dict_to_json

    def remove_category_item(self, item_id):
        spam = self.category_items[item_id]
        del self.category_items[item_id]
        return spam

    @property
    def remove_category(self):
        self._is_active = False
        return self._is_active


class GoodItem(ABC):

    @abstractmethod
    def _get_fabric_price(self):
        pass

    @abstractmethod
    def _set_fabric_price(self):
        pass

    @abstractmethod
    def get_price(self):
        pass


class Item(GoodItem):
    item_list = list()

    def __init__(self, category_id, item_idx, item_style, item_name,
                 item_size):
        self.category_id = category_id
        self.item_idx = item_idx
        self.item_id = len(self.item_list)
        self.item_style = item_style
        self.item_name = item_name
        self.item_size = item_size
        self._fabric_price = self._get_fabric_price
        self._now = str(date.today())
        SetState(self)

    def __str__(self):
        dict_to_json = {
            'category_id': self.category_id,
            'item_idx': self.item_idx,
            'item_id': self.item_id,
            'item_style': self.item_style,
            'item_name': self.item_name,
            'item_size': self.item_size,
            'item_price': self.get_price
        }
        return str(dict_to_json)

    @property
    def _get_fabric_price(self):
        self._fabric_price = randrange(2, 300)
        return self._fabric_price

    def _set_fabric_price(self):
        self._fabric_price = float(input('Введите закупочную стоимость: '))

    def add_to_order(self, item_id):
        return Item.item_list[item_id]

    def update_item(self, item_id, item_style='', item_name='', item_size=''):
        if item_style:
            self.item_style = item_style
        if item_name:
            self.item_name = item_name
        if item_size:
            self.item_size = item_size
        dict_to_json = {
            'category_id': self.category_id,
            'item_id': self.item_id,
            'item_style': self.item_style,
            'item_name': self.item_name,
            'item_size': self.item_size,
            'item_price': self.get_price
        }
        return dict_to_json

    @property
    def remove_item(self):
        self._is_active = False
        return self._is_active

    @property
    def get_price(self):
        self.price = Catalog.currency_rate['_now'] * self._fabric_price
        return self.price

