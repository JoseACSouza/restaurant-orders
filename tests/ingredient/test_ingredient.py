from src.models.ingredient import Ingredient, Restriction  # noqa: F401, E261, E501


# Req 1
def test_ingredient():
    ingredient1 = Ingredient('queijo mussarela')
    ingredient2 = Ingredient('carne')
    ingredient3 = Ingredient('queijo mussarela')

    assert ingredient1.name == "queijo mussarela"
    assert ingredient1.restrictions == {
        Restriction.LACTOSE,
        Restriction.ANIMAL_DERIVED
    }

    assert ingredient1 == ingredient3
    assert ingredient1 != ingredient2

    assert hash(ingredient1) == hash(ingredient3)
    assert hash(ingredient1) != hash(ingredient2)

    assert repr(ingredient2) == "Ingredient('carne')"
