"""
Database class with memento pattern
"""
import json


class GetState:
    def __call__():
        with open('database.json', 'r') as file_r:
            data = json.load(file_r)
        return data


class SetState:
    def __call___call__(elem):
        try:
            with open('database.json', "w") as file_w:
                json.dump(elem, file_w)
        except Exception as err:
            return err
        else:
            return True
