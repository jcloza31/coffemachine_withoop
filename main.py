class CoffeeMachine:

    def __init__(self):
        self.stock = {"water": 400, "money": 550, "milk": 540, "coffee_beans": 120, "disposable_cups": 9}
        self.required_ingredients = {"espresso": {"water": 250, "coffee_beans": 16}, "latte":
            {"water": 350, "milk": 75, "coffee_beans": 20},
                                     "cappuccino": {"water": 200, "milk": 100, "coffee_beans": 12}}
        self.coffee_prices = {"espresso": 4, "latte": 7, "cappuccino": 6}

    def display_inventory(self):
        print("The coffee machine has:")
        print(f"{self.stock['water']} of water")
        print(f"{self.stock['milk']} of milk")
        print(f"{self.stock['coffee_beans']} of coffee beans")
        print(f"{self.stock['disposable_cups']} of disposable cups")
        if self.stock["money"] > 0:
            print(f"${self.stock['money']} of money")
        else:
            print("0 of money")

    def choose_coffee_flavor(self, coffee_flavor):
        if coffee_flavor == 1:
            return "espresso"
        elif coffee_flavor == 2:
            return "latte"
        elif int(coffee_flavor) == 3:
            return "cappuccino"

    def check_ingredients(self, coffee_flavor):
        for ingredient, required_amount in self.required_ingredients[coffee_flavor].items():
            if required_amount > self.stock[ingredient]:
                print(f"Sorry, not enough {ingredient}!")
                return False
        return True

    def buy(self, coffee_flavor):
        self.stock["disposable_cups"] -= 1
        self.stock["money"] += self.coffee_prices[coffee_flavor]
        for ingredient, required_amount in self.required_ingredients[coffee_flavor].items():
            self.stock[ingredient] -= required_amount
        print("I have enough resources, making you a coffee!")

    def fill(self, water, milk, coffee_beans, cups):
        """Restock the ingredients by taking the amount of ingredient as input"""
        self.stock["water"] += water
        self.stock["milk"] += milk
        self.stock["coffee_beans"] += coffee_beans
        self.stock["disposable_cups"] += cups

    def take(self):
        """Withdraw the money"""
        print(f"I gave you ${self.stock['money']}")
        self.stock["money"] = 0

    def show_remaining(self):
        self.display_inventory()

    def machine_menu(self, option):
        if option == "buy":
            user_choice = input("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino:\n")
            if user_choice == "back":
                # The double quotes will act as a filler to continue the machine_menu method loop
                self.machine_menu("")
            else:
                chosen_flavor = self.choose_coffee_flavor(int(user_choice))
                if self.check_ingredients(chosen_flavor):
                    self.buy(chosen_flavor)
        elif option == "fill":
            additional_water = int(input("Write how many ml of water you want to add:\n"))
            additional_milk = int(input("Write how many ml of milk you want to add:\n"))
            additional_coffee_beans = int(input("Write how many grams of coffee beans you want to add:\n"))
            additional_disposable_cups = int(input("Write how many disposable coffee cups you want to add:\n"))
            self.fill(additional_water, additional_milk, additional_coffee_beans, additional_disposable_cups)
        elif option == "take":
            self.take()
        elif option == "remaining":
            self.show_remaining()
        elif option == "exit":
            return False

    def coffee_machine(self):
        """The Coffee Machine Program"""
        self.machine_menu()

    def coffee_machine_is_on(self):
        while self.coffee_machine_is_on:
            self.coffee_machine()


dolce_gusto = CoffeeMachine()
power_is_on = True
while power_is_on:
    user_choice = input("Write action (buy, fill, take, remaining, exit):\n").lower()
    if user_choice == "exit":
        power_is_on = False
    else:
        dolce_gusto.machine_menu(user_choice)

