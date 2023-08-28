import csv


class Item:
    """
    Класс для представления товара в магазине.
    """
    pay_rate = 1.0
    all = []

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
    def instantiate_from_csv(cls):
        """
        класс-метод, инициализирующий экземпляры класса Item данными из файла src/items.csv
        """
        with open('../src/items.csv', newline='', encoding='windows-1251') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                Item.all.append(cls(row['name'], row['price'], row['quantity']))

    @staticmethod
    def string_to_number(string):
        """
        Статический метод, возвращающий число из числа - строки
        """
        if string.isdigit():
            return int(string)
        else:
            return int(string.split('.')[0])
