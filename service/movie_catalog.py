import os


class MovieCatalog:

    rute_archive = 'movie.txt'

    @classmethod
    def add_movie(cls, movie):
        with open(cls.rute_archive, 'a', encoding='utf-8') as archive:
            archive.write(f'{movie.title}\n')

    @classmethod
    def list_movie(cls):
        with open(cls.rute_archive, 'r', encoding='utf-8') as archive:
            print('Movie Catalog'.center(50, '-'))
            print(archive.read())

    @classmethod
    def del_movies(cls):
        os.remove(cls.rute_archive)
        print("Deleted sucefull")
