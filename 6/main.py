class Room:
    """
    Класс, представляющий комнату для расчета площади оклейки обоями.
    Содержит информацию о ширине, длине, высоте и списке поверхностей, не требующих оклейки.
    """

    def __init__(self, width, length, height, windows_and_doors):
        """
        Конструктор класса Room.

        Аргументы:
            width (float): Ширина комнаты.
            length (float): Длина комнаты.
            height (float): Высота комнаты.
            windows_and_doors (list): Список кортежей, представляющих размеры окон и дверей (ширина, высота).
        """
        self.width = width
        self.length = length
        self.height = height
        self.wd = windows_and_doors

    def get_full_area(self):
        """
        Вычисляет полную площадь стен комнаты.

        Возвращает:
            float: Полная площадь стен комнаты.
        """
        return 2 * (self.width + self.length) * self.height

    def get_wallpaper_area(self):
        """
        Вычисляет площадь поверхности, требующей оклейки обоями.

        Учитывает окна и двери.

        Возвращает:
            float: Площадь поверхности для оклейки обоями.
        """
        full_area = self.get_full_area()
        area_to_subtract = sum(w * h for w, h in self.wd)  # Суммируем площади всех окон и дверей
        return full_area - area_to_subtract

    def calculate_wallpaper_rolls(self, roll_width, roll_length):
        """
        Вычисляет необходимое количество рулонов обоев для оклейки комнаты.

        Аргументы:
            roll_width (float): Ширина рулона обоев.
            roll_length (float): Длина рулона обоев.

        Возвращает:
            int: Необходимое количество рулонов обоев.
        """
        wallpaper_area = self.get_wallpaper_area()
        roll_area = roll_width * roll_length
        num_rolls = wallpaper_area / roll_area
        return int(num_rolls + 1)  # Округляем в большую сторону, т.к. нельзя купить часть рулона


def get_user_input():
    """
    Получает данные от пользователя через консоль.

    Возвращает:
        tuple: Кортеж, содержащий ширину, длину, высоту комнаты и список окон и дверей.
    """
    width = float(input("Введите ширину комнаты: "))
    length = float(input("Введите длину комнаты: "))
    height = float(input("Введите высоту комнаты: "))

    num_wd = int(input("Введите количество окон и дверей: "))
    windows_and_doors = []
    for i in range(num_wd):
        width_wd = float(input(f"Введите ширину {i + 1}-го окна/двери: "))
        height_wd = float(input(f"Введите высоту {i + 1}-го окна/двери: "))
        windows_and_doors.append((width_wd, height_wd))

    return width, length, height, windows_and_doors


def main():
    """
    Основная функция программы.
    """
    width, length, height, windows_and_doors = get_user_input()

    room = Room(width, length, height, windows_and_doors)

    wallpaper_area = room.get_wallpaper_area()
    print(f"Площадь для оклейки обоями: {wallpaper_area:.2f}")

    roll_width = float(input("Введите ширину рулона обоев: "))
    roll_length = float(input("Введите длину рулона обоев: "))

    num_rolls = room.calculate_wallpaper_rolls(roll_width, roll_length)
    print(f"Необходимо рулонов обоев: {num_rolls}")


if __name__ == "__main__":
    main()