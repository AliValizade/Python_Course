import random, arcade
SCREEN_WIDTH = 500
SCREEN_HEIGHT = 500

class Poo(arcade.Sprite):
    def __init__(self):
        super().__init__()
        self.poo = arcade.Sprite('img/poo.png', scale=1)
        self.poo.center_x = random.randint(10, SCREEN_WIDTH-10)
        self.poo.center_y = random.randint(10, SCREEN_HEIGHT-10)

    def draw(self):
        self.poo.draw()