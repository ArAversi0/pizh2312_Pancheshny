# Программирование на языке высокого уровня (Python).
# Задание №4.3.5. Вариант N/A
#
# Выполнил: Панчешный Александр Алексеевич
# Группа: ПИЖ-б-о-23-1-2
# E-mail: pancheshny2020@yandex.ru

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