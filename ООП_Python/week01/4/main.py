class Point:
    """
    Класс, представляющий точку на плоскости.
    """

    def __init__(self, x, y):
        """
        Конструктор класса Point.

        Аргументы:
            x (int или float): Координата x точки.
            y (int или float): Координата y точки.
        """
        self.x = x
        self.y = y

    def __add__(self, other):
        """
        Перегрузка оператора сложения (+).

        Определяет, что происходит при сложении двух объектов Point.
        Создает и возвращает новый объект Point, координаты которого являются суммой координат исходных точек.

        Аргументы:
            other (Point): Второй объект Point, который будет добавлен к текущему объекту.

        Возвращает:
            Point: Новый объект Point, представляющий сумму двух точек.
        """
        if isinstance(other, Point): # Проверяем, является ли other объектом класса Point
            new_x = self.x + other.x
            new_y = self.y + other.y
            return Point(new_x, new_y) # Создаем и возвращаем новый объект Point
        else:
            return NotImplemented # Если other не Point, возвращаем NotImplemented, чтобы Python попытался использовать __radd__

    def __str__(self):
        """
        Метод для строкового представления объекта Point.

        Возвращает:
            str: Строка в формате "(x, y)".
        """
        return f"({self.x}, {self.y})"

    # Пример реализации __radd__ (правостороннее сложение)
    def __radd__(self, other):
        """
        Перегрузка оператора правостороннего сложения (+).

        Вызывается, если self находится справа от оператора +, а левый операнд не имеет метода __add__.

        Аргументы:
            other: Левый операнд оператора +.

        Возвращает:
            Point: Новый объект Point (в данном случае всегда возвращается None).
        """
        if other == 0:  #  Позволяет использовать sum() со списком объектов Point.
            return self
        else:
            return NotImplemented

# Пример использования
point1 = Point(1, 2)
point2 = Point(3, 4)

point3 = point1 + point2  # Используем перегруженный оператор +
print(f"point1: {point1}") # Выводим point1
print(f"point2: {point2}") # Выводим point2
print(f"point1 + point2 = {point3}") # Выводим результат сложения

# Пример использования __radd__ (нужно для sum())
points = [Point(1, 1), Point(2, 2), Point(3, 3)]
total = sum(points)  # Используем встроенную функцию sum() с объектами Point
print(f"Sum of points: {total}")