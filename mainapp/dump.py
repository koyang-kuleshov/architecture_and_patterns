"""
Database class with memento pattern
"""
import jsonpickle


class ItemSerializer:
    def serialize_items(self, items):
        return jsonpickle.dumps(items)

    def deserialize_items(self, items):
        return jsonpickle.loads(items)

    def dump_items(self, items, file_name):
        try:
            with open(file_name, 'w', encoding='utf-8') as file_w:
                items = self.serialize_items(items)
                file_w.write(items)
        except Exception as err:
            return err
        else:
            return True

    def load_items(self, file_name):
        try:
            with open(file_name, 'r', encoding='utf-8') as file_r:
                data = file_r.read()
        except Exception as err:
            return err
        else:
            items = self.deserialize_items(data)
        return items
