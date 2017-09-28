class Animal:
    name = ''
    isabird = False
    color = ''
    milk_production = 0 #litres in a day
    eggs_production = 0 #pieces in a day
    weight = 0 #kg
    hunger = 0 #percent 0-100


    def eat(self):
        self.hunger -= 10
        return self.hunger


cow = Animal()
cow.name = 'Cow'
cow.color = 'White'
cow.hunger = 100
cow.weight = 750
cow.milk_production = 10

goat = Animal()
goat.name = 'Goat'
goat.color = 'Grey'
goat.milk_production = 5
goat.hunger = 70
goat.weight = 50

pig = Animal()
pig.name = 'Pig'
pig.color = 'Pink'
pig.hunger = 30
pig.weight = 300

duck = Animal()
duck.name = 'Duck'
duck.isabird = True
duck.color = 'Grey'
duck.weight = 15
duck.hunger = 35

chicken = Animal()
chicken.name = 'Chicken'
chicken.isabird = True
chicken.color = 'Orange'
chicken.eggs_production = 2
chicken.weight = 5
chicken.hunger = 45

goose = Animal()
goose.name = 'Goose'
goose.isabird = True
goose.color = 'Grey'
goose.weight = 7
goose.hunger = 15
