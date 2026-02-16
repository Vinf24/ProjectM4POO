""" CLASE COMPRA purchase.py """

from datetime import datetime
from src.exceptions.client_exceptions import InvalidAmountError


class Purchase:
    """ CLASE COMPRA """

    def __init__(self, amount: float, description: str = "", date = None):
        self.amount = amount
        self.description = description
        self.date = date if date else datetime.now().replace(microsecond=0)

    @property
    def amount(self) -> float:
        """ MONTO DE COMPRA """
        return self._amount

    @amount.setter
    def amount(self, value: float) -> None:
        if not isinstance(value, (int, float)):
            raise ValueError("Amount must be a number")

        if value <= 0:
            raise InvalidAmountError("Amount must be greater than zero")

        self._amount = float(value)

    @property
    def date(self):
        """ FECHA DE COMPRA """
        return self._date

    @date.setter
    def date(self, value):
        if isinstance(value, str):
            self._date = datetime.strptime(value, "%Y-%m-%d %H:%M:%S")
        elif isinstance(value, datetime):
            self._date = value
        else:
            raise ValueError("Invalid date format")

    def calculate_total_with_discount(self, client) -> float:
        """ APLICA EL DESCUENTO """
        discount = client.get_discount()
        return self._amount - (self._amount * discount)

    def __str__(self) -> str:
        return (
            f"Purchase(amount={self._amount}, "
            f"description='{self.description}', "
            f"date={self.date.strftime('%Y-%m-%d %H:%M:%S')})"
        )
