import arcade

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
        self.speed = 4
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