# 1) Create a Food class with a “name” and a “kind” attribute as well as a “describe() ” method (which prints “name” and “kind” in a sentence).
class Food:
    def __init__(self, name, kind):
        self.name = name
        self.kind = kind

    def describe(self):
        print('name is {}, kind is {}'.format(self.name, self.kind))

    def __repr__(self):
        return 'name = {}, kind = {} from class Food'.format(self.name, self.kind)

food = Food('banana', 'fruit')
food.describe()
print(food)

# 2) Try turning describe()  from an instance method into a class and a static method. Change it back to an instance method thereafter.
# class Food:
#     def __init__(self, name, kind):
#         self.name = name
#         self.kind = kind

#     @classmethod
#     def describe(cls):
#         print('name is {}, kind is {}'.format(cls.name, cls.kind))

# food = Food('banana', 'fruit')
# Food.describe()

# class Food:
#     def __init__(self, name, kind):
#         self.name = name
#         self.kind = kind

#     @staticmethod
#     def describe(self):
#         print('name is {}, kind is {}'.format(self.name, self.kind))

# food = Food('banana', 'fruit')
# Food.describe()

# 3) Create a  “Meat” and a “Fruit” class – both should inherit from “Food”. Add a “cook() ” method to “Meat” and “clean() ” to “Fruit”.
class Meat(Food):
    def __init__(self, name):
        super().__init__(name, 'Meat')
    
    def cook(self):
        print('Cooking {} {}'.format(self.name, self.kind))

class Fruit(Food):
    def __init__(self, name):
        super().__init__(name, 'Fruit')

    def clean(self):
        print('Cleaning {} fruit'.format(self.name, self.kind))

beef = Meat('beef')
beef.describe()
beef.cook()
fruit = Fruit('orange')
fruit.describe()
fruit.clean()
        

# 4) Overwrite a “dunder” method to be able to print your “Food” class.