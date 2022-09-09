import time
import arcade
from player import Player
from ground import Ground
from enemy import Enemy

class Game(arcade.Window):
    def __init__(self):
        self.w = 900
        self.h = 600
        super().__init__(self.w, self.h, 'Nostalgic_Game')
        self.t1 = time.time()
        self.bg_img = arcade.load_texture('bg.png')
        self.gravity = 0.5
        self.me = Player()
        self.ground_list = arcade.SpriteList()
        for i in range(65, 900, 130):
            self.ground_list.append(Ground(i, 40))
        self.enemy_list = arcade.SpriteList()
        self.all_object_lists = []
        self.all_object_lists.append(self.ground_list)
        self.all_object_lists.append(self.enemy_list)

        self.physics_engine = arcade.PhysicsEnginePlatformer(self.me, self.all_object_lists, gravity_constant=self.gravity)

    def on_draw(self):
        arcade.start_render()
        arcade.draw_lrwh_rectangle_textured(0, 0, self.w, self.h, self.bg_img)
        self.me.draw()
        for ground in self.ground_list:
            ground.draw()
        for enemy in self.enemy_list:
            enemy.draw()

    def on_update(self, delta_time: float):
        self.t2 = time.time()
        if self.t2 - self.t1 > 5:
            self.enemy_list.append(Enemy())
            self.t1 = time.time()
        self.physics_engine.update()
    
    def on_key_press(self, key, modifiers):
        if key == arcade.key.LEFT:
            self.me.change_x = -1 * self.me.speed
        elif key == arcade.key.RIGHT:
            self.me.change_x = 1 * self.me.speed
        elif key == arcade.key.UP:
            if self.physics_engine.can_jump():
                self.me.change_y = 20
            
    def on_key_release(self, key, modifiers):
        self.me.change_x = 0
        
nostalgic_game = Game()
arcade.run()



        