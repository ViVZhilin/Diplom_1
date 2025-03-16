import pytest
from Diplom_1.burger import Burger
from Diplom_1.bun import Bun
from Diplom_1.ingredient import Ingredient
from Diplom_1.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING


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


def test_set_buns(burger, bun):
    burger.set_buns(bun)
    assert burger.bun == bun


def test_add_ingredient(burger, ingredient_sauce):
    burger.add_ingredient(ingredient_sauce)
    assert len(burger.ingredients) == 1
    assert burger.ingredients[0] == ingredient_sauce


def test_remove_ingredient(burger, ingredient_sauce, ingredient_filling):
    burger.add_ingredient(ingredient_sauce)
    burger.add_ingredient(ingredient_filling)
    burger.remove_ingredient(0)
    assert len(burger.ingredients) == 1
    assert burger.ingredients[0] == ingredient_filling


def test_move_ingredient(burger, ingredient_sauce, ingredient_filling):
    burger.add_ingredient(ingredient_sauce)
    burger.add_ingredient(ingredient_filling)
    burger.move_ingredient(0, 1)
    assert burger.ingredients[0] == ingredient_filling
    assert burger.ingredients[1] == ingredient_sauce


def test_get_price(burger, bun, ingredient_sauce, ingredient_filling):
    burger.set_buns(bun)
    burger.add_ingredient(ingredient_sauce)
    burger.add_ingredient(ingredient_filling)
    assert burger.get_price() == 400  # 100 * 2 (булочки) + 100 (соус) + 200 (начинка)


def test_get_receipt(burger, bun, ingredient_sauce, ingredient_filling):
    burger.set_buns(bun)
    burger.add_ingredient(ingredient_sauce)
    burger.add_ingredient(ingredient_filling)
    receipt = burger.get_receipt()
    assert "(==== black bun ====)" in receipt
    assert "= sauce hot sauce =" in receipt
    assert "= filling cutlet =" in receipt
    assert "Price: 400" in receipt