class Animal:
    def __init__(self, name, color, weight, hunger):
        self.name = name
        self.color = color
        self.weight = weight
        self.hunger = hunger

    def eat(self):
        self.hunger -= 10
        return self.hunger


class Cow(Animal):
    def __init__(self, name, color, weight, hunger, milk_production):
        super().__init__(name, color, weight, hunger)
        self.milk_production = milk_production


class Goat(Animal):
    def __init__(self, name, color, milk_production, weight, hunger):
        super().__init__(name, color, weight, hunger)
        self.milk_production = milk_production


class Pig(Animal):
    pass


class Bird(Animal):
    isabird = True


class Duck(Bird):
    pass


class Chicken(Bird):
    def __init__(self, name, color, weight, hunger, eggs_produciton):
        super().__init__(name, color, weight, hunger)
        self.eggs_production = eggs_produciton


class Goose(Bird):
    def __init__(self, name, color,  isabird, weight, hunger):
        super().__init__(name, color, weight, hunger)

cow = Cow('Dusyua', 'White', 750, 100, 10)
print(cow.color)

goat = Goat('Goat', 'Grey', 5, 50, 70)
print(goat.hunger)

pig = Pig('Borya', 'Pink', 300, 30)
print(pig.name)

duck = Duck('Duck', 'Grey', 15, 35)
print(duck.isabird)

chicken = Chicken('Ryaba', 'Orange', 5, 45, 2)
print(chicken.eggs_production)

goose = Goose('Goose', 'Color', True, 7, 15)
print(goose.weight)
