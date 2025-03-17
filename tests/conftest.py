import pytest
from Diplom_1.bun import Bun
from Diplom_1.burger import Burger
from Diplom_1.ingredient import Ingredient
from Diplom_1.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING
from Diplom_1.database import Database


@pytest.fixture
def burger():
    return Burger()

@pytest.fixture
def bun():
    return Bun("black bun", 100)

@pytest.fixture
def ingredient_sauce():
    return Ingredient(INGREDIENT_TYPE_SAUCE, "hot sauce", 100)

@pytest.fixture
def ingredient_filling():
    return Ingredient(INGREDIENT_TYPE_FILLING, "cutlet", 100)

@pytest.fixture
def database():
    return Database()