import doctest


class Chair:
    def __init__(self, material: str, weight: float):
        """
        Создание и подготовка к работе объекта "Стул"

        Аргументы:
        :param material: Материал стула
        :param weight: Вес стула

        Примеры:
        >>> chair = Chair("wood", 5.1)

        >>> chair = Chair("wood", "bird")
        Traceback (most recent call last):
        ...
        TypeError: Вес стула должен быть int или float
        >>> chair = Chair("wood", -40)
        Traceback (most recent call last):
        ...
        ValueError: Вес стула должен быть положительным числом
        """
        if not isinstance(weight, (int, float)):
            raise TypeError("Вес стула должен быть int или float")
        if weight <= 0:
            raise ValueError("Вес стула должен быть положительным числом")
        self.weight = weight
        self.material = material

    def destroy(self) -> None:
        """
        Метод "уничтожить" стул

        Примеры:
        >>> chair = Chair("wood", 10.1)
        >>> chair.destroy()
        """
        ...

    def repair(self) -> None:
        """
        Метод "починить" стул

        Примеры:
        >>> chair = Chair("wood", 11.1)
        >>> chair.repair()
        """
        ...


class Human:
    def __init__(self, name: str, height: float):
        """
        Создание и подготовка к работе объекта "Человек"

        Аргументы:
        :param name: Имя человека
        :param height: Рост человека

        Примеры:
        >>> human = Human("Ivan", 50.0)
        """
        if not isinstance(height, (int, float)):
            raise TypeError("Рост человека должен быть int или float")
        if height <= 0:
            raise ValueError("Рост человека должен быть положительным числом")
        self.name = name
        self.height = height

    def sleep(self) -> None:
        """
        Метод "спать" человек

        Примеры:
        >>> human = Human("Igor", 52.1)
        >>> human.sleep()
        """
        ...

    def die(self) -> None:
        """
        Метод "умер" человек

        Примеры:
        >>> human = Human("Denis", 52.1)
        >>> human.die()
        """
        ...


class Animal:
    def __init__(self, specie: str, average_lifetime: float):
        """
        Создание и подготовка к работе объекта "Стул"

        Аргументы:
        :param specie: Вид животного
        :param average_lifetime: Средняя продолжительность жизни животного

        Примеры:
        >>> animal = Animal("chupacabra", 100)
        """
        if not isinstance(average_lifetime, (int, float)):
            raise TypeError("Средняя продолжительность жизни животного int или float")
        if average_lifetime <= 0:
            raise ValueError("Средняя продолжительность жизни животного должена быть положительным числом")
        self.specie = specie
        self.average_lifetime = average_lifetime

    def make_sound(self) -> str:
        """
        Метод "издать звук" животного

        :return: str: Звук животного

        Примеры:
        >>> animal = Animal("cat", 20)
        >>> animal.make_sound()
        """
        ...

    def eat(self) -> None:
        """
        Метод "покушать"

        Примеры:
        >>> animal = Animal("wolf", 5.1)
        >>> animal.eat()
        """
        ...


if __name__ == "__main__":
    doctest.testmod()
