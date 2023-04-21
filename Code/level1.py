import pygame
import pickle
from os import path
import os
import subprocess

pygame.init()
level = 1
max_levels = 3
clock = pygame.time.Clock()
fps = 60
# 0: platform (6).png
# 1: tred_ball.png
# 2: Crate.png
# 3: platform (7).png
# 4: sCactus (3).png
# 5: platform (12).png
# 6: platform (1).png
# 7: sCactus (2).png
# 8: Block.png
# 9: Stone.png
# 10: platform (10).png
# 11: platform (2).png
# 12: platform (3).png
# 13: platform (11).png
# 14: exit.png
# 15: platform (4).png
# 16: platform (8).png
# 17: platform (9).png
# 18: coin.png
# 19: platform (5).png
world_level_3 = [[3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3],
                 [3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 15, 3],
                 [3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3],
                 [3, 0, 0, 0, 0, 0, 0, 19, 19, 0, 0, 0, 0, 0, 0, 0, 0, 19, 19, 3],
                 [3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7, 12, 3],
                 [3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 14, 12, 12, 12, 12, 16, 4, 3],
                 [3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3],
                 [3, 19, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3],
                 [3, 9, 19, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3],
                 [3, 7, 12, 6, 0, 0, 0, 8, 0, 0, 0, 0, 0, 0, 0, 19, 19, 0, 0, 3],
                 [3, 0, 0, 0, 0, 12, 12, 12, 12, 6, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3],
                 [3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 19, 3],
                 [3, 0, 0, 0, 0, 0, 0, 19, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 11, 3],
                 [3, 0, 0, 0, 0, 0, 0, 9, 19, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3],
                 [3, 0, 0, 0, 10, 0, 9, 9, 9, 0, 0, 5, 0, 0, 0, 9, 0, 0, 19, 3],
                 [3, 7, 12, 12, 12, 12, 14, 12, 12, 14, 12, 14, 12, 12, 12, 12, 12, 12, 13, 3]]

world_level_2 = [[3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3],
                 [3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 8, 3],
                 [3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 9, 9, 0, 9, 0, 0, 0, 0, 0, 3],
                 [3, 9, 0, 0, 0, 0, 0, 0, 0, 4, 10, 10, 0, 10, 0, 0, 9, 0, 0, 3],
                 [3, 0, 9, 0, 0, 4, 10, 1, 0, 0, 0, 0, 0, 0, 0, 4, 10, 10, 10, 3],
                 [3, 0, 0, 9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3],
                 [3, 0, 0, 7, 9, 0, 0, 0, 0, 0, 0, 0, 9, 0, 0, 0, 0, 0, 0, 3],
                 [3, 0, 0, 6, 7, 9, 0, 0, 0, 4, 10, 0, 10, 0, 10, 10, 1, 0, 0, 3],
                 [3, 0, 0, 6, 6, 10, 10, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 9, 3],
                 [3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 9, 9, 9, 0, 0, 4, 3],
                 [3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4, 10, 10, 10, 10, 1, 0, 0, 3],
                 [3, 0, 0, 0, 0, 0, 0, 0, 4, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3],
                 [3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3],
                 [3, 0, 0, 0, 0, 0, 5, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 9, 3],
                 [3, 0, 0, 0, 0, 5, 6, 6, 5, 0, 0, 0, 0, 0, 0, 0, 0, 5, 5, 3],
                 [3, 5, 5, 5, 5, 6, 6, 6, 6, 5, 5, 5, 5, 5, 5, 5, 5, 6, 6, 3]]

# gameWindow
screen_width = 1000  # default = 1100
screen_height = 800  # default = 800
tile_Size = 50  # default 100
tile_size = 50
main_menu = True

# buttons

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Ball Platformer game")

img_List = []
img_List_2 = []
img_List_3 = []
loaded_list_3 = []
# load images
bg_img = pygame.image.load('Images/bg_img.jpeg')
bg_img2 = pygame.image.load('Static_Img/bg_img2.jpeg')
wall_idx = 0


