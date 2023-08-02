# здесь подключаются модули
import pygame
from pygame.locals import *
import sys
from random import *
from weapon import *
from coin   import *
from enemy  import *
from main_hero import *
from map import Room

# константы
WIDTH = 1000
HEIGHT = 800
FPS = 30



BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED   = (255, 0, 0)
 


# здесь происходит инициация,
# создание объектов
pygame.init()

screen = pygame.display.set_mode((WIDTH, HEIGHT))
screen.fill(BLACK)
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

cross_anim = [pygame.image.load('sprites\cross_1.png').convert_alpha(), 
              pygame.image.load('sprites\cross_2.png').convert_alpha(),
              pygame.image.load('sprites\cross_3.png').convert_alpha(),
              pygame.image.load('sprites\cross_4.png').convert_alpha(),
              pygame.image.load('sprites\cross_3.png').convert_alpha(),
              pygame.image.load('sprites\cross_2.png').convert_alpha()]

enemy_anim = [pygame.image.load('sprites\enemy_1.png').convert_alpha(), 
              pygame.image.load('sprites\enemy_2.png').convert_alpha(),
              pygame.image.load('sprites\enemy_3.png').convert_alpha(),
              pygame.image.load('sprites\enemy_4.png').convert_alpha(),
              pygame.image.load('sprites\enemy_5.png').convert_alpha(),
              pygame.image.load('sprites\enemy_6.png').convert_alpha()]

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

load_anim = [pygame.transform.scale(pygame.image.load('images\load1.png'), (WIDTH, HEIGHT)).convert_alpha(),
                pygame.transform.scale(pygame.image.load('images\load2.png'), (WIDTH, HEIGHT)).convert_alpha(),
                pygame.transform.scale(pygame.image.load('images\load3.png'), (WIDTH, HEIGHT)).convert_alpha(),
                pygame.transform.scale(pygame.image.load('images\load4.png'), (WIDTH, HEIGHT)).convert_alpha(),
                pygame.transform.scale(pygame.image.load('images\load5.png'), (WIDTH, HEIGHT)).convert_alpha(),
                pygame.transform.scale(pygame.image.load('images\load6.png'), (WIDTH, HEIGHT)).convert_alpha(),
                pygame.transform.scale(pygame.image.load('images\load7.png'), (WIDTH, HEIGHT)).convert_alpha(),
                pygame.transform.scale(pygame.image.load('images\load8.png'), (WIDTH, HEIGHT)).convert_alpha(),
                pygame.transform.scale(pygame.image.load('images\load9.png'), (WIDTH, HEIGHT)).convert_alpha(),
                pygame.transform.scale(pygame.image.load('images\load10.png'), (WIDTH, HEIGHT)).convert_alpha(),
                pygame.transform.scale(pygame.image.load('images\load11.png'), (WIDTH, HEIGHT)).convert_alpha(),
                pygame.transform.scale(pygame.image.load('images\load12.png'), (WIDTH, HEIGHT)).convert_alpha(),
                pygame.transform.scale(pygame.image.load('images\load13.png'), (WIDTH, HEIGHT)).convert_alpha(),
                pygame.transform.scale(pygame.image.load('images\load14.png'), (WIDTH, HEIGHT)).convert_alpha(),
                pygame.transform.scale(pygame.image.load('images\load15.png'), (WIDTH, HEIGHT)).convert_alpha(),
                pygame.transform.scale(pygame.image.load('images\load16.png'), (WIDTH, HEIGHT)).convert_alpha()]

image_weapon = pygame.image.load('sprites\scythe3.png').convert_alpha()
image_weapon = pygame.transform.rotate(image_weapon , -15)
image_weapon = pygame.transform.scale(image_weapon , (image_weapon .get_width() * 1.3, image_weapon .get_height() * 1.3))

image_range  = pygame.image.load('sprites\i_range_1.png').convert_alpha()
image_range_hit  = pygame.image.load('sprites\i_range_hit_1.png').convert_alpha()

animcount = 0         # счетчик кадров для анимации

