from album import Album
from author import Author

class Music():
    
    def __init__(self, name:str, duration:float, extension:str, 
                 genre:str, album: Album = None, author: Author = None):
        self.name = name
        self.duration = duration
        self.genre = genre
        self.extension = extension
        self.album = album
        self.author = author
        
