"""
Database class with mapper
"""

from mainapp.catalog import Item


class DatabaseMapper:
    def __init__(self, connection):
        self.connection = connection
        self.cursor = connection.cursor()

    def find_by_id(self, item_id):
        statement = "SELECT category_id, item_idx, item_style, item_name, \
            item_size FROM items WHERE item_id=?"
        self.cursor.execute(statement, (item_id,))
        result = self.cursor.fetchall()
        if result:
            return Item(*result[0])
        else:
            return None

    def insert(self, item):
        statement = "INSERT INTO items (category_id, item_idx, item_style, \
            item_name, item_size) VALUES (?, ?, ?, ?, ?)"
        self.cursor.execute(statement, (item.category_id, item.item_idx,
                                        item.item_style, item.item_name,
                                        item.item_size))
        try:
            self.connection.commit()
            return True
        except Exception as e:
            return e.args

    def update(self, item):
        statement = "UPDATE items SET category_id=?, \
                        item_idx=?, \
                        item_style=?, \
                        item_name=?, \
                        item_size=? \
                        WHERE item_id=?"
        self.cursor.execute(statement, (item.category_id, item.item_idx,
                                        item.item_style, item.item_name,
                                        item.item_size, item.item_id))
        try:
            self.connection.commit()
            return True
        except Exception as e:
            return e.args

    def delete(self, item):
        statement = "DELETE FROM items WHERE item_id=?"
        self.cursor.execute(statement, (item.item_id,))
        try:
            self.connection.commit()
            return True
        except Exception as e:
            return e.args