r0 = """WWWGGGWWW
W       W
W       W
W       W
W       W
W       W
W       W
W       W
W       W
W       W
W       W
W       W
W       W
WWWWWWWWW
"""
r1 = """WGGGWWWWWWWW
W          W
W          W
W          W
W          W
W          W
W          W
W          W
G          W
G          W
G          W
WWWWWWWWWWWW
"""
r2 = """WWWWWWWWWWWWWWWWWW
W                W
G                G
G                G
G                G
W                W
W                W
W                W
W                W
WWWWWWWWWWGGGWWWWW
"""
r3 = """WWWGGGWWWWWWWW
W            W
W            W
W            W
W            W
W            W
W            W
W            W
W            W
W            W
W            G
W            G
W            G
WWWWWWWWWWWWWW
"""
r4 = """WWWWWWWWWWWWWWWWWW
G                G
G                G
G                G
WWWWWWWWWWWWWWWWWW
"""
r5 = """WWWWWWWWWWWWWWWWW
G               W
G               W
G               W
W               W
W               W
W               W
W               W
W               W
WWWWWWGGGWWWWWWWW
"""

room0 = Room(r0, WIDTH, HEIGHT, 475, 50, -1, -1, -1, -1, -1, -1, 9, 14)
room1 = Room(r1, WIDTH, HEIGHT, 300, 100, -1, -1, -1, -1, 200, 500, 12, 12)
room2 = Room(r2, WIDTH, HEIGHT, -1, -1, 900, 300, 600, 600, 50, 300, 18, 10)
room3 = Room(r3, WIDTH, HEIGHT, 350, 50, 800, 600, -1, -1, -1, -1, 14, 14)
room4 = Room(r4, WIDTH, HEIGHT, -1, -1, 900, 375, -1, -1, 50, 375, 18, 5)
room5 = Room(r5, WIDTH, HEIGHT, -1, -1, -1, -1, 425, 600, 75, 250, 17, 10)
rooms = [room0, room1, room2, room3, room4, room5]
rooms_u = [1, 3]
rooms_r = [2, 3, 4]
rooms_d = [2, 5]
rooms_l = [1, 2, 4, 5]
room_num = 0
level_num = 0
# rooms[room_num].room_draw(screen, WIDTH, HEIGHT, rooms[room_num].room_w/50, rooms[room_num].room_h/50)

Main_Hero = Hero(500, 655, 'sprites\move_right_1.png', 100, 0, 10)

weapon = Weapon(Main_Hero.rect.centerx + 33, Main_Hero.rect.centery - 10, 'sprites\scythe3.png', "Main_Hero", 300, 10)
center = weapon.rect.center
weapon.rect = weapon.image.get_rect(center = center)

range = Range (*Main_Hero.rect.center, 'sprites\i_range_1.png')

Main_Hero.range  = range
Main_Hero.weapon = weapon

coins  = pygame.sprite.Group()
enemys = pygame.sprite.Group()
crosses = pygame.sprite.Group()

# enemy1 = Enemy(WIDTH//2-200, HEIGHT // 2-200, 'sprites\enemy1.png', 100, 1, 4, 1, enemys, None, None)

enemy_count = 0
spawn_time = 0
max_enemy = 0

