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
    def __init__(self, name, color, milk_production, weight, hunger):
        super().__init__(name, color, weight, hunger)
        self.milk_production = milk_production


class Goat(Animal):
    def __init__(self, name, color, milk_production, weight, hunger):
        super().__init__(name, color, weight, hunger)
        self.milk_production = milk_production


class Pig(Animal):
    def __init__(self, name, color,  weight, hunger):
        super().__init__(name, color, weight, hunger)


class Duck(Animal):
    def __init__(self, name, color,  isabird, weight, hunger):
        super().__init__(name, color, weight, hunger)
        self.isabird = isabird


class Chicken(Animal):
    def __init__(self, name, color,  isabird, eggs_produciton, weight, hunger):
        super().__init__(name, color, weight, hunger)
        self.isabird = isabird
        self.eggs_production = eggs_produciton


class Goose(Animal):
    def __init__(self, name, color,  isabird, weight, hunger):
        super().__init__(name, color, weight, hunger)
        self.isabird = isabird

cow = Cow('Dusyua', 'White', 10, 750, 100)
print(cow.color)

goat = Goat('Goat', 'Grey', 5, 50, 70)
print(goat.hunger)

pig = Pig('Borya', 'Pink', 300, 30)
print(pig.name)

duck = Duck('Duck', 'Grey', True, 15, 35)
print(duck.isabird)

chicken = Chicken('Ryaba', 'Orange', True, 2, 5, 45)
print(chicken.eggs_production)

goose = Goose('Goose', 'Color', True, 7, 15)
print(goose.weight)
