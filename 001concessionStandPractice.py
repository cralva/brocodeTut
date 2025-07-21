menu = {"pizza": 3.00,
        "nachos": 4.50,
        "popcorn": 6.00,
        "fries": 2.50,
        "chips": 1.00,
        "pretzel": 3.50,
        "soda": 3.00,
        "lemonade": 4.25}

order = []

total = 0

print("-------- MENU --------")

for key, value in menu.items():
    print(f"{key:10}: ${value:.2f}")

print("----------------------")

while True:
    food = input("Enter the food you wish to enter (q to quit): ").lower()
    if food == "q":
        break
    elif menu.get(food) is not None:
        order.append(food)

for food in order:
    print(food)