import arcade

class Ground(arcade.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.texture = arcade.load_texture(':resources:images/tiles/grassMid.png')
        self.width = 130
        self.height = 130
        self.center_x = x
        self.center_y = y
class Ston_bench(arcade.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.texture = arcade.load_texture(':resources:images/tiles/grassHalf_mid.png')
        self.width = 130
        self.height = 130
        self.center_x = x
        self.center_y = y