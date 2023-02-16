class Film:

    """Класс для фильма"""

    def __init__(self, name: str, length_in_minutes: int, actors: list):
        """Конструктор, в который передается название, длина фильма и список актеров"""
        self.name = name
        self.length_in_minutes = length_in_minutes
        self.is_watched = False
        self.actors = actors

    def __repr__(self) -> str:
        """Возвращает длину фильма"""
        return str(self.length_in_minutes) + " минут"

    def __str__(self) -> str:
        """Дает описание основной информации о фильме"""
        return 'Название фильма: ' + self.name + ', длина фильма: ' + repr(self)

    def set_watched(self):
        """Устанавливает значение, что фильм просмотрен"""
        self.is_watched = True

    def print_actors(self):
        """Выводит список актеров"""
        print('Актеры:')
        for actor in self.actors:
            print(actor)



class Anime(Film):

    """Класс для аниме"""

    def __init__(self, name: str, is_for_child: bool):
        """Конструктор, в который передается название аниме и информация, подходит ли он для детей"""
        self.name = name
        self.is_for_child = is_for_child

    def __repr__(self) -> str:
        """Возвращает текстовое значение для переменной is_for_child"""
        if self.is_for_child:
            return 'подходит для детей'
        else:
            return 'не подходит для детей'

    def __str__(self) -> str:
        """Выводит основную информацию об аниме"""
        return 'Название аниме: ' + self.name + ', ' + repr(self)

    def print_actors(self):
        """В аниме нет актеров, все персонажи нарисованные, поэтому метод перегружен"""
        print('Нет актеров')


film = Film("Титаник", 180, ["Леонардо Ди Каприо"])
print(film)
print(repr(film))
print("Фильм просмотрен: " + str(film.is_watched))
film.set_watched()
print("Фильм просмотрен: " + str(film.is_watched))
film.print_actors()

print()

anime = Anime("Тетрадь смерти", False)
print(anime)
print(repr(anime))
anime.print_actors()

if __name__ == "__main__":
    pass
