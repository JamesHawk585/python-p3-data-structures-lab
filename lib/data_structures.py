

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
    for food in spicy_foods:
        if food['cuisine'] == cuisine:
            return food
    return None


    
def print_spiciest_foods(spicy_foods):
    for food in spicy_foods:
        if food['heat_level'] > 5:
            name = food["name"]
            cuisine = food["cuisine"]
            heat_level = food['heat_level']
            heat_level_emoji = "🌶" * heat_level
            print(f"{name} ({cuisine}) | Heat Level: {heat_level_emoji}")
    
 


def get_average_heat_level(spicy_foods):
    # Creates and empty list
    heat_level = []
    # Creates for loop that loops through the spicy_foods list of dictionaries. 
    for food in spicy_foods:
        # Each time the for loop iterates through the spicy_foods list of dictionaries, the 'heat_level' key is appended to the existing empty heat_level list. 
        heat_level.append(food['heat_level'])
    average = sum(heat_level) / len(heat_level)
    return average 
    

        


def create_spicy_food(spicy_foods, spicy_food):
    pass
