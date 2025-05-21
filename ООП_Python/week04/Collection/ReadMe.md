# Приложение "Контейнер объектов"

---

## Описание

Данный проект представляет собой реализацию класса-контейнера на языке Python, предназначенного для хранения набора объектов. Класс-контейнер обеспечивает базовые операции для управления коллекцией объектов, включая добавление, удаление, индексацию, сохранение и загрузку данных из JSON-файла.

---

## Задачи

- Реализация класса-контейнера:

  1. Создать класс-контейнер, который будет содержать набор объектов заданного типа (например, VectorCollection для объектов Vector).
  1. Предусмотреть поле \_data для хранения набора объектов.

- Реализация специальных методов:

  1. Реализовать метод **init**(self, ...) для инициализации контейнера с необходимыми параметрами (например, начальным списком объектов).
  1. Реализовать метод **str**(self) для представления объекта в удобном для человека виде (например, вывод списка объектов).
  1. Реализовать метод **getitem**(self, index) для индексации и срезов контейнера.

- Реализация методов для управления данными:

  1. Реализовать метод add(self, value) для добавления элемента value в контейнер.
  1. Реализовать метод remove(self, index) для удаления элемента из контейнера по индексу index.
  1. Реализовать метод save(self, filename) для сохранения объекта в JSON-файл filename.
  1. Реализовать метод load(self, filename) для загрузки объекта из JSON-файла filename.

- Построение UML-диаграммы:
  1. Построить UML-диаграмму классов приложения, отражающую структуру классов и их взаимосвязи.

---

## Требования

1. Язык программирования: Python.
1. Класс-контейнер должен быть универсальным и поддерживать хранение объектов различных типов.
1. Методы save и load должны обеспечивать корректное сохранение и загрузку данных в формате JSON.
1. Код должен быть хорошо документирован и соответствовать стандартам PEP 8.
1. Необходимо предоставить UML-диаграмму классов.

---

### Исходный код main.py

```python

from time_classes import Time, MilitaryTime, FormattedTime
from typing import List, Union, Any
import json

class TimeCollection:
    def __init__(self, data: Union[List[Time], None] = None) -> None:
        """
        Инициализирует коллекцию времени.
        Args:
            data: Список объектов Time или None.
        """
        self._data: List[Time] = data if data is not None else []

    def __str__(self) -> str:
        """
        Возвращает строковое представление коллекции времени.
        Returns:
            Строка, представляющая коллекцию времени.
        """
        return "\n".join(str(time) for time in self._data)

    def __getitem__(self, index: int) -> Time:
        """
        Возвращает элемент коллекции по индексу.
        Args:
            index: Индекс элемента.
        Returns:
            Объект Time по указанному индексу.
        """
        return self._data[index]

    @property
    def data(self) -> List[Time]:
        """
        Возвращает список объектов Time в коллекции.
        Returns:
            Список объектов Time.
        """
        return self._data

    def add(self, value: Time) -> None:
        """
        Добавляет объект Time в коллекцию.
        Args:
            value: Объект Time для добавления.
        Raises:
            TypeError: Если value не является объектом Time.
        """
        if isinstance(value, Time):
            self._data.append(value)
        else:
            raise TypeError("Можно добавлять только объекты Time.")

    def remove(self, index: int) -> None:
        """
        Удаляет элемент из коллекции по индексу.
        Args:
            index: Индекс элемента для удаления.
        Raises:
            IndexError: Если индекс вне диапазона.
        """
        if 0 <= index < len(self._data):
            del self._data[index]
        else:
            raise IndexError("Индекс вне диапазона.")

    def save(self, filename: str) -> None:
        """
        Сохраняет коллекцию времени в JSON-файл.
        Args:
            filename: Имя файла для сохранения.
        """
        with open(filename, 'w') as f:
            json.dump([time.__dict__ for time in self._data], f)

    def load(self, filename: str) -> None:
        """
        Загружает коллекцию времени из JSON-файла.
        Args:
            filename: Имя файла для загрузки.
        Raises:
            FileNotFoundError: Если файл не найден.
        """
        try:
            with open(filename, 'r') as f:
                data = json.load(f)
                self._data = []
                for item in data:
                    time_type = item.pop('__class__', 'Time')
                    if time_type == 'MilitaryTime':
                        time_obj = MilitaryTime()
                    elif time_type == 'FormattedTime':
                        time_obj = FormattedTime()
                    else:
                        time_obj = Time()
                    time_obj.__dict__.update(item)
                    self._data.append(time_obj)
        except FileNotFoundError:
            raise FileNotFoundError(f"Файл {filename} не найден.")

if __name__ == "__main__":
    # Создание объектов
    time1 = Time(10, 30, 0)
    time2 = MilitaryTime(14, 45, 0)
    time3 = FormattedTime(8, 15, 30)

    # Добавление объектов классов при инициализации объекта TimeCollection
    time_collection = TimeCollection([time1, time2, time3])

    print("Исходная коллекция:")
    print(time_collection) # Вывод коллекции объектов

    time_collection.add(Time(12, 0, 0)) # Добавление нового объекта в коллекцию
    print("\nКоллекция после добавления:")
    print(time_collection) # Вывод коллекции объектов

    time_collection.remove(1) # Удаление объекта с соответствующим индексом
    print("\nКоллекция после удаления элемента с индексом 1:")
    print(time_collection) # Вывод коллекции объектов

    time_collection.save("time_collection.json") # сохраняем в json файл коллекцию объектов

    new_time_collection = TimeCollection() # Создаём пустую коллекцию
    new_time_collection.load("time_collection.json") # Заполняем новую коллекцию, загружая старую из json файла.

    print("\nКоллекция после загрузки из файла:")
    print(new_time_collection) # Вывод коллекции объектов
```

