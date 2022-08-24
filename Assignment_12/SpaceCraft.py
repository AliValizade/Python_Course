import math, random, time
from os import remove
import arcade

class Enamy(arcade.Sprite):
    def __init__(self, w, h):
        super().__init__(":resources:images/space_shooter/playerShip3_orange.png")
        self.width = 48
        self.height = 48
        self.speed = 4
        self.angle = 180
        self.center_x = random.randint(0, w)
        self.center_y = h
        
    def move(self):
        self.center_y -= self.speed

class Bullet(arcade.Sprite):
    def __init__(self, host):
        super().__init__(":resources:images/space_shooter/laserRed01.png")
        self.angle = host.angle
        self.speed = 5
        self.center_x = host.center_x
        self.center_y = host.center_y
        
    def move(self):
        angle_rad = math.radians(self.angle)
        self.center_x -= self.speed * math.sin(angle_rad)
        self.center_y += self.speed * math.cos(angle_rad)

class SpaceCraft(arcade.Sprite):
    def __init__(self, w, h):
        super().__init__(":resources:images/space_shooter/playerShip1_green.png")
        self.width = 48
        self.height = 48
        self.speed = 5
        self.score = 0
        self.health = 3
        self.center_x = w // 2
        self.center_y = 48
        self.angle = 0
        self.change_angle = 0
        self.bullet_list = []

    def rotate(self):
        self.angle += self.change_angle * self.speed
    
    def fire(self):
        self.bullet_list.append(Bullet(self))

class Life(arcade.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.img_life = arcade.load_texture('heart.png')
        self.width = 48
        self.height = 48
        self.center_x = x
        self.center_y = y

class Game(arcade.Window):
    def __init__(self):
        self.w = 800
        self.h = 600
        super().__init__(self.w, self.h, 'SpaceCraft')
        arcade.set_background_color = arcade.color.BLACK
        self.bg_image = arcade.load_texture(":resources:images/backgrounds/stars.png")
        self.my_airplane = SpaceCraft(self.w, self.h)
        self.enemy_list = []
        self.start_time = time.time()
        self.life = Life(30, 30)
        # self.life_list = []
        # x = 0
        # for i in range(self.my_airplane.health):
        #     self.life_list.append(Life(30 + x, 30))  
        #     x += 30

    def on_draw(self):
        arcade.start_render()
        arcade.draw_lrwh_rectangle_textured(0, 0, self.w, self.h, self.bg_image)
        self.my_airplane.draw()
        score = f"Score: {self.my_airplane.score}"
        arcade.draw_text(score, 20, 565, arcade.color.YELLOW, 16, align='left')
        for i in range(len(self.my_airplane.bullet_list)):
            self.my_airplane.bullet_list[i].draw()
        for i in range(len(self.enemy_list)):
            self.enemy_list[i].draw()
        for i in range(self.my_airplane.health):
            arcade.draw_lrwh_rectangle_textured(20 + i*30, 20, 30, 30, self.life.img_life)
        if self.my_airplane.health == 0:
            arcade.draw_text('GameOver!', 330, 300, arcade.color.RED, 30)
            arcade.pause(1)
            arcade.draw_text('Press "Q" to Quit!', 310, 200, arcade.color.RED, 24)
    def on_update(self, delta_time: float):
        self.end_time = time.time()
        if self.end_time - self.start_time > 4:
            self.enemy_list.append(Enamy(self.w, self.h))
            self.start_time = time.time()
        self.my_airplane.rotate()
        for i in range(len(self.my_airplane.bullet_list)):
            self.my_airplane.bullet_list[i].move()
        for i in range(len(self.enemy_list)):
            self.enemy_list[i].move()
        for bullet in self.my_airplane.bullet_list:
            for enemy in self.enemy_list:
                if arcade.check_for_collision(bullet, enemy):
                    self.enemy_list.remove(enemy)
                    self.my_airplane.bullet_list.remove(bullet)
                    self.my_airplane.score += 1
        for enemy in self.enemy_list:
            if enemy.center_y < 0:
                self.enemy_list.remove(enemy)
                self.my_airplane.health -= 1
        for bullet in self.my_airplane.bullet_list:
            if bullet.center_x > self.w or bullet.center_y > self.h:
                self.my_airplane.bullet_list.remove(bullet)
                
    def on_key_press(self, key: int, modifiers: int):
        if key == arcade.key.RIGHT:
            self.my_airplane.change_angle = -1
        elif key == arcade.key.LEFT:
            self.my_airplane.change_angle = 1
        elif key == arcade.key.SPACE:
            self.my_airplane.fire()
        elif key == arcade.key.Q:
            arcade.exit()
    def on_key_release(self, symbol: int, modifiers: int):
        self.my_airplane.change_angle = 0
        

game = Game()
arcade.run()
        