# rect = pygame.rect

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

        # elif event.type == pygame.USEREVENT:
        #     pass
            #Coin(randint(WIDTH//2 - rooms[room_num].room_w // 2 + 100, WIDTH//2 + rooms[room_num].room_w // 2 - 50), # 50 - размер клетки
            #     randint(HEIGHT//2 - rooms[room_num].room_h // 2 + 100, HEIGHT//2 + rooms[room_num].room_h // 2 - 50),'sprites\coin_1.png', coins)

        # elif event.type == VIDEORESIZE:# Изменение значений констант при изменении размера окна
        #     WIDTH = event.w
        #     HEIGHT = event.h
        #     screen = pygame.display.set_mode((WIDTH, HEIGHT), RESIZABLE)

    # обновление объектов 
    if level_num == 0:
        hp = 100
        damage= 2
        speed = 4

    elif level_num == 1:
        hp = 110
        damage= 4
        speed = 5

    elif level_num == 2:
        hp = 120
        damage= 6
        speed = 6

    # current_time = pygame.time.get_ticks()
    # temp = enemy_count
    if enemy_count > 0 and  pygame.time.get_ticks() >= spawn_time:
        # print(enemy_count, "ADD")
        Cross(
            randint(WIDTH  // 2 - rooms[room_num].room_w // 2 + 100, WIDTH  // 2 + rooms[room_num].room_w // 2 - 50),
            randint(HEIGHT // 2 - rooms[room_num].room_h // 2 + 100, HEIGHT // 2 + rooms[room_num].room_h // 2 - 50),
            'sprites\cross_1.png',  pygame.time.get_ticks(), crosses)
        
        enemy_count -= 1
        spawn_time =  pygame.time.get_ticks() + 3000
        # print( pygame.time.get_ticks())
        # print( spawn_time)
        # print (enemy_count, len(enemys))
    
    # print (enemy_count, len(enemys))
    # clock = pygame.time.Clock()
    if rooms[room_num].is_clear:
        room_last = room_num
        rooms[room_num].gates.clear()
        
        if rooms[room_num].portal1_x != -1:
            pygame.draw.rect(screen, RED, pygame.Rect(*rooms[room_num].rect1.topleft, 50, 50), 1)
            pygame.display.update()
            # pygame.draw.rect(screen, RED, pygame.Rect(*x.rect.topleft,  x.image.get_width(), x.image.get_height()), 1)
            if rooms[room_num].rect1.collidepoint(*Main_Hero.rect.center): 
                room_num = random.choice(rooms_d)
                coins.empty()
                Main_Hero.x = rooms[room_num].portal3_x
                Main_Hero.y = rooms[room_num].portal3_y - 100
                max_enemy =  randint(3, 7)
                enemy_count = max_enemy
                
                cnt = 0
                while(cnt < len(load_anim)):
                    screen.blit(load_anim[cnt], (0, 0))
                    pygame.display.flip()
                    cnt += 1
                    clock.tick(20)
                rooms[room_last].kills_cnt = 0
                rooms[room_last].is_clear = False

        if rooms[room_num].portal2_x != -1:
            pygame.draw.rect(screen, RED, pygame.Rect(*rooms[room_num].rect2.topleft, 50, 50), 1)
            pygame.display.update()
            # if pygame.Rect.colliderect(Main_Hero.rect, rooms[room_num].rect2):
            if rooms[room_num].rect2.collidepoint(*Main_Hero.rect.center): 
                room_num = random.choice(rooms_l)
                coins.empty()
                Main_Hero.x = rooms[room_num].portal4_x + 100
                Main_Hero.y = rooms[room_num].portal4_y
                max_enemy =  randint(3, 7)
                enemy_count = max_enemy
                cnt = 0
                while (cnt < len(load_anim)):
                    screen.blit(load_anim[cnt], (0, 0))
                    pygame.display.flip()
                    cnt += 1
                    clock.tick(16)
                rooms[room_last].kills_cnt = 0
                rooms[room_last].is_clear = False

        if rooms[room_num].portal3_x != -1:
            pygame.draw.rect(screen, RED, pygame.Rect(*rooms[room_num].rect3.topleft, 50, 50), 1)
            pygame.display.update()
            # if pygame.Rect.colliderect(Main_Hero.rect, rooms[room_num].rect3):
            if rooms[room_num].rect3.collidepoint(*Main_Hero.rect.center): 
                room_num = random.choice(rooms_u)
                coins.empty()
                Main_Hero.x = rooms[room_num].portal1_x
                Main_Hero.y = rooms[room_num].portal1_y + 100
                max_enemy =  randint(3, 7)
                enemy_count = max_enemy
                cnt = 0
                while (cnt < len(load_anim)):
                    screen.blit(load_anim[cnt], (0, 0))
                    pygame.display.flip()
                    cnt += 1
                    clock.tick(16)
                rooms[room_last].kills_cnt = 0
                rooms[room_last].is_clear = False

        if rooms[room_num].portal4_x != -1:
            pygame.draw.rect(screen, RED, pygame.Rect(*rooms[room_num].rect4.topleft, 50, 50), 1)
            pygame.display.update()
            # if pygame.Rect.colliderect(Main_Hero.rect, rooms[room_num].rect4):
            if rooms[room_num].rect4.collidepoint(*Main_Hero.rect.center): 
                room_num = random.choice(rooms_r)
                coins.empty()
                Main_Hero.x = rooms[room_num].portal2_x - 100
                Main_Hero.y = rooms[room_num].portal2_y
                max_enemy =  randint(3, 7)
                enemy_count = max_enemy
                cnt = 0
                while (cnt < len(load_anim)):
                    screen.blit(load_anim[cnt], (0, 0))
                    pygame.display.flip()
                    cnt += 1
                    clock.tick(16)
                rooms[room_last].kills_cnt = 0
                rooms[room_last].is_clear = False




                #rooms[room_num].room_draw(screen, WIDTH, HEIGHT, rooms[room_num].room_w / 50,rooms[room_num].room_h / 50)
                #rooms[room_num-1].kill   


    animcount += 1
    if animcount + 2 >= FPS:
        animcount = 0

    crosses.update(animcount, cross_anim, pygame.time.get_ticks(), enemys, rooms[room_num], hp, damage, speed)
    enemys.update(animcount, enemy_anim, Main_Hero, pygame.time.get_ticks(), rooms[room_num])




    coins.update(animcount, coin_anim, Main_Hero)

    Main_Hero.update(animcount, move_right, move_left,
                    flmove_up, flmove_down, flmove_left, flmove_right, 
                    fllast_move_is_right, rooms[room_num])
    
    Main_Hero.update_weapon(animcount, fllast_move_is_right,
                            Main_Hero.weapon, image_weapon,
                            range, image_range, image_range_hit, 
                            enemys, coins)
    

    
    


    rooms[room_num].update(enemy_count, max_enemy, room_num, screen, WIDTH, HEIGHT, enemys)

    # --------
 
    # обновление экрана
    screen.fill(BLACK)
    rooms[room_num].tiles.clear()
    rooms[room_num].room_draw(screen, WIDTH, HEIGHT, rooms[room_num].room_w/50, rooms[room_num].room_h/50)
    screen.blit(range.image, (range.rect[0], range.rect[1] ))
    screen.blit(Main_Hero.image, Main_Hero.rect)
    screen.blit(weapon.image, (weapon.rect[0], weapon.rect[1] + animcount // 6))
    coins.draw(screen)
    crosses.draw(screen)
    enemys.draw(screen)


    font = pygame.font.SysFont('couriernew', int(40))
    text1 = font.render(str("HP: " + str(Main_Hero.hp)), True, WHITE)
    text2 = font.render(str("Coins: " + str(Main_Hero.coins_score)), True, WHITE)

    screen.blit(text1, (0,  0))
    screen.blit(text2, (0, 50))

    
    pygame.draw.rect(screen, RED, pygame.Rect(rooms[room_num].x_offset, rooms[room_num].y_offset, rooms[room_num].room_w, rooms[room_num].room_h), 1)
    
    
    
    
    
    pygame.draw.rect(screen, RED, pygame.Rect(*Main_Hero.rect.topleft,  100, 100), 1)
    pygame.draw.rect(screen, RED, pygame.Rect(*Main_Hero.range.rect.topleft,   Main_Hero.range.image.get_width(),  Main_Hero.range.image.get_height()), 1)
    
    for x in rooms[room_num].tiles:
        pygame.draw.rect(screen, RED, pygame.Rect(*x.rect.topleft,  x.image.get_width(), x.image.get_height()), 1)

        
    
    for x in enemys:
        pygame.draw.rect(screen, RED, pygame.Rect(*x.rect.topleft,  x.image.get_width(), x.image.get_height()), 1)
        pygame.draw.circle(screen, RED, x.rect.center, x.range, 1)
        
    pygame.display.update()
     