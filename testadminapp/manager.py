from random import randint

from mainapp.catalog import Catalog, Category, Item


class Manager:
    """Class for store manager"""

    def __init__(self):
        self.manager_id = randint(100, 1000)
        return None

    def __str__(self):
        return f'Создан менеджер с id: {self.manager_id}'

    def _create_category(self, name):
        Catalog.create_category(name)

    def _update_category(self, category_id, name, price_modifier):
        Catalog.update_category(category_id, name, price_modifier)

    def _remove_category(self, category_id):
        Catalog.remove_category(category_id)

    def _create_item(self, category_id, item_style, item_name):
        Catalog.category_list[category_id].add_category_item(category_id,
                                                             item_style,
                                                             item_name
                                                             )

    def _update_item(self, item_id, item_style, item_name):
        Item[item_id].update_item(item_style, item_name)

    def _remove_item(self, item_id):
        Catalog.category_list[Item.item_list[item_id].category_id].\
            remove_category_item(item_id)
        del Item.item_list[item_id]
