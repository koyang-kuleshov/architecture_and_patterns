from mainapp.catalog import Catalog, Category, Item


def _create_category(name):
    category_id = len(Catalog.category_list)
    new_category = Category(category_id, name)
    Catalog.category_list.append(new_category)
    return new_category


def _update_category(category_id, name, price_modifier):
    spam = Catalog.category_list[category_id].\
        update_category(category_id, name, price_modifier)
    return spam


def _remove_category_item(item_id):
    category_id = Item.item_list[item_id].category_id
    item_idx = Item.item_list[item_id].item_idx
    del Catalog.category_list[category_id].category_items[item_idx]
    spam = Item.item_list[item_id].remove_item
    return spam


def _remove_category(category_id):
    cat = Catalog.category_list[category_id]
    spam = type(cat), cat.remove_category
    del Catalog.category_list[category_id]
    return spam


def _create_item(category_id, item_style, item_name, item_size):
    spam = Catalog.category_list[category_id].add_category_item(item_style,
                                                                item_name,
                                                                item_size
                                                                )
    return spam


def _update_item(item_id, item_style, item_name, item_size):
    spam = Item.item_list[item_id].update_item(item_style, item_name,
                                               item_size)
    return spam


def _remove_item(item_id):
    spam = Item.item_list[item_id].remove_item
    del Item.item_list[item_id]
    return spam
