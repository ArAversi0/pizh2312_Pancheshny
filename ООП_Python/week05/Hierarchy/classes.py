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