from random import choice, randint
import arcade
from pyglet.gl import GL_NEAREST
from enum import Enum
from dino import Dino
from enemy import Bird
from ground import Cloud

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 250
WINDOW_TITLE = 'Dino Game'
BACKGROUND_COLOR = (247, 247, 247) #Gray
GROUND_WIDTH = 600
LEVEL_WIDTH_PIXELS = SCREEN_WIDTH * 4
MAX_CLOUDS = 5
CLOUD_YPOS_MIN = 140
CLOUD_YPOS_MAX = 220

DinoStates = Enum('DinoStates', 'IDLING RUNNING JUMPING DUCKING CRASHING')
GameStates = Enum('GameStates', 'PLAYING GAMEOVER')

class Game(arcade.Window):
    def __init__(self, w, h, t):
        super().__init__(w, h, t)
        self.hi_score = 0
        self.dino_state = DinoStates.IDLING
        self.camera = arcade.Camera(SCREEN_WIDTH, SCREEN_HEIGHT)
        self.camera_gui = arcade.Camera(SCREEN_WIDTH, SCREEN_HEIGHT)
        self.set_mouse_visible(False)
        arcade.set_background_color(BACKGROUND_COLOR)
        self.hit_sound = arcade.load_sound('sounds/hit.mp3')

    def setup(self):
        self.elapsed_time = 0.0
        self.score = 0
        self.game_state = GameStates.PLAYING
        # Scene setup
        self.scene = arcade.Scene()
        # Cloud setup
        self.cloud_list = arcade.SpriteList()
        for i in range(MAX_CLOUDS):
            self.cloud = Cloud(SCREEN_WIDTH, CLOUD_YPOS_MIN, CLOUD_YPOS_MAX)
            self.cloud_list.append(self.cloud)
        # Ground setup
        self.ground_list = arcade.SpriteList()
        for i in range(4):
            ground_type = choice(["1", "2", "3", "4"])
            ground = arcade.Sprite('img/' f"g{ground_type}.png")
            ground.hit_box = [[-300, -10], [300, -10], [300, -6], [-300, -6]]
            ground.left = GROUND_WIDTH * i
            ground.bottom = 23
            self.ground_list.append(ground)
        self.scene.add_sprite_list('ground', False, self.ground_list)
        # Dino setup
        self.dino = Dino()
        self.scene.add_sprite('player', self.dino)
        self.dino_state = DinoStates.RUNNING
        # Obstaclas setup
        self.obstacles_list = arcade.SpriteList()
        self.bird = Bird()
        self.bird.right = LEVEL_WIDTH_PIXELS - 100
        self.obstacles_list.append(self.bird)
        self.add_obstacles(SCREEN_WIDTH * 0.8, LEVEL_WIDTH_PIXELS)
        self.scene.add_sprite_list('obstacles', True, self.obstacles_list)
        # Physics engine
        self.physics_engine = arcade.PhysicsEnginePlatformer(self.dino, self.ground_list, gravity_constant= 0.4)

    def add_obstacles(self, xmin, xmax):
        xpos = xmin
        if self.bird.right < self.camera.goal_position[0]:
            is_bird_off_camera = True
        else:
            is_bird_off_camera = False
        while xpos < xmax:
            if randint(1, 5) == 1 and is_bird_off_camera:
                self.bird.bottom = randint(40, 80)
                self.bird.left = xpos
                xpos += self.bird.width + randint(200, 400)
            else:
                variant = choice(['1', '2', '3'])
                cactus = arcade.Sprite('img/' f"c{variant}.png")
                cactus.scale = 0.5
                cactus.left = xpos
                cactus.bottom = 24
                xpos += (cactus.width + randint(200, 400) + cactus.width)
                self.obstacles_list.append(cactus)
    def on_key_press(self, key, modifiers):
        if key == arcade.key.SPACE:
            self.dino_state = DinoStates.JUMPING
            self.physics_engine.jump(6)
            arcade.play_sound(self.dino.jump_sound)
        elif key == arcade.key.DOWN:
            self.dino_state = DinoStates.DUCKING
            self.dino.hit_box = arcade.load_texture('img/dino-down-0.png').hit_box_points
        elif key == arcade.key.ESCAPE:
            arcade.exit()
    def on_key_release(self, key, modifiers):
        if key == arcade.key.SPACE or key == arcade.key.DOWN:
            self.dino_state = DinoStates.RUNNING
            self.dino.hit_box = arcade.load_texture('img/dino-w0.png').hit_box_points
            if self.dino.center_y < 44:
                self.dino.center_y = 44
        if self.game_state == GameStates.GAMEOVER:
            self.setup()
    def on_update(self, delta_time):
        if self.game_state == GameStates.GAMEOVER:
            self.dino.change_x = 0
            if self.score > self.hi_score:
                self.hi_score = self.score
            self.dino.texture = arcade.load_texture('img/gameover.png')
            return
        self.elapsed_time += delta_time
        self.offset = int(self.elapsed_time * 10)
        dino_frame = self.offset % 2
        self.dino.update()
        self.physics_engine.update()
        # Check for collisions
        collisions = self.dino.collides_with_list(self.obstacles_list)
        if len(collisions) > 0:
            arcade.play_sound(self.hit_sound)
            self.dino_state = DinoStates.CRASHING
            self.game_state = GameStates.GAMEOVER
        if self.dino_state == DinoStates.DUCKING:
            self.dino.texture = arcade.load_texture(choice(['img/' f"dino-down-{dino_frame}.png"]))
            arcade.play_sound(self.dino.jump_sound)
        else:
            self.dino.texture = arcade.load_texture(choice(['img/' f"dino-w{dino_frame}.png"]))
        self.dino.change_x = self.dino.speed
        self.camera.move((self.dino.left - 30, 0))
        self.score = int(self.dino.left // 10)
        # Bird animation
        bird_frame = (self.offset // 2) % 2
        self.bird.texture = arcade.load_texture(choice(['img/' f"bird{bird_frame}.png"]))
        # Extend ground
        if self.ground_list[0].right < self.camera.goal_position[0]:
            ground = self.ground_list.pop(0)
            ground.left = self.ground_list[-1].left + GROUND_WIDTH
            self.add_obstacles(self.ground_list[-1].right, ground.right)
            self.ground_list.append(ground)
        # Shift clouds
        self.cloud_list.move(self.cloud.speed, 0)
        for cloud in self.cloud_list:
            if cloud.right < 0:
                cloud.right = SCREEN_WIDTH + randint(0, SCREEN_WIDTH * 0.25)
                cloud.top = randint(CLOUD_YPOS_MIN, CLOUD_YPOS_MAX)
                break

    def on_draw(self):
        arcade.start_render()
        # GUI camera for clouds
        self.camera_gui.use()
        self.cloud_list.draw(filter=GL_NEAREST)
        # Game camera
        self.camera.use()
        self.scene.draw(filter=GL_NEAREST)
        # GUI camera
        self.camera_gui.use()
        arcade.draw_text(f"{self.score:06}", SCREEN_WIDTH - 100, SCREEN_HEIGHT - 30, arcade.color.BLACK, 20)
        arcade.draw_text(f"H I : {self.hi_score:06}", SCREEN_WIDTH - 280, SCREEN_HEIGHT - 30, arcade.color.BLACK, 20)
        if self.game_state == GameStates.GAMEOVER:
            arcade.draw_text('G A M E  O V E R', 250, 150, arcade.color.BLACK, 28)

def main():
    window = Game(SCREEN_WIDTH, SCREEN_HEIGHT, WINDOW_TITLE)
    window.setup()
    arcade.run()
main()
