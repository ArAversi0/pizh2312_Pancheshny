# Программирование на языке высокого уровня (Python).
# Задание №4.3.4. Вариант 4
#
# Выполнил: Панчешный Александр Алексеевич
# Группа: ПИЖ-б-о-23-1-2
# E-mail: pancheshny2020@yandex.ru

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