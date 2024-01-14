menu = {
    "Baja Taco": 4.25,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}


x = []
x = list(menu)
price = 0
while True:
    try:
        order = (input("Item: ")).title()
        if order in x:

            price = price + menu[order]
            print(f"${price}")

    except EOFError:
        print("\n")
        break


    except KeyError:
        pass

    except ValueError:
        pass
