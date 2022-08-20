import arcade

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

    def draw(self):
        count = 0
        for i in range(10):
            for j in range(10):
                self.center_x = i * 30 + 120
                self.center_y = j * 30 + 120
                if i % 2 == 0:
                    if j % 2 != 0:
                        arcade.draw_circle_filled(self.center_x, self.center_y, 10, self.color1)
                    else:
                        arcade.draw_circle_filled(self.center_x, self.center_y, 10, self.color2)
                else:
                    if j % 2 == 0:
                        arcade.draw_circle_filled(self.center_x, self.center_y, 10, self.color1)
                    else:
                        arcade.draw_circle_filled(self.center_x, self.center_y, 10, self.color2)
        
board = Board()
arcade.run()