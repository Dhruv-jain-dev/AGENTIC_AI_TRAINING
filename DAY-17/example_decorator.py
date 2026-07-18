class Burger:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def show(self):
        print('{name} | ₹{price}'.format_map(vars(self)))


class MealDecorator:
    def __init__(self, burger):
        self.burger = burger
        self.burger.price += 100   

    def show(self):
        self.burger.show()
        print("Burger upgraded to Meal with Fries and Coke")



burger1 = Burger(name="Mc Veggie", price=150)

print("Before Upgrade:")
burger1.show()

print("\nAfter Upgrade:")
meal = MealDecorator(burger1)
meal.show()
