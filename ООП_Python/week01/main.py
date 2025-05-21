class Vehicle:
    #Базовый класс для транспорта.
    def __init__(self, max_speed):
        self.max_speed = max_speed  # Максимальная скорость

    def accelerate(self, value):
        # Метод изменения скорости
        raise NotImplementedError("Этот метод должен быть переопределен")

class SeatsManager:
    # Класс-композиция для управления местами в автобусе
    def __init__(self, capacity):
        self.seats = {i: None for i in range(1, capacity + 1)}

    def has_empty_seats(self):
        # Проверка наличия свободных мест.
        return any(seat is None for seat in self.seats.values())

    def assign_seat(self, passenger):
        # Назначение места пассажиру.
        for seat, occupant in self.seats.items():
            if occupant is None:
                self.seats[seat] = passenger
                return True
            return False
    
    def remove_passenger(self, passenger):
        """Удаление пассажира с места."""
        for seat, occupant in self.seats.items():
            if occupant == passenger:
                self.seats[seat] = None
                return True
            return False

class Bus(Vehicle):
    # Класс Автобус, реализующий принципы ООП.
    def __init__(self, capacity, max_speed):
        super().__init__(max_speed)
        self.capacity = capacity  # Вместимость
        self.__speed = 0  # Инкапсулированная скорость
        self.__passengers = []  # Инкапсулированный список пассажиров
        self.__seats = SeatsManager(capacity)  # Композиция: управление местами

    @property
    def speed(self):
        # Геттер скорости
        return self.__speed

    @speed.setter
    def speed(self, value):
        # Сеттер скорости
        self.__speed = max(0, min(value, self.max_speed))
    
    def add_passenger(self, name):
        # Добавление пассажира
        if len(self.__passengers) < self.capacity and self.__seats.has_empty_seats():
            self.__passengers.append(name)
            self.__seats.assign_seat(name)
            return True
        return False
    
    def accelerate(self, value):
        # Увеличение/уменьшение скорости
        self.speed += value

    def remove_passenger(self, name):
        # Удаление пассажира
        if name in self.__passengers:
            self.__passengers.remove(name)
            self.__seats.remove_passenger(name)
            return True
        return False

    def __contains__(self, name):
        # Оператор 'in' для проверки наличия пассажира
        return name in self.__passengers

    def __iadd__(self, name):
        # Перегрузка оператора '+=' для посадки пассажира
        self.add_passenger(name)
        return self

    def __isub__(self, name):
        # Перегрузка оператора '-=' для высадки пассажира
        self.remove_passenger(name)
        return self

    def __call__(self):
        # Вызов объекта, чтобы показать текущее состояние
        return {
            "speed": self.__speed,
            "capacity": self.capacity,
            "passengers": self.__passengers,
            "has_empty_seats": self.__seats.has_empty_seats()
        }
    
bus_1 = Bus(capacity = 8, max_speed = 100)
bus_1 += "Alexander"  # Посадка пассажира через оператор +=
bus_1 += "Alexey"
bus_1.accelerate(50)  # Увеличение скорости
print("Alexey" in bus_1)  # Проверка наличия пассажира
bus_1 -= "Alexey"  # Высадка пассажира
print(bus_1())  # Вызов объекта, возвращающий текущее состояние

print(bus_1.speed)  # 50 (используется геттер)
bus_1.speed = 130   # Попытка установить скорость выше max_speed
print(bus_1.speed)  # 100 - ограничение
bus_1.speed = -10   # Попытка установить отрицательную скорость
print(bus_1.speed)  # 0 => ограничение сработало

print(bus_1._Bus__seats.seats) # Проверяем распределение мест