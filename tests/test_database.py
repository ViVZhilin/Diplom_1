from Diplom_1.bun import Bun
from Diplom_1.ingredient import Ingredient
from Diplom_1.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING


class TestDatabase:
    def test_available_buns_length(self, database):
        buns = database.available_buns()
        assert len(buns) == 3

    def test_available_buns_first_item(self, database):
        buns = database.available_buns()
        assert isinstance(buns[0], Bun)

    def test_available_buns_first_item_name(self, database):
        buns = database.available_buns()
        assert buns[0].get_name() == "black bun"

    def test_available_buns_first_item_price(self, database):
        buns = database.available_buns()
        assert buns[0].get_price() == 100

    def test_available_ingredients_length(self, database):
        ingredients = database.available_ingredients()
        assert len(ingredients) == 6

    def test_available_ingredients_first_item(self, database):
        ingredients = database.available_ingredients()
        assert isinstance(ingredients[0], Ingredient)

    def test_available_ingredients_first_item_type(self, database):
        ingredients = database.available_ingredients()
        assert ingredients[0].get_type() == INGREDIENT_TYPE_SAUCE

    def test_available_ingredients_first_item_name(self, database):
        ingredients = database.available_ingredients()
        assert ingredients[0].get_name() == "hot sauce"

    def test_available_ingredients_first_item_price(self, database):
        ingredients = database.available_ingredients()
        assert ingredients[0].get_price() == 100