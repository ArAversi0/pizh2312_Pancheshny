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