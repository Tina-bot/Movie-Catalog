from os import *
from domain.movie import Movie
from service.movie_catalog import MovieCatalog as cp


option = None

while option != 4:

    try:
        print('Options :')
        print('1-Add Movie')
        print('2-List Movies')
        print('3-Delete Catalog [!]')
        print('4-Exit')
        option = int(input("Choise (1-4) : \n"))

        if option == 1:
            name_movie = input("Movie Name: ")
            movie = Movie(name_movie)
            cp.add_movie(movie)
        elif option == 2:
            cp.list_movie()
        elif option == 3:
            cp.del_movies()

    except Exception as e:
        print (f'Error {e}')
        option = None


else:
    print('Goodbye')
