import random
import arcade

class Enemy(arcade.Sprite):
    def __init__(self):
        super().__init__()
        self.width = 60
        self.height = 60
        self.center_x = random.randint(0, 900)
        self.center_y = random.randint(300, 550)
        self.speed = 5
        self.texture = arcade.load_texture(':resources:images/animated_characters/female_adventurer/femaleAdventurer_walk0.png')
