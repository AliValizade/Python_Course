import random, arcade
SCREEN_WIDTH = 500
SCREEN_HEIGHT = 500
class Snake(arcade.Sprite):
    def __init__(self):
        super().__init__()
        self.width = 16
        self.height = 16
        self.color1 = arcade.color.DARK_GREEN
        self.color2 = arcade.color.GREEN
        self.score = 1
        self.center_x = SCREEN_WIDTH // 2
        self.center_y = SCREEN_HEIGHT // 2
        self.change_x = 0
        self.change_y = 0
        self.speed = 2
        self.body = []
        self.body.append([self.center_x, self.center_y])

    def draw(self):
        self.body.append([self.center_x, self.center_y])
        for i in range(len(self.body)):
            if i == 0:
                arcade.draw_rectangle_filled(self.body[i][0], self.body[i][1], self.width, self.height, self.color1)
            elif i>0 and i % 2 == 0:
                arcade.draw_rectangle_filled(self.body[i][0], self.body[i][1], self.width, self.height, self.color2)
            else:
                arcade.draw_rectangle_filled(self.body[i][0], self.body[i][1], self.width, self.height, self.color1)
        if len(self.body) > self.score:
            self.body.pop(0)

    def move(self):
        self.center_x += (self.change_x * self.speed)
        self.center_y += (self.change_y * self.speed)

    def eat(self, food):
        if food == 1:
            self.score += 1
            self.body.append([self.center_x, self.center_y])
        if food == 2:
            self.score += 2
            self.body.append([self.center_x, self.center_y])
            self.body.append([self.center_x, self.center_y])
        if food == 0:
            self.score -= 1
            self.body.pop()           

class Apple(arcade.Sprite):
    def __init__(self):
        super().__init__()
        self.apple = arcade.Sprite('apple.png', scale=1)
        self.apple.center_x = random.randint(10, SCREEN_WIDTH-10)
        self.apple.center_y = random.randint(10, SCREEN_HEIGHT-10)

    def draw(self):
        self.apple.draw()
class Pear(arcade.Sprite):
    def __init__(self):
        super().__init__()
        self.pear = arcade.Sprite('pear.png', scale=1)
        self.pear.center_x = random.randint(10, SCREEN_WIDTH-10)
        self.pear.center_y = random.randint(10, SCREEN_HEIGHT-10)

    def draw(self):
        self.pear.draw()

class Poo(arcade.Sprite):
    def __init__(self):
        super().__init__()
        self.poo = arcade.Sprite('poo.png', scale=1)
        self.poo.center_x = random.randint(10, SCREEN_WIDTH-10)
        self.poo.center_y = random.randint(10, SCREEN_HEIGHT-10)

    def draw(self):
        self.poo.draw()

class Game(arcade.Window):
    def __init__(self):
        super().__init__(width=SCREEN_WIDTH, height=SCREEN_HEIGHT, title='Snake')
        arcade.set_background_color(arcade.color.SAND)
        self.snake = Snake()
        self.apple = Apple()
        self.pear = Pear()
        self.poo = Poo()

    def on_draw(self):
        arcade.start_render()
        self.snake.draw()
        self.apple.draw()
        self.pear.draw()
        self.poo.draw()
        score = f"Score: {self.snake.score}"
        arcade.draw_text(score, 20, 465, arcade.color.DARK_BLUE, 15, align='left')
        if self.snake.score <= 0 or self.snake.center_x < 0 or self.snake.center_x > SCREEN_WIDTH or self.snake.center_y < 0 or self.snake.center_y > SCREEN_HEIGHT:
            arcade.draw_text('GameOver!', 140, 250, arcade.color.DARK_RED, 30)
            arcade.pause(5)
            arcade.draw_text('Press "Q" to Quit!', 130, 150, arcade.color.RED, 24)

    def on_key_release(self, key: int, modifiers: int):
        super().on_key_release(key, modifiers)
        if key == arcade.key.UP:
            self.snake.change_y = 1
            self.snake.change_x = 0
        elif key == arcade.key.DOWN:
            self.snake.change_y = -1
            self.snake.change_x = 0
        elif key == arcade.key.LEFT:
            self.snake.change_x = -1
            self.snake.change_y = 0
        elif key == arcade.key.RIGHT:
            self.snake.change_x = 1
            self.snake.change_y = 0
        elif key == arcade.key.Q:
            arcade.exit()
    
    def on_update(self, delta_time: float):
        self.snake.move()
        if arcade.check_for_collision(self.apple.apple, self.snake):
            self.snake.eat(1)
            self.apple = Apple()
        if arcade.check_for_collision(self.pear.pear, self.snake):
            self.snake.eat(2)
            self.pear = Pear()
        if arcade.check_for_collision(self.poo.poo, self.snake):
            self.snake.eat(0)
            self.poo = Poo()
game_board = Game()
arcade.run()