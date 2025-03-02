from menu import MENU, resources

profit = 0
should_continue = True

while should_continue:
    # TODO: 1. Input Coffee Type
    coffee_type = input("What would you like? (espresso/latte/cappuccino): ").lower()

    # TODO: 2. Off
    if coffee_type == "off":
        should_continue = False
        continue

    # TODO: 3. Report
    elif coffee_type == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${profit}")
        continue

    # TODO: 4. Check Resources
    menu = MENU[coffee_type]
    is_enough = True
    for each_ingredients in resources:
        if resources[each_ingredients] < menu["ingredients"][each_ingredients]:
            print(f"Sorry there is not enough {each_ingredients}")
            is_enough = False
            break

    # TODO: 5. Process Coins
    if is_enough:
        print("Please insert coins.")
        total = int(input("how many quarters?: ")) * 0.25
        total += int(input("how many dimes?: ")) * 0.1
        total += int(input("how many nickles?: ")) *  0.05
        total += int(input("how many pennies?: ")) * 0.01

        # TODO: 6. Transaction
        if total < menu["cost"]:
            print("Sorry that's not enough money. Money refunded.")
            continue
        for each_ingredients in resources:
            resources[each_ingredients] -= menu["ingredients"][each_ingredients]
        profit += menu["cost"]
        change = round(total - menu["cost"], 2)
        print(f"Here is ${change} dollars in change.")

        # TODO: 7. Make Coffee
        print(f"Here is your {coffee_type} ☕. Enjoy!")
