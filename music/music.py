from .album import Album
from .author import Author

class Music():
    
    def __init__(self, title:str, duration:float, extension:str, 
                 album: Album = None, author: Author = None):
        self.title = title
        self.duration = duration
        self.extension = extension
        self.album = album
        self.author = author

    def get_title_and_album_name(self):
        return f"{self.title} - {self.album.title}"
    
    def get_title_and_album_name_and_duration(self):
        return f"{self.title} - {self.album.title} - {self.duration}s"
    
    def get_title_and_extension(self):
        return f"{self.title}.{self.extension}"
