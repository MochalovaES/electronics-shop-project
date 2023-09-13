from src.item import Item


class Mixin:
    def __init__(self):
        self.__language = 'EN'

    @property
    def language(self):
        return self.__language

    def change_lang(self):
        if self.__language == 'EN':
            self.__language = 'RU'
        else:
            self.__language = 'EN'
        return self


class Keyboard(Item, Mixin):
    def __init__(self, name: str, price: float, quantity: int, language='EN'):
        super().__init__(name, price, quantity)
        self.__language = language



