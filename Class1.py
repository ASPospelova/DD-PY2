import doctest


class Chair:
    def __init__(self, legs_: int, number_of_people_sitting: int):
        """
        Создание и подготовка к работе объекта "Кровать"
        :param legs_: Количество ножек у стула
        :param number_of_people_sitting: Кол-во людей, которые могут сесть на стул полностью одновременно
        Примеры:
        >>> chair = Chair(4, 1)  # инициализация экземпляра класса
        """
        if not isinstance(legs_, int):
            raise TypeError("Кол-во ножек должно быть типа int")
        if legs_ < 3:
            raise ValueError("Кол-во ножек не может быть меньше 3")
        self.legs_ = legs_

        if not isinstance(number_of_people_sitting, (int)):
            raise TypeError("Кол-во людей, которые могут сесть на стул полностью одновременно должно быть типа int")
        if number_of_people_sitting > 1:
            raise ValueError("Людям будет неудобно")
        self.number_of_people_sitting = number_of_people_sitting

    def is_occupied_chair(self) -> bool:
        """
        Функция которая проверяет сидит ли кто-нибудь на стуле
        :return: Свободен ли стул
        Примеры:
        >>> chair = Chair(3, 0)
        >>> chair.is_occupied_chair()
        """
        ...

    def add_guest_to_chair(self, guest: int) -> None:
        """
        Приглашение гостя присесть.
        :param guest: Кол-во гостей
        :raise ValueError: Если количество гостей превышает 1, то вызываем ошибку
        Примеры:
        >>> chair = Chair(3, 0)
        >>> chair.add_guest_to_chair(1)
        """
        if not isinstance(guest, int):
            raise TypeError("Кол-во гостей должно быть типа int")
        if guest > 1:
            raise ValueError("Людям будет неудобно")
        ...



if __name__ == "__main__":
    doctest.testmod()  # тестирование примеров, которые находятся в документации
    