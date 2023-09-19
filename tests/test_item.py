"""Здесь надо написать тесты с использованием pytest для модуля item."""
from pathlib import Path

import pytest


from src.item import Item, InstantiateCSVError
from src.phone import Phone

ROOT_PATH = Path(__file__).parent.parent
SRC_PATH = Path.joinpath(ROOT_PATH, 'src')
ITEM_CSV = Path.joinpath(SRC_PATH, 'item.csv')
ITEM_ERROR_CSV = Path.joinpath(SRC_PATH, 'item_error.csv')


def test_calculate_total_price():
    item1 = Item("Смартфон", 10000, 20)
    item2 = Item("Ноутбук", 20000, 5)
    assert item1.calculate_total_price() == 200000
    assert item2.calculate_total_price() == 100000


def test_apply_discount():
    item1 = Item("Смартфон", 10000, 20)
    item2 = Item("Ноутбук", 20000, 5)
    Item.pay_rate = 0.8
    item1.apply_discount()
    assert item1.price == 8000
    assert item2.price == 20000


def test_instantiate_from_csv():
    Item.instantiate_from_csv()
    assert len(Item.all) == 5


def test_test_instantiate_from_csv_error():
    with pytest.raises(FileNotFoundError):
        item1 = Item("Смартфон", 10000, 20)
        item1.instantiate_from_csv('bad_path')

    with pytest.raises(InstantiateCSVError):
        item2 = Item("Ноутбук", 20000, 5)
        item2.instantiate_from_csv(ITEM_ERROR_CSV)


def test_string_to_number():
    assert Item.string_to_number('5') == 5
    assert Item.string_to_number('5.0') == 5
    assert Item.string_to_number('5.5') == 5


def test__repr__():
    item1 = Item("Смартфон", 10000, 20)
    item2 = Item("Ноутбук", 100000, 3)
    assert repr(item1) == "Item('Смартфон', 10000, 20)"
    assert repr(item2) == "Item('Ноутбук', 100000, 3)"


def test__str__():
    item1 = Item("Смартфон", 10000, 20)
    item2 = Item("Ноутбук", 100000, 3)
    assert str(item1) == 'Смартфон'
    assert str(item2) == 'Ноутбук'


def test__add__():
    item1 = Item("Смартфон", 10000, 20)
    item2 = Item("Ноутбук", 100000, 3)
    phone1 = Phone("iPhone 14", 120_000, 5, 2)
    phone2 = Phone("iPhone 10", 100_000, 7, 2)
    assert item1 + phone1 == 25
    assert phone1 + phone1 == 10
    assert item1 + item1 == 40
    assert item1 + item2 == 23
    assert item1 + phone2 == 27
    assert phone1 + phone2 == 12
    assert item2 + phone2 == 10