### Исходный код файла time_classes.py

```python

import json

class Time:
    # Базовый класс для представления времени.

    def __init__(self, hours: int = 0, minutes: int = 0, seconds: int = 0) -> None:
        # Инициализация объекта времени.
        self._hours = hours
        self._minutes = minutes
        self._seconds = seconds

    @property
    def hours(self) -> int:
        # Получить часы.
        return self._hours  # Возвращает текущее значение часов

    @hours.setter
    def hours(self, value: int) -> None:
        # Установить часы.
        if 0 <= value < 24:
            self._hours = value  # Устанавливает новое значение часов
        else:
            raise ValueError("Часы должны быть в диапазоне от 0 до 23.")

    @property
    def minutes(self) -> int:
        # Получить минуты.
        return self._minutes  # Возвращает текущее значение минут

    @minutes.setter
    def minutes(self, value: int) -> None:
        # Установить минуты.
        if 0 <= value < 60:
            self._minutes = value  # Устанавливает новое значение минут
        else:
            raise ValueError("Минуты должны быть в диапазоне от 0 до 59.")

    @property
    def seconds(self) -> int:
        # Получить секунды.
        return self._seconds  # Возвращает текущее значение секунд

    @seconds.setter
    def seconds(self, value: int) -> None:
        # Установить секунды.
        if 0 <= value < 60:
            self._seconds = value  # Устанавливает новое значение секунд
        else:
            raise ValueError("Секунды должны быть в диапазоне от 0 до 59.")

    def __str__(self) -> str:
        # Представление объекта в виде строки.
        return f"{self.hours:02}:{self.minutes:02}:{self.seconds:02}"  # Возвращает строку в формате ЧЧ:ММ:СС

    def __add__(self, other: 'Time') -> 'Time':
        # Сложение времени.
        if isinstance(other, Time):
            total_seconds = self.hours * 3600 + self.minutes * 60 + self.seconds + \
                            other.hours * 3600 + other.minutes * 60 + other.seconds
            hours = total_seconds // 3600 % 24
            minutes = total_seconds % 3600 // 60
            seconds = total_seconds % 60
            return Time(hours, minutes, seconds)  # Возвращает новый объект Time, представляющий сумму времени
        else:
            raise TypeError("Операнд должен быть объектом Time.")

    def __sub__(self, other: 'Time') -> 'Time':
        # Вычитание времени.
        if isinstance(other, Time):
            total_seconds1 = self.hours * 3600 + self.minutes * 60 + self.seconds
            total_seconds2 = other.hours * 3600 + other.minutes * 60 + other.seconds
            diff_seconds = total_seconds1 - total_seconds2
            if diff_seconds < 0:
                raise ValueError("Результат вычитания отрицательный.")
            hours = diff_seconds // 3600 % 24
            minutes = diff_seconds % 3600 // 60
            seconds = diff_seconds % 60
            return Time(hours, minutes, seconds)  # Возвращает новый объект Time, представляющий разницу во времени
        else:
            raise TypeError("Операнд должен быть объектом Time.")

    @classmethod
    def from_string(cls, time_string: str) -> 'Time':
        # Создание объекта Time из строки.
        try:
            hours, minutes, seconds = map(int, time_string.split(':'))
            return cls(hours, minutes, seconds)  # Возвращает новый объект Time, созданный из строки
        except ValueError:
            raise ValueError("Неверный формат времени. Ожидается 'ЧЧ:ММ:СС'.")

    def save(self, filename: str) -> None:
        # Сохранение объекта в JSON-файл.
        with open(filename, 'w') as f:
            json.dump({'hours': self.hours, 'minutes': self.minutes, 'seconds': self.seconds}, f)  # Сохраняет объект в JSON-файл

    def load(self, filename: str) -> None:
        # Загрузка объекта из JSON-файла.
        try:
            with open(filename, 'r') as f:
                data = json.load(f)
                self.hours = data['hours']
                self.minutes = data['minutes']
                self.seconds = data['seconds']  # Загружает объект из JSON-файла
        except FileNotFoundError:
            raise FileNotFoundError(f"Файл {filename} не найден.")

    def to_seconds(self) -> int:
        # Преобразование времени в секунды.
        return self.hours * 3600 + self.minutes * 60 + self.seconds  # Возвращает время в секундах

    def to_minutes(self) -> int:
        # Преобразование времени в минуты.
        return self.hours * 60 + self.minutes  # Возвращает время в минутах

    def to_hours(self) -> float:
        # Преобразование времени в часы.
        return self.hours + self.minutes / 60 + self.seconds / 3600  # Возвращает время в часах


class MilitaryTime(Time):
    # Класс для представления военного времени (24-часовой формат).

    def __str__(self) -> str:
        # Представление военного времени в виде строки.
        return f"{self.hours:02}{self.minutes:02}"  # Возвращает строку в формате ЧЧММ


class FormattedTime(Time):
    # Класс для представления времени в формате с AM/PM.

    def __str__(self) -> str:
        # Представление времени в формате с AM/PM.
        hours = self.hours % 12
        if hours == 0:
            hours = 12
        am_pm = "AM" if self.hours < 12 else "PM"
        return f"{hours:02}:{self.minutes:02}:{self.seconds:02} {am_pm}"  # Возвращает строку в формате "ЧЧ:ММ:СС AM/PM"
```

---

### UML-диаграмма классов:

![UML-диаграмма](https://sun9-36.userapi.com/impg/a3hrOReBDbx-V1ZGruP4EKIuDLa84iRq43AlmA/DcKQgadBPFk.jpg?size=632x769&quality=95&sign=7407b95a9f4abd0ba2339758e5e8cf46&type=album)
