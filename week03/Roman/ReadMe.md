# класс Roman (Римское число)

- Цель: Создать класс Roman, представляющий римские числа и поддерживающий основные арифметические операции.

---

## Задачи:

1. Создание класса Roman:
   - Реализовать класс Roman для представления римских чисел.
   - Обеспечить возможность инициализации объекта класса с римским числом в виде строки.
2. Реализация статических методов преобразования:
   - Реализовать статический метод to_decimal для преобразования римского числа в десятичное.
   - Реализовать статический метод to_roman для преобразования десятичного числа в римское.
3. Реализация арифметических операций:
   - Перегрузить оператор + (**add**) для сложения двух римских чисел.
   - Перегрузить оператор - (**sub**) для вычитания двух римских чисел.
   - Перегрузить оператор \* (**mul**) для умножения двух римских чисел.
   - Перегрузить оператор / (**truediv**) для деления двух римских чисел.
4. Создание UML-диаграммы:
   - Разработать UML-диаграмму классов, отражающую структуру класса Roman.
5. Написание файла main.py:
   - Импортировать классы из файла с классами.
   - Продемонстрировать реализацию возможностей классов.

---

### Требования к коду

- Реализовать арифметические операции с римскими числами.
- Преобразование чисел должно быть выполнено с помощью статических методов.
- Предоставить UML-диаграмму классов.
- Предоставить код, демонстрирующий использование классов.

---

#### Исходный код файла roman.py:

```python

class Roman:
    # Класс, представляющий римское число.

    def __init__(self, value: str):
        """
        Инициализирует объект Roman.
        Args: value: Римское число в виде строки.
        """
        self.value = value

    @staticmethod
    def to_decimal(roman: str) -> int:
        """
        Преобразует римское число в десятичное.
       Args:
            roman: Римское число в виде строки.
        Returns:
            Десятичное представление римского числа.
        """
        roman_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        decimal = 0
        prev_value = 0
        for char in reversed(roman):
            value = roman_dict[char]
            if value < prev_value:
                decimal -= value
            else:
                decimal += value
            prev_value = value
        return decimal # Возвращаем десятичное представление

    @staticmethod
    def to_roman(decimal: int) -> str:
        """
        Преобразует десятичное число в римское.
        Args:
            decimal: Десятичное число.
        Returns:
            Римское представление десятичного числа.
        """
        roman_dict = {1: 'I', 4: 'IV', 5: 'V', 9: 'IX', 10: 'X', 40: 'XL', 50: 'L',
                      90: 'XC', 100: 'C', 400: 'CD', 500: 'D', 900: 'CM', 1000: 'M'}
        result = ''
        for value, numeral in sorted(roman_dict.items(), reverse=True):
            while decimal >= value:
                result += numeral
                decimal -= value
        return result # Возвращение римского представления

    def __add__(self, other: 'Roman') -> 'Roman':
        """
        Складывает два римских числа.
        Args:
            other: Другой объект Roman.
        Returns:
            Новый объект Roman, представляющий сумму.
        """
        decimal_sum = Roman.to_decimal(self.value) + Roman.to_decimal(other.value)
        return Roman(Roman.to_roman(decimal_sum)) # Возвращает новый объект Roman, сумму двух предыдущих.

    def __sub__(self, other: 'Roman') -> 'Roman':
        """
        Вычитает одно римское число из другого.
        Args:
            other: Другой объект Roman.
        Returns:
            Новый объект Roman, представляющий разность.
        """
        decimal_diff = Roman.to_decimal(self.value) - Roman.to_decimal(other.value)
        return Roman(Roman.to_roman(decimal_diff)) # Возвращает новый объект Roman, разность двух предыдущих.

    def __mul__(self, other: 'Roman') -> 'Roman':
        """
        Умножает два римских числа.
        Args:
            other: Другой объект Roman.
        Returns:
            Новый объект Roman, представляющий произведение.
        """
        decimal_product = Roman.to_decimal(self.value) * Roman.to_decimal(other.value)
        return Roman(Roman.to_roman(decimal_product)) # Возвращает новый объект Roman, произведение двух предыдущих.

    def __truediv__(self, other: 'Roman') -> 'Roman':
        """
        Делит одно римское число на другое.
        Args:
            other: Другой объект Roman.
        Returns:
            Новый объект Roman, представляющий частное.
        """
        decimal_quotient = Roman.to_decimal(self.value) // Roman.to_decimal(other.value)
        return Roman(Roman.to_roman(decimal_quotient)) # Возвращает новый объект Roman, частное двух предыдущих.


class AdvancedRoman(Roman):
    # Класс, представляющий расширенное римское число.

    def __init__(self, value: str, color: str):
        """
        Инициализирует объект AdvancedRoman.
        Args:
            value: Римское число в виде строки.
            color: Цвет римского числа.
        """
        super().__init__(value)
        self.color = color

    def get_color(self) -> str:
        """
        Возвращает цвет римского числа.
        Returns:
            Цвет римского числа.
        """
        return self.color # Возвращает условную характеристику, цвет
```

---

#### Исходный код файла main.py:

```python

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
```

---

#### UML-диаграмма классов

![UML-диаграмма классов](https://sun9-53.userapi.com/impg/-1v1pSLYDenoXcRutlybnbKHZXkzhuV8-nOvkw/OCOd7Z6nQww.jpg?size=802x529&quality=95&sign=449949067565af39cb4b0d3e18c38add&type=album)

---
