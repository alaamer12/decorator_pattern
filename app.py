# Base coffee interface
class Coffee:
    def cost(self):
        pass

    def description(self):
        pass

# Concrete coffee classes
class SimpleCoffee(Coffee):
    def cost(self):
        return 5

    def description(self):
        return "Simple Coffee"

class MilkCoffee(Coffee):
    def __init__(self, coffee):
        self._coffee = coffee

    def cost(self):
        return self._coffee.cost() + 2

    def description(self):
        return self._coffee.description() + ", Milk"

class SugarCoffee(Coffee):
    def __init__(self, coffee):
        self._coffee = coffee

    def cost(self):
        return self._coffee.cost() + 1

    def description(self):
        return self._coffee.description() + ", Sugar"

class VanillaCoffee(Coffee):
    def __init__(self, coffee):
        self._coffee = coffee

    def cost(self):
        return self._coffee.cost() + 3

    def description(self):
        return self._coffee.description() + ", Vanilla"

if __name__ == "__main__":
    # Creating a simple coffee
    coffee = SimpleCoffee()
    print("Cost:", coffee.cost())
    print("Description:", coffee.description())

    # Adding milk
    coffee_with_milk = MilkCoffee(coffee)
    print("Cost:", coffee_with_milk.cost())
    print("Description:", coffee_with_milk.description())

    # Adding sugar
    coffee_with_sugar = SugarCoffee(coffee)
    print("Cost:", coffee_with_sugar.cost())
    print("Description:", coffee_with_sugar.description())

    # Adding vanilla
    coffee_with_vanilla = VanillaCoffee(coffee)
    print("Cost:", coffee_with_vanilla.cost())
    print("Description:", coffee_with_vanilla.description())

    # Adding milk and sugar
    coffee_with_milk_and_sugar = SugarCoffee(MilkCoffee(coffee))
    print("Cost:", coffee_with_milk_and_sugar.cost())
    print("Description:", coffee_with_milk_and_sugar.description())
