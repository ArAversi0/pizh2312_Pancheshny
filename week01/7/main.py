import math

class Snow:
    """
    Класс для представления количества снежинок и выполнения операций с ними.
    """

    def __init__(self, snowflakes):
        """
        Конструктор класса Snow.

        Аргументы:
            snowflakes (int): Начальное количество снежинок. Должно быть целым числом.
        """
        if not isinstance(snowflakes, int):
            raise TypeError("Количество снежинок должно быть целым числом.")
        self.snowflakes = snowflakes

    def __add__(self, other):
        """
        Перегрузка оператора сложения (+).

        Увеличивает количество снежинок на число или на количество снежинок в другом объекте Snow.

        Аргументы:
            other (int или Snow): Число или объект Snow, который нужно прибавить.

        Возвращает:
            Snow: Новый объект Snow с увеличенным количеством снежинок.
        """
        if isinstance(other, (int, Snow)): # Проверяем тип аргумента
            if isinstance(other, Snow):
                new_snowflakes = self.snowflakes + other.snowflakes # Складываем, если other - Snow
            else:
                new_snowflakes = self.snowflakes + other # Складываем, если other - int
            return Snow(new_snowflakes)
        else:
            raise TypeError("Сложение возможно только с целым числом или объектом Snow.")

    def __sub__(self, other):
        """
        Перегрузка оператора вычитания (-).

        Уменьшает количество снежинок на число или на количество снежинок в другом объекте Snow.

        Аргументы:
            other (int или Snow): Число или объект Snow, который нужно вычесть.

        Возвращает:
            Snow: Новый объект Snow с уменьшенным количеством снежинок.
        """
        if isinstance(other, (int, Snow)): # Проверяем тип аргумента
            if isinstance(other, Snow):
                new_snowflakes = self.snowflakes - other.snowflakes # Вычитаем, если other - Snow
            else:
                new_snowflakes = self.snowflakes - other # Вычитаем, если other - int

            if new_snowflakes < 0:  # Проверка, чтобы количество снежинок не стало отрицательным
                new_snowflakes = 0
            return Snow(new_snowflakes)
        else:
            raise TypeError("Вычитание возможно только с целым числом или объектом Snow.")

    def __mul__(self, other):
        """
        Перегрузка оператора умножения (*).

        Увеличивает количество снежинок в указанное число раз.

        Аргументы:
            other (int): Число, на которое нужно умножить количество снежинок.

        Возвращает:
            Snow: Новый объект Snow с увеличенным количеством снежинок.
        """
        if isinstance(other, int):  # Проверяем тип аргумента
            new_snowflakes = self.snowflakes * other
            return Snow(new_snowflakes)
        else:
            raise TypeError("Умножение возможно только на целое число.")

    def __truediv__(self, other):
        """
        Перегрузка оператора деления (/).

        Делит количество снежинок на указанное число, округляя результат до целого числа.

        Аргументы:
            other (int): Число, на которое нужно разделить количество снежинок.

        Возвращает:
            Snow: Новый объект Snow с уменьшенным (после деления и округления) количеством снежинок.
        """
        if isinstance(other, int):  # Проверяем тип аргумента
            if other == 0: # Предотвращаем деление на ноль
                raise ZeroDivisionError("Деление на ноль недопустимо.")
            new_snowflakes = round(self.snowflakes / other)  # Выполняем деление и округляем
            return Snow(new_snowflakes)
        else:
            raise TypeError("Деление возможно только на целое число.")

    def makeSnow(self, snowflakes_per_row):
        """
        Создает текстовое представление снежинок, распределенных по рядам.

        Аргументы:
            snowflakes_per_row (int): Количество снежинок в каждом ряду.

        Возвращает:
            str: Строка, представляющая снежинки, распределенные по рядам, разделенным символом новой строки.
        """
        if not isinstance(snowflakes_per_row, int):
            raise TypeError("Количество снежинок в ряду должно быть целым числом.")

        if snowflakes_per_row <= 0:
            return "" # Если количество снежинок в ряду не положительное, возвращаем пустую строку

        rows = self.snowflakes // snowflakes_per_row  # Вычисляем количество рядов
        remainder = self.snowflakes % snowflakes_per_row  # Вычисляем остаток снежинок
        snow_string = ""
        for _ in range(rows):  # Создаем строки с полным количеством снежинок
            snow_string += "*" * snowflakes_per_row + "\n"
        snow_string += "*" * remainder  # Добавляем строку с остатком снежинок
        return snow_string

    def __call__(self, new_snowflakes):
        """
        Перегрузка оператора вызова (()).

        Позволяет изменить количество снежинок в объекте, вызывая его как функцию.

        Аргументы:
            new_snowflakes (int): Новое количество снежинок.
        """
        if not isinstance(new_snowflakes, int):
            raise TypeError("Количество снежинок должно быть целым числом.")
        self.snowflakes = new_snowflakes

    def __str__(self):
        """
        Строковое представление объекта Snow.
        """
        return f"Snowflakes: {self.snowflakes}"


# Пример использования
try:
    snow1 = Snow(15)
    snow2 = Snow(7)

    print(f"snow1: {snow1}")
    print(f"snow2: {snow2}")

    snow3 = snow1 + snow2
    print(f"snow1 + snow2 = {snow3}")

    snow4 = snow3 - 5
    print(f"snow3 - 5 = {snow4}")

    snow5 = snow4 * 3
    print(f"snow4 * 3 = {snow5}")

    snow6 = snow5 / 4
    print(f"snow5 / 4 = {snow6}")

    print(f"snow1 makeSnow(5):\n{snow1.makeSnow(5)}")

    snow1(25)  # Перезапись значения
    print(f"snow1 after calling snow1(25): {snow1}")
except (TypeError, ZeroDivisionError) as e:
    print(f"Ошибка: {e}")