import doctest
# TODO Написать 3 класса с документацией и аннотацией типов
class Car:
    def __init__(self, model: str, year: int, max_speed: int):
        """
        Создание и подготовка к работе с объектом Car

        : model: модель транспорта
        : year: год создания транспорта
        : max_speed: максимальная скорость транспорта

        Примеры:
        >>> BMW = Car("BMW", 2024, 200) #инициализация экземпляра класса
        """
        if not isinstance(model, str):
            raise TypeError("Модель должна иметь тип string")
        if model == "":
            raise ValueError("Модель должна иметь название")

        if not isinstance(year, int):
            raise TypeError("Год создания должен быть типа int")
        if year > 2024 or year < 1900:
            raise ValueError("Год создания не может быть больше 2024 или меньше 1900")

        if not isinstance(max_speed, (int, float)):
            raise TypeError("Максимальная скорость должна быть типа int или float")
        if max_speed > 300:
            raise ValueError("Максимальная скорость не может быть большее 300 км/ч")

        self.model = model
        self.year = year
        self.max_speed = max_speed

    def drive(self) -> str:
        """
        Метод позволяет управлять машиной, возвращает строку состоящая из маршрута

        : return: строка показывающая маршрут

        Примеры:
        >>> BMW = Car("BMW", 2024, 200)
        >>> bmw_route = BMW.drive()
        """
        ...
    def GetCoordinates(self) -> str:
        """
        Метод показывает текущие координаты транспорта

        : return: строка состоящая из координат

        Примеры:
        >>> BMW = Car("BMW", 2023, 150)
        >>> bmw_coordinates = BMW.GetCoordinates()
        """
        ...

class Phone:
    def __init__(self, model: str, cost: float):
        """
        Создание и подготовка к работе с объектом Phone

        : model: модель телефона
        : cost: цена телефона

        Примеры:
        >>> apple = Phone("iphone 13", 50000)
        """
        if not isinstance(model, str):
            raise TypeError("Модель телефона должна иметь тип string")
        if model == "":
            raise ValueError("Модель телефона должна иметь название")

        if not isinstance(cost, (int, float)):
            raise TypeError("Цена должна быть типа int или float")
        if cost < 0:
            raise ValueError("Цена не может быть меньше нулю")

        self.model = model
        self.cost = cost

    def call(self, phone_number: str) -> None:
        """
        Метод совершает звонок по номеру телефона в аргументе

        : phone_number: номер телефона на который нужно совершить звонок
        Пример:
        >>> apple = Phone("iphone 13", 50000)
        >>> apple.call("+70009989868")
        """
        if not isinstance(phone_number, (str, int)):
            raise TypeError("Номер телефона должен быть строкой либо int")

        # проверка на корректность номера

        self.phone_number = phone_number
        ...

    def install_app(self, app_name: str) -> None:
        """
        Метод устанавливает приложение

        : app_name: название приложения

        Пример:
        >>> apple = Phone("iphone 13", 50000)
        >>> apple.install_app("gosuslugi")
        """
        if not isinstance(app_name, str):
            raise TypeError("Название должно быть строкой")
        self.app_name = app_name
        ...

class Employee:
    def __init__(self, name: str, position: str):
        """
        Создание и подготовка объекта Employee

        : name: имя сотрудника
        : position: должность сотрудника

        Пример:
        >>> employee = Employee("Ivan", "Director")
        """
        if not isinstance(name, str):
            raise TypeError("Имя должно иметь тип string")
        if name == "":
            raise ValueError("Имя должно иметь название")

        if not isinstance(position, str):
            raise TypeError("Должность должна иметь тип string")
        if position == "":
            raise ValueError("Должность должна иметь название")
        self.name = name
        self.position = position
        ...

    def work(self) -> str:
        """
        Метод с которым сотрудник делает работу

        : return: строка описывающая проделанную работу

        Пример:
        >>> employee = Employee("Ivan", "Director")
        >>> employee_work = employee.work()
        """
        ...

    def receive_salary(self) -> float:
        """
        Метод рассчитывает зарплату

        : return: возвращает зарплату
        Пример:
        >>> employee = Employee("Ivan", "Director")
        >>> employee_salary = employee.receive_salary()
        """
        ...

if __name__ == "__main__":
    doctest.testmod()

