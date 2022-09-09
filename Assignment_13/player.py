import arcade

class Player(arcade.Sprite):
    def __init__(self):
        super().__init__()
        self.width = 60
        self.height = 60
        self.center_x = 100
        self.center_y = 400
        self.speed = 5
        self.texture = arcade.load_texture(':resources:images/animated_characters/robot/robot_idle.png')
