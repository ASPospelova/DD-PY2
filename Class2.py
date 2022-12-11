import doctest


class Hanger:
    def __init__(self, number_of_hangers: int, number_of_coats: int):
        """
        Создание и подготовка к работе объекта "Вешалка"
        :param number_of_hangers: Кол-во плечиков
        :param number_of_coats: Кол-во пальто, которое нужно развесить на плечиках
        Примеры:
        >>> hanger = Hanger(6, 6)  # инициализация экземпляра класса
        """
        if not isinstance(number_of_hangers, int):
            raise TypeError("Кол-во плечиков должно быть типа int или float")
        if number_of_hangers <= 0:
            raise ValueError("Если число плечиков < 0, то вешать не на что")
        self.number_of_hangers = number_of_hangers

        if not isinstance(number_of_coats, int):
            raise TypeError("Кол-во пальто, которое нужно развесить на плечиках должно быть типа int")
        if number_of_coats < 0:
            raise ValueError("Если число пальто < 0, то вешать нечего")
        if number_of_coats > number_of_hangers:
            raise ValueError("Если число пальто > числа плечиков, то вешать лишние пальто некуда")
        self.number_of_coats = number_of_coats

    def remove_coat_from_Henger(self, estimate_coat: int) -> None:
        """
        Снять пальто с вешалки.
        :param estimate_coat: Кол-во снятых пальто
        :raise ValueError: Если количество снятых пальто превышает количество пальто на вешалке,
        то возвращается ошибка.
        :return: Объем реально снятых пальто
        Примеры:
        >>> hanger = Hanger(6, 6)
        >>> hanger.remove_coat_from_Henger(2)
        """
        ...


if __name__ == "__main__":
    doctest.testmod()  # тестирование примеров, которые находятся в документации