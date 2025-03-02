from abc import ABC
import csv


class InstantiateCSVError(Exception):
    def __init__(self, message):
        self.message = message


class Item(ABC):
    """
    Класс для представления товара в магазине.
    """
    pay_rate = 1.0
    all = []
    filename = '../src/items.csv'

    def __init__(self, name: str, price: float, quantity: int) -> None:
        """
        Создание экземпляра класса item.

        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        """
        self.__name = name
        self.price = price
        self.quantity = quantity
        super().__init__()

    def __repr__(self):
        name = "'" + self.__name + "'"
        return f"{self.__class__.__name__}({name}, {self.price}, {self.quantity})"

    def __str__(self):
        return f"{self.__name}"

    def __add__(self, other):
        """
        Сложение по количеству товара в магазине
        """
        if isinstance(other, self.__class__):
            return self.quantity + other.quantity
        return None

    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.

        :return: Общая стоимость товара.
        """
        return self.price * self.quantity

    def apply_discount(self) -> None:
        """
        Применяет установленную скидку для конкретного товара.
        """
        self.price *= self.pay_rate

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name_string):
        if len(name_string) <= 10:
            self.__name = name_string
        else:
            self.__name = name_string[:10]

    @classmethod
    def instantiate_from_csv(cls, file=filename):
        """
        класс-метод, инициализирующий экземпляры класса Item данными из файла src/items.csv
        """
        try:
            with open(file, newline='', encoding='windows-1251') as csvfile:
                reader = csv.DictReader(csvfile)
                for row in reader:
                    Item.all.append(cls(row['name'], row['price'], row['quantity']))
        except KeyError:
            raise InstantiateCSVError('Файл item.csv поврежден')
        except FileNotFoundError:
            raise FileNotFoundError('Отсутствует файл item.csv')

    @staticmethod
    def string_to_number(string):
        """
        Статический метод, возвращающий число из числа - строки
        """
        if string.isdigit():
            return int(string)
        else:
            return int(float(string))





