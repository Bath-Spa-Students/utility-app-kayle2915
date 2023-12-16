items = {
    'drinks': {
        1: {'item': 'heineken', 'price': 8.00},
        2: {'item': 'san mig light', 'price': 7.25},
        3: {'item': 'red horse', 'price': 8.00},
        4: {'item': 'light beer', 'price': 8.00},
        5: {'item': 'hennessy', 'price': 8.00}
    },
    'chips': {
        5: {'item': 'lays', 'price': 1.25},
        6: {'item': 'cheetos', 'price': 1.25},
        7: {'item': 'ding dong', 'price':1.25 }
    }
}

# Ask for user's age
while True:
    try:
        age = int(input("Please enter your age: "))
        break
    except ValueError:
        print("Please enter a valid age.")

if age >= 18:
    print("\nWelcome to vending machine!")
    print("Here are the available items:")

    for category, category_items in items.items():
        print(f"\n{category.capitalize()}:")
        for item_number, item_details in category_items.items():
            print(f"Item {item_number}: {item_details['item'].capitalize()} - Price: {item_details['price']} AED")

    # user money
    while True:
        try:
            money = float(input("\nPlease enter the amount of money you have: "))
            break
        except ValueError:
            print("Please enter a valid amount of money.")

    # selecting items
    selected_items = []
    while True:
        try:
            selected_item_number = int(input("\nEnter the number of the item you want (0 to finish): "))
            if selected_item_number == 0:
                break
            elif selected_item_number in [num for cat in items.values() for num in cat.keys()]:
                selected_items.append(selected_item_number)
            else:
                print("Invalid item number. Please select again.")
        except ValueError:
            print("Please enter a valid item number.")

    total_price = 0
    for selected_item_number in selected_items:
        for category, category_items in items.items():
            if selected_item_number in category_items:
                selected_item = category_items[selected_item_number]['item']
                price = category_items[selected_item_number]['price']
                print(f"\nYou selected {selected_item.capitalize()} - Price: {price} AED")
                total_price += price

    if money >= total_price:
        change = money - total_price
        print(f"\nYour total is: {total_price} AED")
        print(f"You will receive {change} AED in change.")
    else:
        print(f"\nYour total is: {total_price} AED")
        print(f"Sorry, you don't have enough money.")

else:
    print("Sorry, you must be 18 or older to access this vending machine.")