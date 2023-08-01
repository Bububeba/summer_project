# здесь подключаются модули
import pygame
import sys
from random import *
from weapon import *
from coin   import *
from enemy  import *
from main_hero import *
from map import Room


# константы
WIDTH = 600
HEIGHT = 600
FPS = 30

# speed = 5

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
pygame.time.set_timer(pygame.USEREVENT, 5000)



flmove_up    = False            # двигаться вверх?
flmove_down  = False            # двигаться вниз?
flmove_right = False            # двигаться впрвао?
flmove_left  = False            # двигаться влево?
fllast_move_is_right = True     # последнее движение было вправо?


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


range_anim = [pygame.image.load('sprites\i_range_1.png').convert_alpha(), 
              pygame.image.load('sprites\i_range_2.png').convert_alpha(),
              pygame.image.load('sprites\i_range_3.png').convert_alpha(),
              pygame.image.load('sprites\i_range_4.png').convert_alpha(),
              pygame.image.load('sprites\i_range_5.png').convert_alpha(),
              pygame.image.load('sprites\i_range_6.png').convert_alpha()]

range_hit_anim =   [pygame.image.load('sprites\i_range_hit_1.png').convert_alpha(), 
                    pygame.image.load('sprites\i_range_hit_2.png').convert_alpha(),
                    pygame.image.load('sprites\i_range_hit_3.png').convert_alpha(),
                    pygame.image.load('sprites\i_range_hit_4.png').convert_alpha(),
                    pygame.image.load('sprites\i_range_hit_5.png').convert_alpha(),
                    pygame.image.load('sprites\i_range_hit_6.png').convert_alpha()]


image_weapon = pygame.image.load('sprites\scythe3.png').convert_alpha()
image_weapon = pygame.transform.rotate(image_weapon , -15)
image_weapon = pygame.transform.scale(image_weapon , (image_weapon .get_width() * 1.3, image_weapon .get_height() * 1.3))

image_range  = pygame.image.load('sprites\i_range_1.png').convert_alpha()
image_range_hit  = pygame.image.load('sprites\i_range_hit_1.png').convert_alpha()

animcount = 0         # счетчик кадров для анимации

Main_Hero = Hero(WIDTH // 2, HEIGHT // 2, 'sprites\move_right_1.png', 100, 0, 7, None, None)

weapon = Weapon(Main_Hero.rect.centerx + 33, Main_Hero.rect.centery - 10, 'sprites\scythe3.png', "Main_Hero", 3, 150)
center = weapon.rect.center
weapon.rect = weapon.image.get_rect(center = center)

range = Range (*Main_Hero.rect.center, 'sprites\i_range_1.png')

Main_Hero.range  = range
Main_Hero.weapon = weapon


coins  = pygame.sprite.Group()
enemys = pygame.sprite.Group()

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
r2 = """WWWWWWWWWWWW
W          W
W          W
W          W
W          W
W          W
W          W
W          W
w          W
           W
           W                  
WWWWWWWWWWWW
"""


# size = (700, 700)
# screen = pygame.display.set_mode(size)
donbass = []
room1 = Room(r1, 80, 250, 250, 50)
room2 = Room(r2, 70, 470, 100, 100)
world = [room1, room2]

rect = pygame.rect


# если надо до цикла отобразить
# какие-то объекты, обновляем экран
# Enemy(300, 300,'sprites\coin_1.png', 50, 10, 5, 1, enemys)
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


            elif event.key == pygame.K_d or event.key==pygame.K_RIGHT:
                # flmove_up    = False
                # flmove_down  = False
                flmove_left  = False
                flmove_right = True

                fllast_move_is_right = True
            elif event.key == pygame.K_ESCAPE:
                sys.exit()

        
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
            # Coin(randint(25, WIDTH - 25), randint(25, HEIGHT - 25),'sprites\coin_1.png', coins)
            Enemy(randint(25, WIDTH - 25), randint(25, HEIGHT - 25),'sprites\enemy1.png', 200, 1, 5, 1, enemys)
            # print(enemys)
         
    # обновление объектов    
    animcount += 1
    if animcount + 2 >= FPS:
        animcount = 0

    
    # Main_Hero.weapon.range = 150 + Main_Hero.coins_score
    
    Main_Hero.update(animcount, move_right, move_left,
                    flmove_up, flmove_down, flmove_left, flmove_right, 
                    fllast_move_is_right, room1)
    

    Main_Hero.update_weapon(animcount, fllast_move_is_right,
                            Main_Hero.weapon, image_weapon, range, image_range, image_range_hit, enemys, coins)
    

    enemys.update(Main_Hero, pygame.time.get_ticks())
    # print(enemys)
    coins.update(animcount, coin_anim, Main_Hero)
    

    # --------
 
    # обновление экрана
    screen.fill((255,255,255))

    
    screen.blit(range.image, (range.rect[0], range.rect[1] ))
    screen.blit(Main_Hero.image, Main_Hero.rect)
    screen.blit(weapon.image, (weapon.rect[0], weapon.rect[1] + animcount // 6))
    enemys.draw(screen)
    coins.draw(screen)


    font = pygame.font.SysFont('couriernew', int(40))
    text = font.render(str("HP: " + str(Main_Hero.hp)), True, BLACK )
    # room1.room_draw(screen, Main_Hero, donbass)
    screen.blit(text, (0, 0))

    pygame.draw.rect(screen, RED, pygame.Rect(*Main_Hero.rect.topleft,  100, 100), 1)
    pygame.draw.rect(screen, RED, pygame.Rect(*Main_Hero.range.rect.topleft,  150 + animcount // 2, 150 + animcount // 2), 1)
    for x in enemys:
        # print (*x.rect.topleft)
        # print( x.image.get_width)
        # print( x.image.get_height)
        pygame.draw.rect(screen, RED, pygame.Rect(*x.rect.topleft,  x.image.get_width(), x.image.get_height()), 1)
        
        pygame.draw.circle(screen, RED, x.rect.center, 100, 1)
        pass
        


    pygame.display.update()
     
    # coins.update()
    