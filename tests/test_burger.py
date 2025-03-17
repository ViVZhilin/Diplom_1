import pytest


class TestBurger:

    def test_set_buns(self, burger, bun):
        burger.set_buns(bun)
        assert burger.bun == bun

    def test_add_ingredient_length(self, burger, ingredient_sauce):
        burger.add_ingredient(ingredient_sauce)
        assert len(burger.ingredients) == 1

    def test_add_ingredient_content(self, burger, ingredient_sauce):
        burger.add_ingredient(ingredient_sauce)
        assert burger.ingredients[0] == ingredient_sauce

    def test_remove_ingredient_length(self, burger, ingredient_sauce, ingredient_filling):
        burger.add_ingredient(ingredient_sauce)
        burger.add_ingredient(ingredient_filling)
        burger.remove_ingredient(0)
        assert len(burger.ingredients) == 1

    def test_remove_ingredient_content(self, burger, ingredient_sauce, ingredient_filling):
        burger.add_ingredient(ingredient_sauce)
        burger.add_ingredient(ingredient_filling)
        burger.remove_ingredient(0)
        assert burger.ingredients[0] == ingredient_filling

    def test_move_ingredient_first_position(self, burger, ingredient_sauce, ingredient_filling):
        burger.add_ingredient(ingredient_sauce)
        burger.add_ingredient(ingredient_filling)
        burger.move_ingredient(0, 1)
        assert burger.ingredients[0] == ingredient_filling

    def test_move_ingredient_second_position(self, burger, ingredient_sauce, ingredient_filling):
        burger.add_ingredient(ingredient_sauce)
        burger.add_ingredient(ingredient_filling)
        burger.move_ingredient(0, 1)
        assert burger.ingredients[1] == ingredient_sauce

    def test_get_price(self, burger, bun, ingredient_sauce, ingredient_filling):
        burger.set_buns(bun)
        burger.add_ingredient(ingredient_sauce)
        burger.add_ingredient(ingredient_filling)
        assert burger.get_price() == 400  # 100 * 2 (булочки) + 100 (соус) + 200 (начинка)

    def test_get_receipt(self, burger, bun, ingredient_sauce, ingredient_filling):
        burger.set_buns(bun)
        burger.add_ingredient(ingredient_sauce)
        burger.add_ingredient(ingredient_filling)
        receipt = burger.get_receipt()
        expected_receipt = (
            "(==== black bun ====)\n"
            "= sauce hot sauce =\n"
            "= filling cutlet =\n"
            "(==== black bun ====)\n\n"
            "Price: 400"
        )
        assert receipt == expected_receipt