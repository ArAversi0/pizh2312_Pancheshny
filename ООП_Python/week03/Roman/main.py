from roman import Roman, AdvancedRoman

def main():
    # Создание объектов Roman
    roman1 = Roman("XIX")
    roman2 = Roman("V")

    # Преобразование римского числа в десятичное
    decimal_value = Roman.to_decimal("XIV")
    print(f"Десятичное значение XIV: {decimal_value}")  # Вывод: 14

    # Преобразование десятичного числа в римское
    roman_value = Roman.to_roman(24)
    print(f"Римское значение 24: {roman_value}")  # Вывод: XXIV

    # Сложение римских чисел
    roman3 = roman1 + roman2
    print(f"{roman1.value} + {roman2.value} = {roman3.value}")  # Вывод: XIX + V = XXIV

    # Вычитание римских чисел
    roman4 = roman1 - roman2
    print(f"{roman1.value} - {roman2.value} = {roman4.value}")  # Вывод: XIX - V = XIV

    # Умножение римских чисел
    roman5 = roman1 * roman2
    print(f"{roman1.value} * {roman2.value} = {roman5.value}")  # Вывод: XIX * V = XCV

    # Деление римских чисел
    roman6 = roman1 / roman2
    print(f"{roman1.value} / {roman2.value} = {roman6.value}")  # Вывод: XIX / V = III

    # Создание объекта AdvancedRoman
    advanced_roman = AdvancedRoman("IX", "red")
    print(f"Цвет римского числа {advanced_roman.value}: {advanced_roman.get_color()}")  # Вывод: Цвет римского числа IX: red

if __name__ == "__main__":
    main()