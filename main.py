from abc import ABC, abstractmethod

# Component interface
class Coffee(ABC):
    @abstractmethod
    def cost(self):
        pass

    @abstractmethod
    def description(self):
        pass

# Concrete component
class SimpleCoffee(Coffee):
    def cost(self):
        return 1

    def description(self):
        return "Simple coffee"

# Decorator
class CoffeeDecorator(Coffee, ABC):
    def __init__(self, decorated_coffee):
        self.decorated_coffee = decorated_coffee

    @abstractmethod
    def cost(self):
        pass

    @abstractmethod
    def description(self):
        pass

# Concrete decorators
class Milk(CoffeeDecorator):
    def cost(self):
        return self.decorated_coffee.cost() + 0.5

    def description(self):
        return self.decorated_coffee.description() + ", milk"

class Sugar(CoffeeDecorator):
    def cost(self):
        return self.decorated_coffee.cost() + 0.2

    def description(self):
        return self.decorated_coffee.description() + ", sugar"

class Vanilla(CoffeeDecorator):
    def cost(self):
        return self.decorated_coffee.cost() + 0.3

    def description(self):
        return self.decorated_coffee.description() + ", vanilla"

# Client code
def main():
    simple_coffee = SimpleCoffee()
    print(f"{simple_coffee.description()} costs ${simple_coffee.cost()}")

    milk_coffee = Milk(simple_coffee)
    print(f"{milk_coffee.description()} costs ${milk_coffee.cost()}")

    sugar_coffee = Sugar(milk_coffee)
    print(f"{sugar_coffee.description()} costs ${sugar_coffee.cost()}")

    vanilla_coffee = Vanilla(sugar_coffee)
    print(f"{vanilla_coffee.description()} costs ${vanilla_coffee.cost()}")

if __name__ == "__main__":
    main()
