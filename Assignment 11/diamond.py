import arcade
from PIL import Image

BOARD_WIDTH = 500
BOARD_HEIGHT = 500
class Board(arcade.Window):
    def __init__(self):
        super().__init__(width=BOARD_WIDTH, height=BOARD_HEIGHT, title='Complex Loop - Box')
        arcade.set_background_color(arcade.color.WHITE)
        self.diamond = Diamond()

    def on_draw(self):
        arcade.start_render()
        self.diamond.draw()  

class Diamond(arcade.Sprite):
    def __init__(self):
        super().__init__()
        self.center_x = 0
        self.center_y = 0
        self.color1 = arcade.color.RED
        self.color2 = arcade.color.BLUE
        self.angle = 45

    def draw(self):
        for i in range(10):
            for j in range(10):
                self.center_x = i * 30 + 120
                self.center_y = j * 30 + 120
                if i % 2 == 0:
                    if j % 2 != 0:
                        arcade.draw_rectangle_filled(self.center_x, self.center_y, 18, 18, self.color1, self.angle)
                    else:
                        arcade.draw_rectangle_filled(self.center_x, self.center_y, 18, 18, self.color2, self.angle)
                else:
                    if j % 2 == 0:
                        arcade.draw_rectangle_filled(self.center_x, self.center_y, 18, 18, self.color1, self.angle)
                    else:
                        arcade.draw_rectangle_filled(self.center_x, self.center_y, 18, 18, self.color2, self.angle)
        
board = Board()
arcade.run()