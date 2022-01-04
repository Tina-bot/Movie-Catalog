class Movie:

    def __init__(self, title):
        self._title = title

    def __str__(self):
        return f'Movie: {self._title}'

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, title):
        self._title = title