def loadImages():
    entries = os.listdir('./Images')
    # print(entries[1])
    for i in range(0, len(entries)):
        if entries[i] == 'bg_img.jpeg' or entries[i] == '.DS_Store':
            continue
        if entries[i] == 'SideWall.png':
            wall_idx = len(img_List)
        c_path = 'Images/'
        c_path += entries[i]
        curr_img = pygame.image.load(c_path)
        # print(entries[i])
        img_List.append(curr_img)

    entries = os.listdir('./Images_2')
    # print(entries[1])
    for i in range(0, len(entries)):
        if entries[i] == 'bg_img.jpeg' or entries[i] == '.DS_Store':
            continue
        if entries[i] == 'SideWall.png':
            wall_idx = len(img_List)
        c_path = 'Images_2/'
        c_path += entries[i]
        curr_img = pygame.image.load(c_path)
        # print(entries[i])
        img_List_2.append(curr_img)

    entries = os.listdir('./Images_3')
    # print(entries[1])
    c = 0
    for i in range(0, len(entries)):
        print(entries[i])
        if entries[i] == 'bg_img.jpeg' or entries[i] == '.DS_Store':
            continue
        c_path = 'Images_3/'
        c_path += entries[i]
        loaded_list_3.append(entries[i])
        curr_img = pygame.image.load(c_path)
        # print(entries[i])
        img_List_3.append(curr_img)
    print("Number of images loaded:" + str(len(img_List) + len(img_List_2) + len(img_List_3)))


loadImages()
for c in range(len(loaded_list_3)):
    print(str(c) + ": " + loaded_list_3[c])
# define game variables
clicked = False
white = (255, 255, 255)
font = pygame.font.SysFont('Futura', 24)
game_over = 0

# load sounds
pygame.mixer.music.load('img/music.wav')
pygame.mixer.music.set_volume(0.1)
pygame.mixer.music.play(-1, 0.0, 5000)
coin_fx = pygame.mixer.Sound('img/coin.wav')
coin_fx.set_volume(0.5)
jump_fx = pygame.mixer.Sound('img/jump.wav')
jump_fx.set_volume(0.5)
game_over_fx = pygame.mixer.Sound('img/game_over.wav')
game_over_fx.set_volume(0.5)

# define font
font = pygame.font.SysFont('Bauhaus 93', 70)
font_score = pygame.font.SysFont('Bauhaus 93', 30)

# create empty tile list
world_data = []
N_row = round(screen_height / tile_Size)
N_col = round(screen_width / tile_Size)

world_data = [[2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2],
              [2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2],
              [2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 8, 0, 2],
              [2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 2],
              [2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 2],
              [2, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 2],
              [2, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2],
              [2, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 11, 11, 0, 0, 0, 0, 0, 2],
              [2, 0, 11, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2],
              [2, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2],
              [2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 9, 9, 9, 0, 0, 0, 0, 0, 0, 2],
              [2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 6, 6, 6, 0, 0, 0, 1, 1, 1, 2],
              [2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2],
              [2, 1, 1, 1, 1, 1, 0, 0, 1, 1, 0, 0, 0, 0, 1, 1, 1, 0, 0, 2],
              [2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2],
              [2, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 2]]
world_level_1 = [[2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2],
                 [2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2],
                 [2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 8, 0, 2],
                 [2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 2],
                 [2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 2],
                 [2, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 2],
                 [2, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2],
                 [2, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 11, 11, 0, 0, 0, 0, 0, 2],
                 [2, 0, 11, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2],
                 [2, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2],
                 [2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 9, 9, 9, 0, 0, 0, 0, 0, 0, 2],
                 [2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 6, 6, 6, 0, 0, 0, 1, 1, 1, 2],
                 [2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2],
                 [2, 1, 1, 1, 1, 1, 0, 0, 1, 1, 0, 0, 0, 0, 1, 1, 1, 0, 0, 2],
                 [2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2],
                 [2, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 2]]


def draw_text(text, font, col, x, y):
    img = font.render(text, True, col)
    screen.blit(img, (x, y))


