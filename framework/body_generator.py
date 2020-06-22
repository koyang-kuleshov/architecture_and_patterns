import sys
import os
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, BASE_DIR)

from templates.header import header
from templates.footer import footer
from templates.add_item import add_item


def body_generator(template, data=None):
    result = header
    if template == 'index':
        for item in data:
            spam = (f'<h2>Артикул: {item[3]}</h2><p>Наименование: '
                    f'{item[4]}</p><p>Размер: {item[5]}')
            result += spam
    elif template == 'add_item':
        result += add_item
    result += footer
    return result
