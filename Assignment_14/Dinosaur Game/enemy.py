import arcade

class Bird(arcade.Sprite):
    def __init__(self):
        super().__init__()
        self.texture = arcade.load_texture('img/bird1.png')
        self.scale = 0.3
        self.bottom = 100

    