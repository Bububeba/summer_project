# здесь подключаются модули

import pygame
import sys
from random import *
from weapon import *
from coin import *
from main_hero import *


flmove_up    = False            # двигаться вверх?
flmove_down  = False            # двигаться вниз?
flmove_right = False            # двигаться впрвао?
flmove_left  = False            # двигаться влево?
fllast_move_is_right = True     # последнее движение было вправо?


WIDTH = 600
HEIGHT = 400
FPS = 30



BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED   = (255, 0, 0)
 
# здесь происходит инициация,
# создание объектов
pygame.init()


screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.RESIZABLE)
screen.fill((255,255,255))
pygame.display.set_caption("game_VZ")
clock = pygame.time.Clock()

pygame.time.set_timer(pygame.USEREVENT, 300)


move_right = [pygame.image.load('sprites\move_right_1.png').convert_alpha(), 
              pygame.image.load('sprites\move_right_2.png').convert_alpha(),
              pygame.image.load('sprites\move_right_3.png').convert_alpha(),
              pygame.image.load('sprites\move_right_4.png').convert_alpha(),
              pygame.image.load('sprites\move_right_5.png').convert_alpha(),
              pygame.image.load('sprites\move_right_6.png').convert_alpha()]

move_left =  [pygame.image.load('sprites\move_left_1.png').convert_alpha(), 
              pygame.image.load('sprites\move_left_2.png').convert_alpha(),
              pygame.image.load('sprites\move_left_3.png').convert_alpha(),
              pygame.image.load('sprites\move_left_4.png').convert_alpha(),
              pygame.image.load('sprites\move_left_5.png').convert_alpha(),
              pygame.image.load('sprites\move_left_6.png').convert_alpha()]

coin_anim =  [pygame.image.load('sprites\coin_1.png').convert_alpha(), 
              pygame.image.load('sprites\coin_2.png').convert_alpha(),
              pygame.image.load('sprites\coin_3.png').convert_alpha(),
              pygame.image.load('sprites\coin_4.png').convert_alpha(),
              pygame.image.load('sprites\coin_5.png').convert_alpha(),
              pygame.image.load('sprites\coin_6.png').convert_alpha()]


animcount = 0         # счетчик кадров для анимации



# если надо до цикла отобразить
# какие-то объекты, обновляем экран

 
speed = 5


pygame.time.set_timer(pygame.USEREVENT, 300)


Main_Hero = Hero(0, HEIGHT // 2, 'sprites\move_right_1.png', 100, 0, 5, None)

image_weapon = pygame.image.load('sprites\scythe3.png').convert_alpha()
image_weapon  = pygame.transform.rotate(image_weapon , -15)
image_weapon = pygame.transform.scale(image_weapon , (image_weapon .get_width() * 1.3, image_weapon .get_height() * 1.3))
weapon = Weapon(Main_Hero.rect.centerx + 33, Main_Hero.rect.centery - 10, 'sprites\scythe3.png', "Main_Hero", 5, 100)
center = weapon.rect.center
weapon.rect = weapon.image.get_rect(center = center)
Main_Hero.weapon = weapon


coins = pygame.sprite.Group()

# all_sprites = pygame.sprite.Group()
# coins.add(Main_Hero)


pygame.display.update()
while True:
 
    # задержка
    clock.tick(FPS)
 
    # цикл обработки событий
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        elif event.type == pygame.KEYDOWN:
            if event.key==pygame.K_w or event.key==pygame.K_UP:
                flmove_up    = True
                flmove_down  = False
                # flmove_left  = False
                # flmove_right = False

            elif event.key==pygame.K_s or event.key==pygame.K_DOWN:
                flmove_up    = False
                flmove_down  = True
                # flmove_left  = False
                # flmove_right = False
                

            elif event.key==pygame.K_a or event.key==pygame.K_LEFT:
                # flmove_up    = False
                # flmove_down  = False
                flmove_left  = True
                flmove_right = False

                fllast_move_is_right = False


            elif event.key==pygame.K_d or event.key==pygame.K_RIGHT:
                # flmove_up    = False
                # flmove_down  = False
                flmove_left  = False
                flmove_right = True

                fllast_move_is_right = True
        
        elif event.type == pygame.KEYUP:
            if event.key==pygame.K_w or event.key==pygame.K_UP:
                flmove_up    = False

            elif event.key==pygame.K_s or event.key==pygame.K_DOWN:
                flmove_down  = False

            elif event.key==pygame.K_a or event.key==pygame.K_LEFT:
                flmove_left  = False

            elif event.key==pygame.K_d or event.key==pygame.K_RIGHT:
                flmove_right = False

        elif event.type == pygame.USEREVENT:
            Coin(randint(25, WIDTH - 25), randint(25, HEIGHT - 25),'sprites\coin_1.png', coins)
         




    # обновление объектов    
    animcount += 1
    if animcount + 2 >= 30:
        animcount = 0


    # if pygame.sprite.collide_rect(Main_Hero, coin):
    #     print("Collision!")


    
    
    Main_Hero.update(animcount, move_right, move_left,
                    flmove_up, flmove_down, flmove_left, flmove_right, 
                    fllast_move_is_right)
    
    Main_Hero.update_weapon(animcount, fllast_move_is_right,
                            Main_Hero.weapon, image_weapon)
    

    
    coins.update(animcount, coin_anim, Main_Hero )
    
    

    # --------
 
    # обновление экрана
    screen.fill((255,255,255))

    
    
    screen.blit(Main_Hero.image, Main_Hero.rect)
    screen.blit(weapon.image, (weapon.rect[0], weapon.rect[1] + animcount // 6))
    coins.draw(screen)


    font = pygame.font.SysFont('couriernew', int(40))
    text = font.render(str("Coins: " + str(Main_Hero.coins_score)), True, BLACK )
    screen.blit(text, (0, 0))

    pygame.display.update()
     
    # coins.update()
    