from typing import List

class Pizza:
    # Базовый класс для пиццы

    def __init__(self, name: str, dough: str, sauce: str, toppings: List[str], price: float):
        """
        Инициализирует объект Pizza.
        Args:
            name: Название пиццы.
            dough: Тесто.
            sauce: Соус.
            toppings: Список начинок.
            price: Цена пиццы.
        """
        self.name = name
        self.dough = dough
        self.sauce = sauce
        self.toppings = toppings
        self.price = price

    def prepare(self) -> None:
        # "Готовит пиццу"
        
        print(f"Готовим пиццу {self.name}...") # Вывод поля name
        print(f"Замешиваем тесто: {self.dough}") # Вывод поля dough
        print(f"Добавляем соус: {self.sauce}") # Вывод поля sauce
        print(f"Добавляем начинки: {', '.join(self.toppings)}") # Вывод списка начинок

    def bake(self) -> None:
        # "Выпекает пиццу"
        
        print(f"Выпекаем пиццу {self.name}...") # Вывод поля name

    def cut(self) -> None:
        # "Режет пиццу.""

        print(f"Режем пиццу {self.name}...") # Вывод поля name

    def pack(self) -> None:
        # "Упаковывает пиццу"
        
        print(f"Упаковываем пиццу {self.name}...") # Вывод поля name


class PepperoniPizza(Pizza):
    # Класс для пиццы Пепперони.

    def __init__(self):
        super().__init__(
            name="Пепперони",
            dough="Тонкое тесто",
            sauce="Томатный соус",
            toppings=["Пепперони", "Сыр моцарелла"],
            price=10.99,
        )

class BarbecuePizza(Pizza):
    # Класс для пиццы Барбекю.
    
    def __init__(self):
        super().__init__(
            name="Барбекю",
            dough="Пышное тесто",
            sauce="Соус барбекю",
            toppings=["Курица", "Бекон", "Лук", "Сыр чеддер"],
            price=12.99,
        )

class SeafoodPizza(Pizza):
    # Класс для пиццы Дары Моря.

    def __init__(self):
        super().__init__(
            name="Дары Моря",
            dough="Тонкое тесто",
            sauce="Сливочный соус",
            toppings=["Креветки", "Кальмары", "Мидии", "Сыр пармезан"],
            price=14.99,
        )

class Order:
    # Класс для заказа.

    order_count = 0  # Счетчик заказов

    def __init__(self):
        Order.order_count += 1
        self.order_id = Order.order_count
        self.pizzas: List[Pizza] = []

    def add_pizza(self, pizza: Pizza) -> None:
        """
        Добавляет пиццу в заказ.
        Args:
            pizza: Объект Pizza.
        """
        self.pizzas.append(pizza)

    def calculate_total_price(self) -> float:
        """
        Вычисляет общую стоимость заказа.
        Returns:
            Общая стоимость заказа.
        """
        return sum(pizza.price for pizza in self.pizzas) # возвращает стоимость заказа

    def execute(self) -> None:
        # Выполняет заказ.
        
        print(f"Выполняем заказ №{self.order_id}...") # вывод поля id заказа
        for pizza in self.pizzas:
            pizza.prepare()
            pizza.bake()
            pizza.cut()
            pizza.pack()
        print(f"Заказ №{self.order_id} готов!") # вывод о готовности заказа 

class Terminal:
    # Класс для терминала пиццерии.

    def __init__(self):
        self.menu: List[Pizza] = [PepperoniPizza(), BarbecuePizza(), SeafoodPizza()]
        self.order: Order = None
        self.display_menu = True

    def show_menu(self) -> None:
        # Отображает меню на экране.

        print("Меню:") # вывод
        for i, pizza in enumerate(self.menu):
            print(f"{i + 1}. {pizza.name} - {pizza.price:.2f} руб.") # вывод стоимости каждого пункта меню

    def handle_menu_item(self, choice: int) -> None:
        """
        Обрабатывает выбор пункта меню.
        Args:
            choice: Номер выбранного пункта меню.
        """
        if 1 <= choice <= len(self.menu):
            pizza = self.menu[choice - 1]
            self.order.add_pizza(pizza)
            print(f"Добавлена пицца: {pizza.name}") # Вывод о добавлении пиццы
        else:
            print("Некорректный выбор.") # вывод о некорректности выбора

    def process_command(self, command: str) -> None:
        """
        Обрабатывает команду пользователя.
        Args:
            command: Команда пользователя.
        """
        if command.isdigit():
            self.handle_menu_item(int(command))
        elif command.lower() == "заказ":
            if self.order and self.order.pizzas:
                self.display_order_summary()
                self.accept_payment()
                self.order.execute()
                self.order = None
            else:
                print("Заказ пуст.") # Вывод об отсутствии заказа
        elif command.lower() == "отмена":
            self.order = None
            print("Заказ отменен.") # Отмена заказа
        else:
            print("Неизвестная команда.") # предупреждение об неккоректности команды

    def display_order_summary(self) -> None:
        # Отображает информацию о заказе.

        print("Ваш заказ:") # вывод
        for pizza in self.order.pizzas:
            print(f"- {pizza.name} - {pizza.price:.2f} руб.")
        print(f"Итого: {self.order.calculate_total_price():.2f} руб.") # Подсчитывание стоимости заказа

    def accept_payment(self) -> None:
        # Принимает оплату.

        print("Оплата принята.") # вывод о принятии оплаты