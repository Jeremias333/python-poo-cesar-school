from people import People


class Author(People):
    
    def __init__(self, author_name, name, birth):
        self.author_name = author_name
        self.name = name
        self.birth = birth