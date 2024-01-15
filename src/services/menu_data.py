import csv
from typing import Set
from models.dish import Dish
from models.ingredient import Ingredient

# Req 3
class MenuData:
    def __init__(self, source_path: str) -> dict:
        self.dishes: Set[Dish] = set()
        self.loaded_data = self.load_menu_data(source_path)
        self.create_dishes()

    def load_menu_data(self, source_path: str) -> None:
        try:
            with open(source_path, encoding='utf-8') as file:
                dish_reader = csv.reader(file, delimiter=",", quotechar='"')

                header, *data = dish_reader

            group_by_dish_name = {}
            for row in data:
                dish_name = row[0]
                if dish_name not in group_by_dish_name:
                    group_by_dish_name[dish_name] = {
                        "price": row[1],
                        "ingredients": [{
                            "ingredient_name": row[2],
                            "qty": row[3]}
                        ]}
                else:
                    group_by_dish_name[dish_name]["ingredients"].append({
                        "ingredient_name": row[2],
                        "qty": row[3]
                    })
            return group_by_dish_name
        except FileNotFoundError:
            raise FileNotFoundError("Arquivo CSV não encontrado.")

    def create_dishes(self) -> None:
        for dish_name, dish_data in self.loaded_data.items():
            new_dish = Dish(dish_name, float(dish_data["price"]))
            ingredients = dish_data["ingredients"]
            for ingredient in ingredients:
                new_ingredient = Ingredient(ingredient["ingredient_name"])
                qty = ingredient["qty"]
                new_dish.add_ingredient_dependency(new_ingredient, int(qty))
            self.dishes.add(new_dish)
