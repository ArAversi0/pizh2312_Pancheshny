# Time Manager

1. Описание

Мини-приложение предоставляет пользователю возможность создавать, редактировать, сохранять и загружать временные отрезки, а также выполнять арифметические операции с ними. Приложение поддерживает различные форматы представления времени, включая стандартный 24-часовой формат, военный формат и формат с AM/PM.

---

2. Цели и задачи

- Предоставить удобный инструмент для учета и управления временем.
- Реализовать возможность выполнения арифметических операций с временными отрезками.
- Обеспечить поддержку различных форматов представления времени.
- Предоставить возможность сохранения и загрузки данных.
- Реализовать функциональность секундомера.

---

3. Функциональные требования

- Управление временем:

  - Создание объектов времени с указанием часов, минут и секунд.
  - Редактирование объектов времени.
  - Вывод времени в различных форматах (стандартный, военный, AM/PM).
  - Преобразование времени в секунды, минуты и часы.
  - Выполнение арифметических операций (сложение, вычитание) с временными отрезками.
  - Сохранение и загрузка объектов времени в JSON-файл.

- Секундомер:

  - Запуск и остановка секундомера.
  - Вычисление прошедшего времени.
  - Отображение прошедшего времени в удобном формате.

- Интерфейс пользователя:
  - Консольный интерфейс или графический интерфейс (на выбор разработчика).
  - Удобный и интуитивно понятный интерфейс для работы с приложением.
  - Отображение информации о времени в выбранном формате.
  - Отображение результатов арифметических операций и работы секундомера.

---

4. Список задач

   1. Реализовать класс Time с необходимыми методами и свойствами.
   1. Реализовать классы MilitaryTime и FormattedTime, наследующие от Time.
   1. Реализовать класс Stopwatch для работы с секундомером.
   1. Разработать интерфейс пользователя (консольный или графический).
   1. Реализовать функции для выполнения арифметических операций с временем.
   1. Реализовать функции для сохранения и загрузки данных.
   1. Реализовать функции для работы с секундомером.
   1. Протестировать приложение на корректность работы всех функций.
   1. Документировать код и интерфейс приложения.

---

5. Учебные задачи

- Изучение предметной области объекта и доступных операций:
  - Определить, какие операции можно выполнять с объектом времени (сложение, вычитание, сравнение и т.д.).
  - Изучить доступные форматы представления времени (24-часовой, военный, AM/PM).
- Проектирование полей и методов:
  - Для каждого поля и метода определить его область видимости (публичный, приватный).
  - Определить необходимость использования свойств для доступа к полям.
- Реализация специальных методов:
  - Реализовать метод **init** для инициализации объекта с необходимыми параметрами.
  - Реализовать метод **str** для представления объекта в удобном для человека виде.
- Реализация методов класса:
  - Реализовать метод from_string для создания объекта из строки.
  - Реализовать методы save и load для сохранения и загрузки объекта в JSON-файл.
  - Реализовать не менее 3-х дополнительных методов и свойств, выявленных на этапе изучения класса.

---

## Демонстрация работы

- Исходный код time_classes.py:

```python

import json
from typing import Optional

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

- Исходный код stopwatch.py:
```python

from time_classes import Time
from typing import Optional

class Stopwatch:
    # Класс для представления секундомера.

    def __init__(self) -> None:
        # Инициализация секундомера.
        self._start_time: Optional[Time] = None
        self._end_time: Optional[Time] = None

    def start(self, start_time: Time) -> None:
        # Запуск секундомера.
        self._start_time = start_time  # Устанавливает время начала

    def stop(self, end_time: Time) -> None:
        # Остановка секундомера.
        self._end_time = end_time  # Устанавливает время окончания

    def elapsed_time(self) -> Optional[Time]:
        # Вычисление прошедшего времени.
        if self._start_time and self._end_time:
            return self._end_time - self._start_time  # Возвращает прошедшее время
        else:
            return None  # Возвращает None, если секундомер не был запущен или остановлен
```

- Исходный код main.py с демонстрацией функционала:

```python

# Импортирование всех классов
from time_classes import Time, MilitaryTime, FormattedTime, Stopwatch

# Создание объектов Time
time1 = Time(10, 30, 45)
time2 = Time.from_string("12:15:30")

# Вывод времени
print(f"Time 1: {time1}")  # Вывод: Time 1: 10:30:45
print(f"Time 2: {time2}")  # Вывод: Time 2: 12:15:30

# Арифметические операции
time3 = time1 + time2
time4 = time2 - time1
print(f"Time 1 + Time 2: {time3}")  # Вывод: Time 1 + Time 2: 22:46:15
print(f"Time 2 - Time 1: {time4}")  # Вывод: Time 2 - Time 1: 01:44:45

# Преобразование времени
print(f"Time 1 в секундах: {time1.to_seconds()}")  # Вывод: Time 1 в секундах: 37845
print(f"Time 2 в минутах: {time2.to_minutes()}")  # Вывод: Time 2 в минутах: 735
print(f"Time 3 в часах: {time3.to_hours()}")  # Вывод: Time 3 в часах: 22.770833333333332

# Сохранение и загрузка времени
time1.save("time1.json")
time5 = Time()
time5.load("time1.json")
print(f"Загруженное время: {time5}")  # Вывод: Загруженное время: 10:30:45

# Военное время
military_time = MilitaryTime(15, 45, 0)
print(f"Военное время: {military_time}")  # Вывод: Военное время: 1545

# Форматированное время
formatted_time = FormattedTime(15, 45, 30)
print(f"Форматированное время: {formatted_time}")  # Вывод: Форматированное время: 03:45:30 PM

# Секундомер
stopwatch = Stopwatch()
start_time = Time(10, 0, 0)
stop_time = Time(10, 0, 10)
stopwatch.start(start_time)
stopwatch.stop(stop_time)
elapsed_time = stopwatch.elapsed_time()
print(f"Прошедшее время секундомера: {elapsed_time}")  # Вывод: Прошедшее время секундомера: 00:00:10
```

1. Успешно создаётся объект Time с начальными аргументами (за счёт констуктора)
2. Поддерживается создание объекта Time с использованием входной строки (позволяет так делать метод from_string("ЧЧ:ММ:СС")), происходит успешно и без ошибок.
3. Время успешно выводится на экран, если требуется.
4. Операции сложения и вычитания времени работают корректно, формируется новый экземпляр класса, где атрибуты часов, минут и секунд есть результат сложения или же вычитания.
5. Преобразование времени только в часы, минуты или секунды работает исправно.
6. Создание и сохранение в json файл времени выполняется корректно, как и считывание времени из json.
7. Реализованные 2 формата времени работают. Успешно создаются экземпляры классов MilitaryTime и FormattedTime
8. Функционал класса Stopwatch работает как надо (отношение композиции между ним и базовым классом Time)

---

### UML-диаграмма классов

![Time_manager UML](https://sun9-34.userapi.com/impg/rba2t4OQvtCyFZS91inrz3OneZ3PStfLKdS30Q/AN3UFsUBsZ8.jpg?size=1180x790&quality=95&sign=579c2b61ca236aa7709081b82cc0e887&type=album)
