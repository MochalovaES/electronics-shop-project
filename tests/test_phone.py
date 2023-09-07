from src.item import Item
from src.phone import Phone


def test__str__():
    phone1 = Phone("iPhone 14", 120_000, 5, 2)
    phone2 = Phone("iPhone 10", 100_000, 7, 2)
    assert str(phone1) == 'iPhone 14'
    assert str(phone2) == 'iPhone 10'


def test__repr__():
    phone1 = Phone("iPhone 14", 120_000, 5, 2)
    phone2 = Phone("iPhone 10", 100_000, 7, 2)
    assert repr(phone1) == "Phone('iPhone 14', 120000, 5, 2)"
    assert repr(phone2) == "Phone('iPhone 10', 100000, 7, 2)"
