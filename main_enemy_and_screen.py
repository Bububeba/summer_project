# здесь подключаются модули

import pygame
import sys
from random import *
from weapon import *
from coin import *
from main_hero import *
from enemy import *
from map import Room
from pygame.locals import *

# константы
WIDTH = 1000
HEIGHT = 800
FPS = 30

# здесь происходит инициация,
# создание объектов
pygame.init()

screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.RESIZABLE)
screen.fill((0, 0, 0))
pygame.display.set_caption("game_VZ")
clock = pygame.time.Clock()

pygame.time.set_timer(pygame.USEREVENT, 300)

flmove_up = False  # двигаться вверх?
flmove_down = False  # двигаться вниз?
flmove_right = False  # двигаться впрвао?
flmove_left = False  # двигаться влево?
fllast_move_is_right = True  # последнее движение было вправо?

move_right = [pygame.image.load('sprites\move_right_1.png').convert_alpha(),
              pygame.image.load('sprites\move_right_2.png').convert_alpha(),
              pygame.image.load('sprites\move_right_3.png').convert_alpha(),
              pygame.image.load('sprites\move_right_4.png').convert_alpha(),
              pygame.image.load('sprites\move_right_5.png').convert_alpha(),
              pygame.image.load('sprites\move_right_6.png').convert_alpha()]

move_left = [pygame.image.load('sprites\move_left_1.png').convert_alpha(),
             pygame.image.load('sprites\move_left_2.png').convert_alpha(),
             pygame.image.load('sprites\move_left_3.png').convert_alpha(),
             pygame.image.load('sprites\move_left_4.png').convert_alpha(),
             pygame.image.load('sprites\move_left_5.png').convert_alpha(),
             pygame.image.load('sprites\move_left_6.png').convert_alpha()]

coin_anim = [pygame.image.load('sprites\coin_1.png').convert_alpha(),
             pygame.image.load('sprites\coin_2.png').convert_alpha(),
             pygame.image.load('sprites\coin_3.png').convert_alpha(),
             pygame.image.load('sprites\coin_4.png').convert_alpha(),
             pygame.image.load('sprites\coin_5.png').convert_alpha(),
             pygame.image.load('sprites\coin_6.png').convert_alpha()]

range_anim = [pygame.image.load('sprites\i_range_1.png').convert_alpha(),
              pygame.image.load('sprites\i_range_2.png').convert_alpha(),
              pygame.image.load('sprites\i_range_3.png').convert_alpha(),
              pygame.image.load('sprites\i_range_4.png').convert_alpha(),
              pygame.image.load('sprites\i_range_5.png').convert_alpha(),
              pygame.image.load('sprites\i_range_6.png').convert_alpha()]

range_hit_anim = [pygame.image.load('sprites\i_range_hit_1.png').convert_alpha(),
                  pygame.image.load('sprites\i_range_hit_2.png').convert_alpha(),
                  pygame.image.load('sprites\i_range_hit_3.png').convert_alpha(),
                  pygame.image.load('sprites\i_range_hit_4.png').convert_alpha(),
                  pygame.image.load('sprites\i_range_hit_5.png').convert_alpha(),
                  pygame.image.load('sprites\i_range_hit_6.png').convert_alpha()]

image_weapon = pygame.image.load('sprites\scythe3.png').convert_alpha()
image_weapon = pygame.transform.rotate(image_weapon, -15)
image_weapon = pygame.transform.scale(image_weapon, (image_weapon.get_width() * 1.3, image_weapon.get_height() * 1.3))

image_range = pygame.image.load('sprites\i_range_1.png').convert_alpha()
image_range_hit = pygame.image.load('sprites\i_range_hit_1.png').convert_alpha()

animcount = 0  # счетчик кадров для анимации

pygame.time.set_timer(pygame.USEREVENT, 300)

