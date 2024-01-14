import pytest
from src.models.ingredient import Ingredient, Restriction
from src.models.dish import Dish  # noqa: F401, E261, E501


# Req 2
def test_dish():
    with pytest.raises(TypeError):
        dish1 = Dish("Omelete da Casa", "20.00")

    with pytest.raises(ValueError):
        dish1 = Dish("Omelete da Casa", -20.00)

    dish1 = Dish("Omelete da Casa", 20.00)  # Prato válido

    assert dish1.name == "Omelete da Casa"
    assert dish1.price == 20.00
    assert dish1.recipe == {}

    egg = Ingredient("ovo")
    cheese = Ingredient("queijo mussarela")
    bacon = Ingredient("bacon")
    ham = Ingredient("presunto")
    chicken = Ingredient("frango")
    dish1.add_ingredient_dependency(egg, 5)
    dish1.add_ingredient_dependency(cheese, 2)
    dish1.add_ingredient_dependency(bacon, 1)
    dish1.add_ingredient_dependency(ham, 1)
    dish1.add_ingredient_dependency(chicken, 2)

    assert len(dish1.recipe) == 5
    assert egg in dish1.recipe
    assert dish1.recipe[egg] == 5
    assert bacon in dish1.recipe
    assert dish1.recipe[bacon] == 1

    restrictions = dish1.get_restrictions()

    assert Restriction.ANIMAL_DERIVED in restrictions
    assert Restriction.LACTOSE in restrictions
    assert Restriction.ANIMAL_MEAT in restrictions

    ingredients = dish1.get_ingredients()

    assert egg in ingredients
    assert cheese in ingredients
    assert bacon in ingredients
    assert ham in ingredients
    assert chicken in ingredients

    dish2 = Dish("Omelete Light", 15.00)  # Prato válido
    dish3 = Dish("Omelete da Casa", 20.00)  # Prato válido

    assert dish1 == dish3
    assert dish1 != dish2

    assert hash(dish1) == hash(dish3)
    assert hash(dish1) != hash(dish2)

    assert repr(dish2) == "Dish('Omelete Light', R$15.00)"
