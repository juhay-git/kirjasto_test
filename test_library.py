import pytest
from library import Library

def test_add_book():
    lib = Library()
    lib.add_book("Jee jee", "M.Syrjä")
    lib.add_book("laskdjf", "qweqwe")
    assert len(lib.books) == 2

def test_remove_book():
    lib = Library()
    lib.add_book("Jee jee", "M.Syrjä")
    lib.add_book("laskdjf", "qweqwe")
    lib.remove_book("Jee jee")
    assert len(lib.books) == 1
    assert "Jee jee" not in lib.books