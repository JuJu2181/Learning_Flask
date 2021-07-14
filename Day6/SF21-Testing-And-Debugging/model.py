import json

class FruitDB:
    def __init__(self) -> None:
        self.__data = None
    
    def connect(self, data_file):
        with open(data_file) as json_file:
            self.__data = json.load(json_file)
    
    def get_data(self, name):
        for  fruit in self.__data['Fruits']:
            if fruit['name'] == name:
                return fruit
    
    def close(self):
        pass


class FruitSalad:
    def __init__(self) -> None:
        self.__data = []
    
    def add(self, fruit):
        self.__data.append(fruit)
    
    def contain(self, fruit):
        if fruit in self.__data:
            return True
        else:
            return False
    
    def remove(self, fruit):
        if self.contain(fruit):
            self.__data.remove(fruit)
        else:
            raise NameError


