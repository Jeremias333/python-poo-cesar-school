from music.album import Album
from music.author import Author
from music.music import Music

def main():
    author = Author(author_name="The Beatles", birth=1960)
    album = Album(title="Rubber Soul", length=34.55, tracks=14, year=1965, genre="Rock")
    music = Music(title="Think for yourself", duration=2.18, extension="mp3", album=album, author=author)
    
    print(music)
    print(f"Este é o nome do autor do album {music.album.title}, {music.author.name} ")
    print(f"Vamos ouvir a faixa: {music.title} que tem a duração de {music.duration}s")
    print(music.get_title_and_extension())


if __name__ == "__main__":
    main()