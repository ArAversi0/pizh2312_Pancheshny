# Класс "Автобус"

1. Общие требования
   Необходимо реализовать класс Bus, который моделирует работу автобуса.
   Класс должен содержать свойства и методы, обеспечивающие посадку и высадку пассажиров, управление скоростью и работу с местами в салоне.
   При реализации должны быть использованы принципы ООП: абстракция, наследование, инкапсуляция, полиморфизм, композиция.

2. Свойства класса Bus

- speed – текущая скорость автобуса.
- capacity – максимальное количество пассажиров.
- maxSpeed – максимальная скорость автобуса.
- passengers – список имён пассажиров.
- hasEmptySeats – наличие свободных мест (True/False).
- seats – словарь с распределением пассажиров по местам ({номер места: имя пассажира}).

3. Методы класса Bus
   Управление пассажирами:

- add_passenger(name) – посадка пассажира (если есть свободные места).
  remove_passenger(name) – высадка пассажира (если он находится в автобусе).
  Управление скоростью:
- accelerate(value) – изменение скорости на заданное значение (с учётом максимального ограничения).
  Геттер speed и сеттер speed, ограничивающий диапазон значений (0 ≤ скорость ≤ maxSpeed).

## Перегрузка операторов (полиморфизм):

- \_\_\contains\_\_(name) – оператор in, проверяющий, находится ли пассажир в автобусе.
- \_\_\iadd\_\_(name) – оператор += для посадки пассажира (bus += "Alice").
- \_\_\isub\_\_(name) – оператор -= для высадки пассажира (bus -= "Bob").

## Композиция (управление местами):

- Класс SeatMap, который отвечает за распределение мест в автобусе:
  -has_empty_seats() – проверяет, есть ли свободные места.
- assign_seat(name) – назначает пассажиру место.
- remove_passenger(name) – освобождает место.
- Вызываемый метод (\_\_\call\_\_):

\_\_\call\_\_() – возвращает текущее состояние автобуса (скорость, пассажиры, наличие мест).

4. Требования к реализации ООП

- Абстракция – скрытие деталей работы автобуса, предоставление удобного интерфейса.
- Наследование – Bus наследует базовый класс Vehicle (определяет максимальную скорость).
- Инкапсуляция – защищённые свойства (**speed, **passengers, \_\_seats).
- Полиморфизм – перегрузка операторов +=, -=, in, () для удобного управления.
- Композиция – использование SeatMap для управления местами.

## Полный код main.py:

```python

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
```
