

from abc import ABC, abstractmethod


class People(ABC):
    
    def __init__(self):
        self.name = None
        self.birth = None
        
    # def set_name(self, name):
    #     self.__name = name
    
    # def get_name(self):
    #     return self.__name
        
    # def set_birth(self, birth):
    #     self.__birth = birth
    
    # def get_birth(self):
    #     return self.__birth
    
    @abstractmethod
    def calculate_age(self, birth, year):
        pass
        
        