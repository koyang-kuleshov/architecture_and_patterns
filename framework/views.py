from mainapp.catalog import Catalog, Item
from framework.body_generator import body_generator
from framework.common import HTML, CSS


def index_view(request=None):
    spam = Catalog.show_all_items()
    data = []
    for row in spam:
        data.append(list(row))
    data = body_generator('index', data)
    return '200 OK', data, HTML


def add_item(request=None):
    data = body_generator('add_item')
    return '200 OK', data, HTML


def add_item_script(request=None):
    if request is not None:
        Item.add_item(request['data'])
    return '200 OK', 'Товар добавлен. <a href="/">Перейти на главную</a>', HTML


def styles(request=None):
    return '200 OK', '/templates/styles.css', CSS
