import time
import arcade
from player import Player, Life
from ground import Ground, Ston_bench
from enemy import Enemy

class Game(arcade.Window):
    def __init__(self):
        self.w = 900
        self.h = 600
        super().__init__(self.w, self.h, 'Nostalgic_Game')
        self.t1 = time.time()
        self.bg_img = arcade.load_texture('img/bg.png')
        self.gravity = 0.2
        self.me = Player()
        self.life = Life(20, 570)
        self.key = arcade.Sprite(':resources:images/items/keyGreen.png')
        self.key.width = 50
        self.key.height = 50
        self.key.center_x = 870
        self.key.center_y = 500
        self.lock = arcade.Sprite('img/closed.png')
        self.lock.width = 80
        self.lock.height = 110
        self.lock.center_x = 860
        self.lock.center_y = 145
        self.ground_list = arcade.SpriteList()
        for i in range(65, 900, 130):
            self.ground_list.append(Ground(i, 40))
        self.ston_bench_list = arcade.SpriteList()
        for i in range(100, 550, 130):
            self.ground_list.append(Ston_bench(i, 230))
        for i in range(450, 850, 130):
            self.ground_list.append(Ston_bench(i, 420))
        self.enemy_list = arcade.SpriteList()
        self.my_physics_engine = arcade.PhysicsEnginePlatformer(self.me, self.ground_list, gravity_constant=self.gravity)
        self.enemy_physics_engine_list = []

    def on_draw(self):
        arcade.start_render()
        arcade.draw_lrwh_rectangle_textured(0, 0, self.w, self.h, self.bg_img)
        for i in range(self.me.health):
            arcade.draw_lrwh_rectangle_textured(20 + i*30, 570, 30, 30, self.life.img_life)
        if self.me.health == 0:
            arcade.draw_text('GameOver!', 430, 300, arcade.color.RED, 30)
            arcade.finish_render()
            time.sleep(0.5)
        try:
            self.key.draw()
        except:
            pass
        self.lock.draw()
        self.me.draw()
        for ground in self.ground_list:
            ground.draw()
        for enemy in self.enemy_list:
            enemy.draw()
        if self.lock.texture == arcade.load_texture('img/opened.png'):
            arcade.draw_text('Hoora! Door opened✅', 700, 220, arcade.color.GREEN, 14)

    def on_update(self, delta_time: float):
        self.me.update_animation()
        for enemy in self.enemy_list:
            enemy.update_animation()
        self.t2 = time.time()
        if self.t2 - self.t1 > 5:
            new_enemy = Enemy()
            self.enemy_list.append(new_enemy)
            self.enemy_physics_engine_list.append(arcade.PhysicsEnginePlatformer(new_enemy, self.ground_list, gravity_constant=self.gravity))
            self.t1 = time.time()
        self.my_physics_engine.update()
        for enemy in self.enemy_physics_engine_list:
            enemy.update()
        try:
            if arcade.check_for_collision(self.me, self.key):
                self.me.pocket.append(self.key)
                del self.key
        except:
            pass
        if arcade.check_for_collision(self.me, self.lock):
            self.me.stop()
            if len(self.me.pocket) == 1:
                self.lock.texture = arcade.load_texture('img/opened.png')
        for enemy in self.enemy_list:
            if arcade.check_for_collision(self.me, enemy):
                self.enemy_list.remove(enemy)
                self.me.health -= 1
            if enemy.center_x < 0 or enemy.center_x > 900:
                self.enemy_list.remove(enemy)
            
    def on_key_press(self, key, modifiers):
        if key == arcade.key.LEFT:
            self.me.change_x = -1 * self.me.speed
        elif key == arcade.key.RIGHT:
            self.me.change_x = 1 * self.me.speed
        elif key == arcade.key.UP:
            if self.my_physics_engine.can_jump():
                self.me.change_y = 10
            
    def on_key_release(self, key, modifiers):
        self.me.change_x = 0
        
nostalgic_game = Game()
arcade.run()



        