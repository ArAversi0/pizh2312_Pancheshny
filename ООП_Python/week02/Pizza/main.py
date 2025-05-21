from typing import List
from pizza import Pizza, Order, PepperoniPizza, BarbecuePizza, SeafoodPizza, Terminal

def main():
    terminal = Terminal()  # Создаем экземпляр терминала

    # Демонстрация прямого использования класса Pizza
    custom_pizza = Pizza(
        name="Моя пицца",
        dough="Толстое тесто",
        sauce="Кетчуп",
        toppings=["Грибы", "Оливки", "Томаты"],
        price=15.50,
    )

    print("Демонстрация приготовления пользовательской пиццы:")
    custom_pizza.prepare()
    custom_pizza.bake()
    custom_pizza.cut()
    custom_pizza.pack()
    print("Пользовательская пицца готова!\n")

    while terminal.display_menu:
        terminal.show_menu()  # Отображаем меню
        terminal.order = Order()  # Создаем новый заказ

        while True:
            command = input("Введите номер пиццы (или 'заказ' для подтверждения, 'отмена' для отмены): ")
            terminal.process_command(command)  # Обрабатываем команду пользователя

            if command.lower() == "заказ" or command.lower() == "отмена":
                break  # Выходим из цикла, если заказ подтвержден или отменен

        if command.lower() == "отмена":
            continue  # Переходим к следующему заказу, если предыдущий отменен

        terminal.accept_payment()  # Выполняем заказ

        break  # Выходим из цикла, если заказ подтвержден

if __name__ == "__main__":
    main()