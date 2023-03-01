import random, arcade
SCREEN_WIDTH = 500
SCREEN_HEIGHT = 500

class Apple(arcade.Sprite):
    def __init__(self):
        super().__init__()
        self.apple = arcade.Sprite('img/apple.png', scale=1)
        self.apple.center_x = random.randint(10, SCREEN_WIDTH-10)
        self.apple.center_y = random.randint(10, SCREEN_HEIGHT-10)

    def draw(self):
        self.apple.draw()