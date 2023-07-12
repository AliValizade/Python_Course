import arcade
from snake import Snake
from apple import Apple
from poo import Poo

SCREEN_WIDTH = 500
SCREEN_HEIGHT = 500

class Game(arcade.Window):
    def __init__(self):
        super().__init__(width=SCREEN_WIDTH, height=SCREEN_HEIGHT, title='Snake')
        arcade.set_background_color(arcade.color.SAND)
        self.snake = Snake()
        self.apple = Apple()
        self.poo = Poo()

    def on_draw(self):
        arcade.start_render()
        self.snake.draw()
        self.apple.draw()
        self.poo.draw()
        score = f"Score: {self.snake.score}"
        arcade.draw_text(score, 20, 465, arcade.color.DARK_BLUE, 15, align='left')
        if self.snake.score <= 0 or self.snake.center_x < 0 or self.snake.center_x > SCREEN_WIDTH or self.snake.center_y < 0 or self.snake.center_y > SCREEN_HEIGHT:
            arcade.draw_text('GameOver!', 140, 250, arcade.color.DARK_RED, 30)
            arcade.pause(5)
            arcade.draw_text('Press "Q" to Quit!', 130, 150, arcade.color.RED, 24)

    def on_key_release(self, key: int, modifiers: int):
        super().on_key_release(key, modifiers)
        # if key == arcade.key.UP:
        #     self.snake.change_y = 1
        #     self.snake.change_x = 0
        # elif key == arcade.key.DOWN:
        #     self.snake.change_y = -1
        #     self.snake.change_x = 0
        # elif key == arcade.key.LEFT:
        #     self.snake.change_x = -1
        #     self.snake.change_y = 0
        # elif key == arcade.key.RIGHT:
        #     self.snake.change_x = 1
        #     self.snake.change_y = 0
        if key == arcade.key.Q:
            arcade.exit()
    
    def on_update(self, delta_time: float):
        if self.snake.center_x < self.apple.apple.center_x:
            self.snake.change_x = 1
        elif self.snake.center_x > self.apple.apple.center_x:
            self.snake.change_x = -1
        else:
            self.snake.change_x = 0
        
        if self.snake.center_y < self.apple.apple.center_y:
            self.snake.change_y = 1
        elif self.snake.center_y > self.apple.apple.center_y:
            self.snake.change_y = -1
        else:
            self.snake.change_y = 0
        self.snake.move()
        if arcade.check_for_collision(self.apple.apple, self.snake):
            self.snake.eat(1)
            self.apple = Apple()
        if arcade.check_for_collision(self.poo.poo, self.snake):
            self.snake.eat(0)
            self.poo = Poo()
game_board = Game()
arcade.run()