# Программирование на языке высокого уровня (Python).
# Задание №6. Вариант - 4
#
# Выполнил: Панчешный Александр Алексеевич
# Группа: ПИЖ-б-о-23-1-2
# E-mail: pancheshny2020@yandex.ru

from classes import PostalTransfer, BankTransfer, CurrencyTransfer

if __name__ == "__main__":
    # Демонстрация работы PostalTransfer
    postal_transfer = PostalTransfer(
        sender="Иван Иванов",
        recipient="Александр Панчешный",
        amount=100.0,
        postal_address="ул. Тухачевского, 27"
    )
    print("Почтовый перевод:")
    postal_transfer.execute()
    print(f"ID перевода: {postal_transfer.get_transfer_id()}")
    print(f"Отправитель: {postal_transfer.sender}")
    print(f"Получатель: {postal_transfer.recipient}")
    print(f"Сумма: {postal_transfer.amount}")
    print("-" * 20)

    # Демонстрация работы BankTransfer
    bank_transfer = BankTransfer(
        sender="Александр Панчешный",
        recipient="Иван Иванов",
        amount=500.0,
        bank_account="1234567890"
    )
    print("Банковский перевод:")
    bank_transfer.execute()
    print(f"ID перевода: {bank_transfer.get_transfer_id()}")
    print(f"Отправитель: {bank_transfer.sender}")
    print(f"Получатель: {bank_transfer.recipient}")
    print(f"Сумма: {bank_transfer.amount}")
    print(f"Счет: {bank_transfer.bank_account}")
    print("-" * 20)

    # Демонстрация работы CurrencyTransfer
    currency_transfer = CurrencyTransfer(
        sender="Панчешный Александр",
        recipient="Пётр Петров",
        amount=200.0,
        currency="USD",
        exchange_rate=90.0
    )
    print("Валютный перевод:")
    currency_transfer.execute()
    print(f"ID перевода: {currency_transfer.get_transfer_id()}")
    print(f"Отправитель: {currency_transfer.sender}")
    print(f"Получатель: {currency_transfer.recipient}")
    print(f"Сумма: {currency_transfer.amount}")
    print("-" * 20)