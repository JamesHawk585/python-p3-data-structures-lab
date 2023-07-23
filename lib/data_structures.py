spicy_foods = [
    {
        "name": "Green Curry",
        "cuisine": "Thai",
        "heat_level": 9,
    },
    {
        "name": "Buffalo Wings",
        "cuisine": "American",
        "heat_level": 3,
    },
    {
        "name": "Mapo Tofu",
        "cuisine": "Sichuan",
        "heat_level": 6,
    },
]

def get_names(spicy_foods):
    spicy_foods_names = [food['name'] for food in spicy_foods]
    return spicy_foods_names

def get_spiciest_foods(spicy_foods):
    spiciest_foods = [food for food in spicy_foods if food['heat_level'] > 5] 
    return spiciest_foods

def print_spicy_foods(spicy_foods):
    for food in spicy_foods:
        name = food["name"]
        cuisine = food["cuisine"]
        heat_level = food['heat_level']
        heat_level_emoji = "🌶" * heat_level
        print(f"{name} ({cuisine}) | Heat Level: {heat_level_emoji}")

def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    spicy_food_by_cuisine = []
    for food in spicy_foods:
            if food['cuisine'] == cuisine:
                spicy_food_by_cuisine.append(food)
    return spicy_food_by_cuisine

def print_spiciest_foods(spicy_foods):
    pass

def get_average_heat_level(spicy_foods):
    pass

def create_spicy_food(spicy_foods, spicy_food):
    pass
