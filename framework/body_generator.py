from framework.header import header
from framework.footer import footer


def body_generator(data):
    result = header
    for item in data:
        spam = (f'<h2>Артикул: {item[3]}</h2><p>Наименование: {item[4]}</p>'
                f'<p>Размер: {item[5]}')
        result += spam
    result += footer
    return result
