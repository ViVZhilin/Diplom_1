import pytest
from Diplom_1.database import Database
from Diplom_1.bun import Bun
from Diplom_1.ingredient import Ingredient
from Diplom_1.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING


@pytest.fixture
def database():
    return Database()


def test_available_buns(database):
    buns = database.available_buns()
    assert len(buns) == 3
    assert isinstance(buns[0], Bun)
    assert buns[0].get_name() == "black bun"
    assert buns[0].get_price() == 100


def test_available_ingredients(database):
    ingredients = database.available_ingredients()
    assert len(ingredients) == 6
    assert isinstance(ingredients[0], Ingredient)
    assert ingredients[0].get_type() == INGREDIENT_TYPE_SAUCE
    assert ingredients[0].get_name() == "hot sauce"
    assert ingredients[0].get_price() == 100