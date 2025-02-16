import doctest
class Car:
    def __init__(self, model: str, year: int):
        """
        Создание и подготовка к работе с объектом Car

        : model: модель транспорта
        : year: год создания транспорта

        Примеры:
        >>> BMW = Car("BMW", 2024) #инициализация экземпляра класса
        """
        if not isinstance(model, str):
            raise TypeError("Модель должна иметь тип string")
        if model == "":
            raise ValueError("Модель должна иметь название")

        if not isinstance(year, int):
            raise TypeError("Год создания должен быть типа int")
        if year > 2024 or year < 1900:
            raise ValueError("Год создания не может быть больше 2024 или меньше 1900")

        self._model = model #поля model и year непубличные, потому что возможно случайное изменение данных полей, а такие поля как модель и год создания не могут изменяться
        self._year = year


    def __str__(self):
        return f"Модель: {self._model}, год создания: {self._year}"

    def __repr__(self):
        return f"Модель: {self._model}, год создания: {self._year}"

    def drive(self) -> str:
        """
        Метод возвращает строку, описывающую маршрут

        : return: строка с описанием маршрута
        >>> BMW = Car("BMW", 2024) #инициализация экземпляра класса
        >>> BMW.drive()

        # Пример маршрута
        routes = [
            "A",
            "B",
            "C",
            "B",
            "A"
        ]

        return f"Модель: {self._model}, маршрут: {routes}"
        """

    def getCoordinates(self) -> str:
        """
        Метод показывает текущие координаты транспорта.

        :return: строка с координатами
        Метод получает текущие координаты и возвращает их
        return f"Координаты {self.model}: Широта {56.5}, Долгота {62.3}"

        Пример:
        >>> BMW = Car("BMW", 2024) #инициализация экземпляра класса
        >>> BMW.getCoordinates()
        """



class PassengerCar(Car):
    def __init__(self, model: str, year: int, max_speed: float):
        """
        Инициализация объекта PassengerCar, наследует от Car.

        : model: модель автомобиля
        : year: год выпуска автомобиля
        : max_speed: максимальная скорость автомобиля
        """
        super().__init__(model, year)

        if not isinstance(max_speed, (int, float)):
            raise TypeError("Максимальная скорость должна быть типа int или float")
        if max_speed > 500:
            raise ValueError("Максимальная скорость не может быть большее 500 км/ч")

        self._max_speed = max_speed # поле непубличное изменение максимальной скорости происходит через метод

    def __str__(self) -> str:
        """
        Переопределенный метод потому что выводится дополнительная информация о максимальной скорости
        """
        return f"Модель: {self._model}, год создания: {self._year} , максимальная скорость: {self._max_speed} км/ч"

    def __repr__(self) -> str:
        """
        Переопределенный метод потому что выводится дополнительная информация о максимальной скорости
        """
        return f"Модель: {self._model}, год создания: {self._year} , максимальная скорость: {self._max_speed} км/ч"

    def setMax_speed(self, new_max_speed: float):
        """
        Обновление грузоподъемности. Позволяет увеличить или уменьшить грузоподъемность

        : new_max_speed: новая макс скорость

        if new_max_speed <= 0:
            raise ValueError("Максимальная скорость должна быть положительным числом")
        self._max_speed = new_max_speed
        """

    def drive(self) -> str:
        """
        Перегруженный метод
        Метод возвращает строку, описывающую маршрут A-B, то есть от точки до пункта назначения (такси)

        : return: строка с описанием маршрута для легкового автомобиля

        Пример:
        >>> BMW = PassengerCar("BMW", 2024, 250) #инициализация экземпляра класса
        >>> BMW.drive()

        # Пример маршрута
        routes = [
            "A",
            "B",
        ]

        return f"Модель: {self._model}, маршрут: {routes}"
        """



class Truck(Car):
    def __init__(self, model: str, year: int, payload: float):
        """
        Создание и подготовка к работе с объектом Truck, наследуется от Car

        : model: модель автомобиля
        : year: год выпуска автомобиля
        : payload: грузоподъемность
        """
        super().__init__(model, year)

        if not isinstance(payload, (int, float)):
            raise TypeError("Грузоподъемность должна быть типа int или float")
        if payload <= 0:
            raise ValueError("Грузоподъемность должна быть положительным числом")

        self._payload = payload #поле грузоподъемность непубличное чтобы исключить возможность изменения не через метод

    def __str__(self) -> str:
        """
        Переопределенный метод потому что выводится дополнительная информация о грузоподъемности
        """
        return f"Модель: {self._model}, год создания: {self._year}, грузоподъемность: {self._payload} кг"

    def __repr__(self) -> str:
        """
        Переопределенный метод потому что выводится дополнительная информация о грузоподъемности
        """
        return f"Модель: {self._model}, год создания: {self._year}, грузоподъемность: {self._payload} кг"

    def setPayload(self, new_payload: float):
        """
        Обновление грузоподъемности, например, транспорт может быть поврежден, поэтому максимальная грузоподъемность должна быть снижена

        : new_payload: новая грузоподъемность

        if new_payload <= 0 or new_payload >= 20:
            raise ValueError("Грузоподъемность должна быть положительным числом и не больше 20 тонн)")
        self._payload = new_payload
        """

    def drive(self) -> str:
        """
        Перегруженный метод
        Метод возвращает строку, описывающую маршрут A-B-C-B-A, то есть от склада до пункта назначения и обратно на склад(доставка)

        : return: строка с описанием маршрута для грузового автомобиля
        Пример:
        >>> GAZ = Truck("GAZ", 2020, 12.5) #инициализация экземпляра класса
        >>> GAZ.drive()

        # Пример маршрута
        routes = [
            "A",
            "B",
            "C",
            "B",
            "A"
        ]

        return f"Модель: {self._model}, маршрут: {routes}"
        """

if __name__ == "__main__":
    doctest.testmod()
    car1 = PassengerCar("BMW", 2022, 220)
    truck1 = Truck("GAZ", 2020, 10.5)

    # Вывод информации о транспортных средствах
    print(car1)  # Легковой автомобиль BMW, 2022 года, макс. скорость: 220 км/ч
    print(truck1)  # Грузовой автомобиль GAZ, 2020 года, грузоподъемность: 10.5 тонн

    # Обновление максимальной скорости
    car1.setMax_speed(200)
    print(car1)  # Легковой автомобиль BMW, 2022 года, макс. скорость: 200 км/ч

    # Обновление грузоподъемности
    truck1.setPayload(12.5)
    print(truck1)  # Грузовой автомобиль GAZ, 2020 года, грузоподъемность: 10.5 тонн
