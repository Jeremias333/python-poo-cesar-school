from .people import People

#criando herança
class Author(People):
    def __init__(self, author_name, birth, name_official=None):
        self.name = author_name
        self.name_official = name_official
        self.birth = birth
    
    def calculate_age(self, birth, year):
        return year - birth
    