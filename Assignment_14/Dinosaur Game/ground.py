from random import randint
import arcade

class Ground(arcade.Sprite):
    def __init__(self):
        super().__init__()
        self.texture = arcade.load_texture('img/g1.png')


class Cloud(arcade.Sprite):
    def __init__(self, w, min, max):
        super().__init__()
        self.texture = arcade.load_texture('img/cloud.png')
        self.max_cloud = 5
        self.left = randint(0, w)
        self.top = randint(min, max)
        self.speed = -0.5
