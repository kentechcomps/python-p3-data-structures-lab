spiciest_foods = [
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
    names = [food["name"] for food in spicy_foods]
    return names
    

def get_spiciest_foods(spicy_foods):
     spiciest_foods = [food for food in spicy_foods if food["heat_level"] > 5]
     return spiciest_foods
 

def print_spicy_foods(spiciest_foods):
        for food in spiciest_foods:
         heat_level_emojis = "🌶" * food["heat_level"]
         print(f"{food['name']} ({food['cuisine']}) | Heat Level: {heat_level_emojis}")


def get_spicy_food_by_cuisine(spiciest_foods, cuisine):
     for food in spiciest_foods:
        if food["cuisine"] == cuisine:
            return food
     return None

def print_spiciest_foods(spiciest_foods):
      spiciest_foods = get_spiciest_foods(spiciest_foods)
      for food in spiciest_foods:
        heat_level_emojis = "🌶" * food["heat_level"]
        print(f"{food['name']} ({food['cuisine']}) | Heat Level: {heat_level_emojis}")


def get_average_heat_level(spiciest_foods):
     total_heat = sum(food["heat_level"] for food in spiciest_foods)
     num_foods = len(spiciest_foods)
    
     if num_foods > 0:
        average = total_heat / num_foods
        return int(average)
     else:
        return 0

