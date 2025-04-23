# Проект "Денежные переводы"

---

## Описание

Данный проект представляет собой реализацию иерархии классов для денежных переводов различных типов (почтовый, банковский, валютный). Проект включает в себя создание базового класса MoneyTransfer с абстрактным методом execute() и подклассов, реализующих конкретные типы переводов.

---

## Задачи

- Создание базового класса MoneyTransfer:

  1. Создать абстрактный базовый класс MoneyTransfer с методом execute(), который должен быть реализован в подклассах.
  1. Реализовать общие поля и методы для всех типов переводов (например, отправитель, получатель, сумма).
  1. Реализовать необходимые поля для функционирования базовых методов.
  1. Реализовать минимум по одному общедоступному, не общедоступному и закрытому полю/методу.
  1. Реализовать вывод на экран работы метода (например, сообщение о выполнении перевода).

- Создание подклассов PostalTransfer, BankTransfer, CurrencyTransfer:

  1. Создать подклассы PostalTransfer, BankTransfer, CurrencyTransfer, наследующиеся от MoneyTransfer.
  1. Реализовать метод execute() в каждом подклассе, специфичный для конкретного типа перевода.
  1. Добавить собственные методы в классы иерархии (по желанию).
  1. Предусмотреть необходимые параметры для базовых методов.
  1. Реализовать необходимые поля для функционирования базовых методов.
  1. Реализовать минимум по одному общедоступному, не общедоступному и закрытому полю/методу.
  1. Реализовать вывод на экран работы метода (например, сообщение о выполнении перевода).

- Создание модуля classes.py:

  1. Реализовать все классы в отдельном модуле classes.py.

- Создание скрипта main.py:

  1. Создать скрипт main.py, который бы тестировал все возможности классов.
  1. Демонстрировать создание объектов каждого типа перевода и вызов метода execute().
  1. Выводить на экран результаты работы методов.

- Построение UML-диаграммы:
  1. Построить UML-диаграмму классов приложения, отражающую структуру классов и их взаимосвязи.

---

### Исходный код модуля classe.py

```python

from abc import ABC, abstractmethod
from typing import Optional

class MoneyTransfer(ABC):
    """
    Абстрактный базовый класс для денежных переводов.
    """

    def __init__(self, sender: str, recipient: str, amount: float) -> None:
        """
        Инициализация объекта денежного перевода.

        Args:
            sender: Отправитель перевода.
            recipient: Получатель перевода.
            amount: Сумма перевода.
        """
        self._sender: str = sender
        self._recipient: str = recipient
        self._amount: float = amount
        self._transfer_id: int = self._generate_transfer_id()  # Закрытое поле

    @property
    def sender(self) -> str:
        """Получить отправителя."""
        return self._sender  # Возвращает строку - имя отправителя

    @property
    def recipient(self) -> str:
        """Получить получателя."""
        return self._recipient  # Возвращает строку - имя получателя

    @property
    def amount(self) -> float:
        """Получить сумму перевода."""
        return self._amount  # Возвращает число (float) - сумму перевода

    @abstractmethod
    def execute(self) -> None:
        """Абстрактный метод для выполнения перевода."""
        pass

    def _generate_transfer_id(self) -> int:
        """Генерация идентификатора перевода (закрытый метод)."""
        # Здесь должна быть логика генерации уникального ID
        return hash(f"{self._sender}{self._recipient}{self._amount}")  # Возвращает число (int) - хеш как идентификатор

    def get_transfer_id(self) -> int:
        """Получить идентификатор перевода (общедоступный метод)."""
        return self._transfer_id  # Возвращает число (int) - идентификатор перевода

class PostalTransfer(MoneyTransfer):
    """Класс для почтовых переводов."""

    def __init__(self, sender: str, recipient: str, amount: float, postal_address: str) -> None:
        super().__init__(sender, recipient, amount)
        self._postal_address: str = postal_address  # Не общедоступное поле

    def execute(self) -> None:
        """Выполнение почтового перевода."""
        print(f"Выполняется почтовый перевод от {self.sender} к {self.recipient} на сумму {self.amount}")
        print(f"Адрес доставки: {self._postal_address}")

class BankTransfer(MoneyTransfer):
    """Класс для банковских переводов."""

    def __init__(self, sender: str, recipient: str, amount: float, bank_account: str) -> None:
        super().__init__(sender, recipient, amount)
        self.bank_account: str = bank_account  # Общедоступное поле

    def execute(self) -> None:
        """Выполнение банковского перевода."""
        print(f"Выполняется банковский перевод от {self.sender} к {self.recipient} на сумму {self.amount}")
        print(f"Номер счета: {self.bank_account}")

class CurrencyTransfer(MoneyTransfer):
    """Класс для валютных переводов."""

    def __init__(self, sender: str, recipient: str, amount: float, currency: str, exchange_rate: float) -> None:
        super().__init__(sender, recipient, amount)
        self._currency: str = currency  # Не общедоступное поле
        self._exchange_rate: float = exchange_rate  # Не общедоступное поле

    def execute(self) -> None:
        """Выполнение валютного перевода."""
        converted_amount = self.amount * self._exchange_rate
        print(f"Выполняется валютный перевод от {self.sender} к {self.recipient} на сумму {self.amount} {self._currency} ({converted_amount} в основной валюте)")
        print(f"Курс обмена: {self._exchange_rate}")
```

### Исходный код файла main.py

```python

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
```

---

### UML-диаграмма классов

![UML-диаграмма](https://sun9-55.userapi.com/impg/ENMZYPqi0UIkEIwsp0yZbk9xXi1UjX34CqFOcA/0FZ-hbazs8Y.jpg?size=884x732&quality=95&sign=483a167ebd81af9272a21c6d39739af0&type=album)
