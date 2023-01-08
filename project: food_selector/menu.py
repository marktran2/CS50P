from food import Food

class Menu():
    def __init__(self):
        self.foodlist = []
    

    def add_food(self, name, type, style):
        food = Food(name, type, style)
        self.foodlist.append(food)