Main_Hero = Hero(WIDTH//2, HEIGHT // 2, 'sprites\move_right_1.png', 100, 0, 5, None, None)

weapon = Weapon(Main_Hero.rect.centerx + 33, Main_Hero.rect.centery - 10, 'sprites\scythe3.png', "Main_Hero", 5, 150)
center = weapon.rect.center
weapon.rect = weapon.image.get_rect(center=center)

range = Range(*Main_Hero.rect.center, 'sprites\i_range_1.png')

Main_Hero.range = range
Main_Hero.weapon = weapon

coins = pygame.sprite.Group()
enemy1 = Enemy(WIDTH//2-200, HEIGHT // 2-200, 'sprites\enemy1.png', 100, 2, 4, 1, None, None)

r1 = """W WWWWWWWWWW
W          W
W          W
W          W
W          W
W          W
W          W
W          W
W          W
W          W
           W
WWWWWWWWWWWW
"""

# size = (600, 600)
# screen = pygame.display.set_mode(size)
donbass = [enemy1]
room1 = Room(r1, WIDTH, HEIGHT, 12, 12)
room1.room_draw(screen, Main_Hero, donbass, WIDTH, HEIGHT, 12, 12)

rect = pygame.rect

# если надо до цикла отобразить
# какие-то объекты, обновляем экран
pygame.display.update()

while True:

    # задержка
    clock.tick(FPS)

    # цикл обработки событий
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w or event.key == pygame.K_UP:
                flmove_up = True
                flmove_down = False
                # flmove_left  = False
                # flmove_right = False

            elif event.key == pygame.K_s or event.key == pygame.K_DOWN:
                flmove_up = False
                flmove_down = True
                # flmove_left  = False
                # flmove_right = False


            elif event.key == pygame.K_a or event.key == pygame.K_LEFT:
                # flmove_up    = False
                # flmove_down  = False
                flmove_left = True
                flmove_right = False

                fllast_move_is_right = False


            elif event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                # flmove_up    = False
                # flmove_down  = False
                flmove_left = False
                flmove_right = True

                fllast_move_is_right = True
            elif event.key == pygame.K_ESCAPE:
                sys.exit()


        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_w or event.key == pygame.K_UP:
                flmove_up = False

            elif event.key == pygame.K_s or event.key == pygame.K_DOWN:
                flmove_down = False

            elif event.key == pygame.K_a or event.key == pygame.K_LEFT:
                flmove_left = False

            elif event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                flmove_right = False

        elif event.type == pygame.USEREVENT:
            Coin(randint(WIDTH//2 - room1.room_w // 2 + 50, WIDTH//2 + room1.room_w // 2 - 50), # 50 - размер клетки
                 randint(HEIGHT//2 - room1.room_h // 2 + 50, HEIGHT//2 + room1.room_h // 2 - 50),'sprites\coin_1.png', coins)
            #Enemy(randint(25, WIDTH - 25), randint(25, HEIGHT - 25), 'sprites\coin_1.png', 20, 1, 5, coins)

        elif event.type == VIDEORESIZE:# Изменение значений констант при изменении размера окна
            WIDTH = event.w
            HEIGHT = event.h
            screen = pygame.display.set_mode((WIDTH, HEIGHT), RESIZABLE)

    # обновление объектов
    animcount += 1
    if animcount + 2 >= 30:
        animcount = 0

    # Main_Hero.weapon.range = 150 + Main_Hero.coins_score

    Main_Hero.update(animcount, move_right, move_left,
                     flmove_up, flmove_down, flmove_left, flmove_right,
                     fllast_move_is_right)

    Main_Hero.update_weapon(animcount, fllast_move_is_right,
                            Main_Hero.weapon, image_weapon, range, image_range, image_range_hit, coins)

    coins.update(animcount, coin_anim, Main_Hero)

    enemy1.update(Main_Hero, pygame.time.get_ticks())

    # --------

    # обновление экрана
    screen.fill((0, 0, 0))

    room1.room_draw(screen, Main_Hero, donbass, WIDTH, HEIGHT, 12, 12)

    screen.blit(range.image, (range.rect[0], range.rect[1]))
    screen.blit(Main_Hero.image, Main_Hero.rect)
    screen.blit(enemy1.image, enemy1.rect)
    screen.blit(weapon.image, (weapon.rect[0], weapon.rect[1] + animcount // 6))
    coins.draw(screen)

    font = pygame.font.SysFont('couriernew', int(40))
    text = font.render(str("HP: " + str(Main_Hero.hp)), True, (255, 255, 255))
    text2 = font.render(str("Coins: " + str(Main_Hero.coins_score)), True, (255, 255, 255))
    screen.blit(text, (0, 0))
    screen.blit(text2, (0, 50))

    pygame.display.update()

    # coins.update()