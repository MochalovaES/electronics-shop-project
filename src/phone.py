from src.item import Item


class Phone(Item):

    def __init__(self, name: str, price: float, quantity: int, number_of_sim: float):
        super().__init__(name, price, quantity)
        if number_of_sim <= 0:
            raise ValueError('Количество физических SIM-карт должно быть целым '
                             'числом больше нуля.')
        self.number_of_sim = number_of_sim

    @property
    def number_of_sim(self):
        return self.__number_of_sim

    @number_of_sim.setter
    def number_of_sim(self, value: int):
        if not isinstance(value, int) or value <= 0:
            raise ValueError('Количество физических SIM-карт должно быть целым '
                             'числом больше нуля.')
        self.__number_of_sim = value

    def __repr__(self):
        name = "'" + self.name + "'"
        return f"{self.__class__.__name__}({name}, {self.price}, {self.quantity}, {self.number_of_sim})"