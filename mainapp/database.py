"""
Database class with memento pattern
"""
import json


class GetState:
    def __init__(self, elem):
        with open('database.json', 'r') as file_r:
            data = json.load(file_r)
        return data


class SetState:
    def __init__(self, elem):
        try:
            with open('database.json', "w") as file_w:
                json.dump(elem, file_w)
        except Exception as err:
            return err
        else:
            return True
