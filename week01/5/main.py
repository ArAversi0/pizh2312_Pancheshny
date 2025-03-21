class EncapClass:
    """
    Класс с полной инкапсуляцией.  Доступ к атрибутам и изменение данных
    реализуются через вызовы методов (геттеры и сеттеры).
    """

    def __init__(self, initial_value):
        """
        Конструктор класса.

        Аргументы:
            initial_value: Начальное значение для приватного атрибута _my_attribute.
        """
        self._my_attribute = initial_value  # Приватный атрибут, доступ к которому ограничен.

    def getMyAttribute(self):
        """
        Геттер для приватного атрибута _my_attribute.

        Возвращает:
            Значение приватного атрибута _my_attribute.
        """
        return self._my_attribute

    def setMyAttribute(self, new_value):
        """
        Сеттер для приватного атрибута _my_attribute.

        Позволяет изменять значение приватного атрибута _my_attribute.

        Аргументы:
            new_value: Новое значение для атрибута _my_attribute.
        """
        self._my_attribute = new_value

# Пример использования
obj = EncapClass(10)  # Создаем экземпляр класса с начальным значением 10

print(f"Значение атрибута: {obj.getMyAttribute()}")  # Получаем значение атрибута с помощью геттера

obj.setMyAttribute(20)  # Устанавливаем новое значение атрибута с помощью сеттера

print(f"Новое значение атрибута: {obj.getMyAttribute()}")  # Снова получаем значение атрибута с помощью геттера

# Попытка прямого доступа к приватному атрибуту (не рекомендуется)
# print(obj._my_attribute) # Это будет работать, но нарушает принципы инкапсуляции