import arcade

class Dino(arcade.Sprite):
    def __init__(self):
        super().__init__()
        self.texture = arcade.load_texture('img/dino-w0.png')
        self.center_x = 200
        self.center_y = 44
        self.scale = 0.15
        self.speed = 2
        self.jump_sound = arcade.load_sound('sounds/button-press.mp3')
    
        