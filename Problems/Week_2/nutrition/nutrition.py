fruits = [

    {"name": "apple" , "calories": "130"},
    {"name": "Avocado", "calories": "50"},
    {"name": "banana", "calories": "110"},
    {"name": "Cantaloupe", "calories": "50"},
    {"name": "grapefruit", "calories": "60"},
    {"name": "grapes", "calories": "90"},
    {"name": "Honeydew Melon", "calories": "50"},
    {"name": "Kiwifruit", "calories": "90"},
    {"name": "lemon", "calories": "15"},
    {"name": "lime", "calories": "20"},
    {"name": "nectarine", "calories": "60"},
    {"name": "orange", "calories": "80"},
    {"name": "peach", "calories": "60"},
    {"name": "pear", "calories": "100"},
    {"name": "pineapple", "calories": "50"},
    {"name": "plums", "calories": "70"},
    {"name": "Strawberries", "calories": "50"},
    {"name": "Sweet Cherries", "calories": "100"},
    {"name": "Tangerine", "calories": "50"},
    {"name": "watermelon", "calories": "80"},

]

name = input("Item: ")

for fruit in fruits:
    if fruit["name"] == name:
        print(f"Calories: {fruit['calories']}")