# function to reset level
def reset_level(level):
    player.reset(2 * tile_Size, screen_height - 2 * tile_Size)
    coin_group.empty()
    exit_group.empty()
    world = World(world_data, level)
    # create dummy coin for showing the score
    score_coin = Coin(tile_size // 2, tile_size // 2)
    coin_group.add(score_coin)
    return world


class World():
    def __init__(self, data, level=1):
        self.tile_list = []  # will store list of images and their rectangle objects (storing coordinate informations)
        # load images
        if level == 1:
            for row in range(N_row):
                for col in range(N_col):
                    # traverse over all the images and see if it matches any image
                    # for i in range(len(img_List)):
                    idx_blk = world_level_1[row][col]
                    if idx_blk == 9:
                        coin = Coin(col * tile_size + (tile_size // 2), row * tile_size + (tile_size // 2))
                        coin_group.add(coin)
                        continue
                    if idx_blk == 8:
                        exit = Exit(col * tile_size, row * tile_size - (tile_size // 2))
                        exit_group.add(exit)
                        continue
                    if idx_blk != 0:
                        img = pygame.transform.scale(img_List[idx_blk - 1], (tile_Size, tile_Size))
                        img_rect = img.get_rect()
                        img_rect.x = col * tile_Size
                        img_rect.y = row * tile_Size
                        self.tile_list.append((img, img_rect))
        elif level == 2:
            # add poison cloud frrom separate image only
            # poisonCloud=Enemy(13*tile_Size,14*tile_Size-10)
            # poisonCloud_group.add(poisonCloud)
            poisonCloud_group.add(Enemy(13 * tile_Size, 14 * tile_Size - 10))
            for row in range(N_row):
                for col in range(N_col):
                    # traverse over all the images and see if it matches any image
                    # for i in range(len(img_List)):
                    idx_blk = world_level_2[row][col]
                    if idx_blk == 9:
                        coin = Coin(col * tile_size + (tile_size // 2), row * tile_size + (tile_size // 2))
                        coin_group.add(coin)
                        continue
                    if idx_blk == 8:
                        exit = Exit(col * tile_size, row * tile_size - (tile_size // 2))
                        exit_group.add(exit)
                        continue
                    if idx_blk != 0:
                        img = pygame.transform.scale(img_List_2[idx_blk - 1], (tile_Size, tile_Size))
                        img_rect = img.get_rect()
                        img_rect.x = col * tile_Size
                        img_rect.y = row * tile_Size
                        self.tile_list.append((img, img_rect))
        elif level == 3:
            # print(img_List_3)
            img1 = pygame.transform.scale(img_List_3[10], (tile_Size, tile_Size))
            img2 = pygame.transform.scale(img_List_3[5], (tile_Size, tile_Size))
            platform_group.add(Platform(6 * tile_size, 6 * tile_size, 1, 0, img1))
            platform_group.add(Platform(7 * tile_size, 6 * tile_size, 1, 0, img2))

            platform_group.add(Platform(3 * tile_size, 5 * tile_size, 0, 1, img1))
            platform_group.add(Platform(4 * tile_size, 5 * tile_size, 0, 1, img2))

            platform_group.add(Platform(13 * tile_size, 11 * tile_size, 1, 0, img1))
            platform_group.add(Platform(14 * tile_size, 11 * tile_size, 1, 0, img2))

            img_enem = pygame.transform.scale(img_List_3[4], (2 * tile_Size, tile_Size))
            enemy_group.add(Enemy2(14 * tile_size, 4 * tile_size, 1, 0, img_enem))
            # enemy_group.add(Enemy2(12 * tile_size, 19 * tile_size, 1, 0,img_enem))

            for row in range(N_row):
                for col in range(N_col):
                    # traverse over all the images and see if it matches any image
                    # for i in range(len(img_List)):
                    idx_blk = world_level_3[row][col]
                    if idx_blk == 19:
                        coin = Coin(col * tile_size + (tile_size // 2), row * tile_size + (tile_size // 2))
                        coin_group.add(coin)
                        continue
                    if idx_blk == 15:
                        exit = Exit(col * tile_size, row * tile_size - (tile_size // 2))
                        exit_group.add(exit)
                        continue
                    if idx_blk == 5:
                        # lava = Lava(col * tile_size, row * tile_size )
                        # lava_group.add(lava)
                        enemy_group.add(Enemy2(col * tile_size, row * tile_size, 1, 0, img_enem))
                        continue
                    if idx_blk == 8:
                        # lava = Lava(col * tile_size, row * tile_size)
                        # lava_group.add(lava)
                        enemy_group.add(Enemy2(col * tile_size, row * tile_size, 1, 0, img_enem))
                        continue
                    if idx_blk != 0:
                        img = pygame.transform.scale(img_List_3[idx_blk - 1], (tile_Size, tile_Size))
                        img_rect = img.get_rect()
                        img_rect.x = col * tile_Size
                        img_rect.y = row * tile_Size
                        self.tile_list.append((img, img_rect))

    def draw(self):
        for tile in self.tile_list:
            img = tile[0]
            pos = tile[1]
            screen.blit(img, pos)
            # pygame.draw.rect(screen,(255,255,255),pos,2)


class Player():
    def __init__(self, x, y):
        self.reset(x, y)

    def reset(self, x, y):
        # creating a series of images for moving animation 
        self.images_right = []
        self.images_left = []
        self.index = 0
        self.counter = 0  # speed of player animaion
        for num in range(1, 9):
            img_right = pygame.image.load(f'Ball/redBall{num}.png')
            img_right = pygame.transform.scale(img_right, (tile_Size, tile_Size))
            img_left = pygame.transform.flip(img_right, True,
                                             False)  # flip the image across x axis but not across y axis
            self.images_right.append(img_right)
            self.images_left.append(img_left)
        print(len(self.images_left))
        print(len(self.images_right))
        self.image = self.images_right[self.index]
        self.direction = 0
        self.dead_image_ = pygame.image.load('Static_Img/ghost.png')
        self.dead_image = pygame.transform.scale(self.dead_image_, (tile_Size, tile_Size))
        # ************************ end of animation

        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.width = self.image.get_width()
        self.height = self.image.get_height()
        # print(self.rect)
        self.vel_y = 0  # upward velocity on pressing space
        self.jumped = False  # Have I jumped or not by pressing the space button

    def update(self, game_over):
        col_thresh = 20
        dx = 0
        dy = 0
        walk_cooldown = 1

        if game_over == 0:
            # get keypresses
            key = pygame.key.get_pressed()
            if key[pygame.K_SPACE] and self.jumped == False and self.in_air == False:  # to allow only 1 jump
                self.vel_y = -15
                self.jumped = True
            if key[pygame.K_SPACE] == False:
                self.jumped = False
            if key[pygame.K_LEFT]:
                dx -= 5
                self.direction = -1
                self.counter += 1  # cycle through images only when the left or right keys are pressed
                # if counter is incremented and exceedds the walk_cooldown only then the image index will be incremented
            if key[pygame.K_RIGHT]:
                dx += 5
                self.counter += 1
                self.direction = 1

            # handle animation
            # print(self.counter)
            if self.counter > walk_cooldown:
                self.counter = 0
                self.index = (self.index + 1) % (len(self.images_right))  # cycling through the images
                if self.direction == 1:
                    self.image = self.images_right[self.index]
                if self.direction == -1:
                    self.image = self.images_left[self.index]
            # calculate new player position and check collision at new position

            # adding gravity
            self.vel_y += 1
            if self.vel_y > 10:
                self.vel_y = 10  # setting a limit to gravity i.e. falling down
            dy += self.vel_y

            # check collision
            self.in_air = True
            for tile in world.tile_list:
                # check for collision in x direction
                if tile[1].colliderect(self.rect.x + dx, self.rect.y, self.width, self.height):
                    dx = 0
                # check for collision in y direction
                if tile[1].colliderect(self.rect.x, self.rect.y + dy, self.width, self.height):
                    # if collision is taking place then check

                    # check if below the ground i.e. jumping
                    if self.vel_y < 0:
                        dy = tile[
                                 1].bottom - self.rect.top  # resetting the change dy so that it may not go above the block
                        self.vel_y = 0
                    # check ig above the ground i.e. falling
                    elif self.vel_y >= 0:
                        dy = tile[1].top - self.rect.bottom
                        self.vel_y = 0
                        self.in_air = False

            # check for collision with enemies
            if pygame.sprite.spritecollide(self, poisonCloud_group, False):
                game_over = -1
                game_over_fx.play()
            if pygame.sprite.spritecollide(self, enemy_group, False):
                game_over = -1
                game_over_fx.play()

            # check for collision with exit
            if pygame.sprite.spritecollide(self, exit_group, False):
                game_over = 1
            # check for collision with lava
            if pygame.sprite.spritecollide(self, lava_group, False):
                game_over = -1
                game_over_fx.play()
            # check for collision with platform
            for platform in platform_group:
                # collision in the x direction
                if platform.rect.colliderect(self.rect.x + dx, self.rect.y, self.width, self.height):
                    dx = 0
                # collision in the y direction
                if platform.rect.colliderect(self.rect.x, self.rect.y + dy, self.width, self.height):
                    # check if below platform
                    if abs((self.rect.top + dy) - platform.rect.bottom) < col_thresh:
                        self.vel_y = 0
                        dy = platform.rect.bottom - self.rect.top
                    # check if above platform
                    elif abs((self.rect.bottom + dy) - platform.rect.top) < col_thresh:
                        self.rect.bottom = platform.rect.top - 1
                        self.in_air = False
                        dy = 0
                    # move sideways with the platform
                    # if platform.move_x != 0:
                    self.rect.x += platform.move_direction

            # update player coordinates
            self.rect.x += dx
            self.rect.y += dy

            # checking player does not fall of the screen due to gravity
            if self.rect.bottom > screen_height - tile_Size:
                self.rect.bottom = screen_height - tile_Size
                dy = 0
                self.vel_y = 0

        elif game_over == -1:
            blue = (150, 25, 255)
            self.image = self.dead_image
            draw_text('GAME OVER!', font, blue, (screen_width // 2) - 200, screen_height // 2)
            if self.rect.y > 200:
                self.rect.y -= 5
        # draw player on screen
        screen.blit(self.image, self.rect)
        # pygame.draw.rect(screen,(255,255,255),self.rect,2)
        return game_over


class Lava(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        img = pygame.image.load('Images_3/sCactus (3).png')
        self.image = pygame.transform.scale(img, (tile_size, tile_size // 2))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y


class Button():
    def __init__(self, x, y, image):
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.clicked = False

    def draw(self):
        action = False

        # get mouse position
        pos = pygame.mouse.get_pos()

        # check mouseover and clicked conditions
        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                action = True
                self.clicked = True

        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False

        # draw button
        screen.blit(self.image, self.rect)

        return action


class Coin(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        img = pygame.image.load('Images/coin.png')
        self.image = pygame.transform.scale(img, (round(tile_size // 1.5), round(tile_size // 1.5)))
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)


class Exit(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        img = pygame.image.load('Static_Img/exit.png')
        self.image = pygame.transform.scale(img, (tile_size, int(tile_size * 1.5)))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y


class Enemy(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.img = pygame.image.load('Static_Img/poison.png')
        self.image = pygame.transform.scale(self.img, (tile_Size, tile_Size))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.move_direction = 1
        self.move_counter = 0

    def update(self):
        self.rect.x += self.move_direction
        self.move_counter += 1
        if abs(self.move_counter) > 70:
            self.move_direction *= -1
            self.move_counter *= -1


class Platform(pygame.sprite.Sprite):
    def __init__(self, x, y, move_x, move_y, img):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(img, (tile_size, tile_size // 2))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.move_counter = 0
        self.move_direction = 1
        self.move_x = move_x
        self.move_y = move_y

    def update(self):
        self.rect.x += self.move_direction * self.move_x
        self.rect.y += self.move_direction * self.move_y
        self.move_counter += 1
        if abs(self.move_counter) > 70:
            self.move_direction *= -1
            self.move_counter *= -1


class Enemy2(pygame.sprite.Sprite):
    def __init__(self, x, y, move_x, move_y, img):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(img, (tile_size, tile_size))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.move_counter = 0
        self.move_direction = 1
        self.move_x = move_x
        self.move_y = move_y

    def update(self):
        self.rect.x += self.move_direction * self.move_x
        self.rect.y += self.move_direction * self.move_y
        self.move_counter += 1
        if abs(self.move_counter) > 70:
            self.move_direction *= -1
            self.move_counter *= -1


poisonCloud_group = pygame.sprite.Group()  # For level 2,3
enemy_group = pygame.sprite.Group()
lava_group = pygame.sprite.Group()
platform_group = pygame.sprite.Group()  # For level 3
coin_group = pygame.sprite.Group()
exit_group = pygame.sprite.Group()

# create dummy coin for showing the score
score_coin = Coin(tile_size // 2, tile_size // 2)
coin_group.add(score_coin)

world = World(world_data, level)
player = Player(2 * tile_Size, screen_height - 2 * tile_Size)
run = True
count = 0
print("Opening Game Window")

# Load button images
restart_img = pygame.image.load('Static_Img/restart_btn.png')
restart_img = pygame.transform.scale(restart_img, (4 * tile_Size, 2 * tile_Size))
start_img = pygame.image.load('Static_Img/start_btn.png')
start_img = pygame.transform.scale(start_img, (4 * tile_Size, 2 * tile_Size))
exit_img = pygame.image.load('Static_Img/exit_btn.png')
exit_img = pygame.transform.scale(exit_img, (4 * tile_Size, 2 * tile_Size))

# create buttons
restart_button = Button(screen_width // 2 - 50, screen_height // 2 + 100, restart_img)
start_button = Button(screen_width // 2 - 350, screen_height // 2, start_img)
exit_button = Button(screen_width // 2 + 150, screen_height // 2, exit_img)
print('Here')


# subprocess.run("python3 levelSetter.py", shell=True, check=True)
def drawGridWithTileSize(tile_size):
    # draw vertical lines
    N_ver = round(screen_width / tile_size) - 1
    white = (255, 255, 255)
    for i in range(0, N_ver):
        start_pos = (tile_size * (i + 1), 0)
        end_pos = (tile_size * (i + 1), screen_height)
        pygame.draw.line(screen, white, start_pos, end_pos, 1)
    N_hor = round(screen_height / tile_size) - 1
    # draw horizontal lines
    for i in range(0, N_hor):
        start_pos = (0, tile_size * (i + 1))
        end_pos = (screen_width, tile_size * (i + 1))
        pygame.draw.line(screen, white, start_pos, end_pos, 1)


score = 0
while run:
    clock.tick(fps)

    # draw background
    screen.blit(bg_img, (0, 0))
    # if level==3:
    #      screen.blit(bg_img2,(0.0))
    # drawGrid
    # drawGridWithTileSize(tile_Size)
    count += 1

    if main_menu == True:
        if exit_button.draw():
            run = False
        if start_button.draw():
            main_menu = False
    else:
        world.draw()
        if game_over == 0:
            poisonCloud_group.update()
            enemy_group.update()
            platform_group.update()
            # update score
            # check if a coin has been collected
            if pygame.sprite.spritecollide(player, coin_group, True):
                score += 1
                coin_fx.play()
            draw_text('X ' + str(score), font_score, white, tile_size, 15)
        coin_group.draw(screen)
        exit_group.draw(screen)
        poisonCloud_group.draw(screen)
        enemy_group.draw(screen)
        lava_group.draw(screen)
        platform_group.draw(screen)
        game_over = player.update(game_over)
        # if player has died
        if game_over == -1:
            if restart_button.draw():
                world_data = []
                poisonCloud_group.empty()
                enemy_group.empty()
                platform_group.empty()
                world = reset_level(level)
                game_over = 0
                score = 0

            # if player has completed the level
        if game_over == 1:
            # reset game and go to next level
            level += 1
            if level <= 3:
                # reset level
                world_data = []
                lava_group.empty()
                exit_group.empty()
                platform_group.empty()
                world = reset_level(level)

                game_over = 0
            else:
                draw_text('YOU WIN!', font, (255, 255, 70), (screen_width // 2) - 140, screen_height // 2)
                if restart_button.draw():
                    level = 1
                    world_data = []
                    lava_group.empty()
                    exit_group.empty()
                    platform_group.empty()
                    world = reset_level(level)
                    game_over = 0
                    score = 0

    for event in pygame.event.get():
        # quit game
        if event.type == pygame.QUIT:
            run = False
    # print("Here2")
    # update game display window
    pygame.display.update()

print("Count:" + str(count))
pygame.quit()
