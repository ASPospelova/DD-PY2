import doctest


class SaltShaker:
    def __init__(self, salt: float, capacity_of_the_salt_shaker: float):
        """
        Создание и подготовка к работе объекта "Солонка"
        :param salt: кол-во соли в кг
        :param capacity_of_the_salt_shaker: вместимость солонки в л
        Примеры:
        >>> salt_shaker = SaltShaker(0.36, 0.45)  # инициализация экземпляра класса
        """
        if not isinstance(salt, (int, float)):
            raise TypeError("Кол-во соли должно быть типа int или float")
        if salt <= 0:
            raise ValueError("Кол-во соли должно быть положительным числом")
        self.salt = salt

        if not isinstance(capacity_of_the_salt_shaker, (int, float)):
            raise TypeError("Вместимость солонки должна быть int или float")
        if capacity_of_the_salt_shaker < 0:
            raise ValueError("Вместимость может быть отрицательным числом")
        self.capacity_of_the_salt_shaker = capacity_of_the_salt_shaker

    def is_empty_saltshaker(self) -> bool:
        """
        Функция которая проверяет является ли солонка пустой
        :return: Является ли солонка пустой
        Примеры:
        >>> salt_shaker = SaltShaker(0.3, 0.5)
        >>> salt_shaker.is_empty_saltshaker()
        """
        ...

if __name__ == "__main__":
    doctest.testmod()  # тестирование примеров, которые находятся в документации