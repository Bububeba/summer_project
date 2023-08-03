import pygame
import random
# from main_hero import Hero
from tiles import Tile
# from enemy import Enemy


class Room:
    def __init__(self, location: str, width, height, 
                portal1_x: int, portal1_y: int, portal2_x: int, portal2_y: int,
                portal3_x: int, portal3_y: int, portal4_x: int, portal4_y: int,
                count_of_tile_x, count_of_tile_y, level, kills_cnt = 0, is_clear = False):
                    #1 - up, 2 - right, 3 - down, 4 - left
        self.location = location
        self.elysium_tiles = ['el_wall1.png',
                            'el_wall2.png', 
                            'el_wall3.png', 
                            'el_wall4.png', 
                            'el_corner1.png',
                            'el_corner2.png', 
                            'el_corner3.png', 
                            'el_corner4.png', 
                            'el_fog.png', 
                            'el_floor1.png', 
                            'el_floor2.png',
                            'el_floor3.png', 
                            'el_floor4.png', 
                            'el_floor5.png', 
                            'el_floor6.png', 
                            'el_floor7.png', 
                            'el_floor8.png',
                            'el_floor9.png', 
                            'el_floor10.png', 
                            'el_floor11.png', 
                            'el_floor12.png' , 
                            'el_floor13.png' , 
                            'el_floor14.png']
        
        self.asfodel_tiles = ['as_wall1.png', 'as_wall2.png', 'as_wall3.png', 'as_wall4.png', 'as_corner1.png',
                              'as_corner2.png', 'as_corner3.png', 'as_corner4.png', 'as_lava.png', 'as_floor1.png',
                              'as_floor2.png', 'as_floor3.png', 'as_floor4.png']
        
        self.tartar_tiles = ['tr_wall1.png', 'tr_wall2.png', 'tr_wall3.png', 'tr_wall4.png', 'tr_corner1.png',
                            'tr_corner2.png', 'tr_corner3.png', 'tr_corner4.png', 'tr_water.png', 'tr_floor1.png',
                            'tr_floor2.png', 'tr_floor3.png', 'tr_floor4.png', 'tr_floor5.png', 'tr_floor6.png',
                            'tr_floor7.png', 'tr_floor8.png', 'tr_floor9.png']
        
        self.sticks_tiles = ['as_wall1.png',
                            'as_wall2.png',
                            'as_wall3.png',
                            'as_wall4.png',
                            'as_corner1.png',
                            'as_corner2.png',
                            'as_corner3.png',
                            'as_corner4.png',
                            'as_lava.png',
                            'as_floor1.png',
                            'as_floor2.png',
                            'as_floor3.png',
                            'as_floor4.png']
        
        self.levels = [self.sticks_tiles, self.elysium_tiles, self.asfodel_tiles, self.tartar_tiles]
        # self.wall_tile = "wall.png"
        # self.floor_tile = "floor.png"
        # self.gates_tile = "gate.png"
        self.tiles = []
        self.gates = []
        self.portal1_x = portal1_x
        self.portal1_y = portal1_y
        self.portal2_x = portal2_x
        self.portal2_y = portal2_y
        self.portal3_x = portal3_x
        self.portal3_y = portal3_y
        self.portal4_x = portal4_x
        self.portal4_y = portal4_y
        self.screen_w = width
        self.screen_h = height
        self.room_w = count_of_tile_x * 50
        self.room_h = count_of_tile_y * 50
        self.x_offset = (self.screen_w - self.room_w) // 2
        self.y_offset = (self.screen_h - self.room_h) // 2
        self.level = level
        self.kills_cnt = kills_cnt
        self.is_clear = is_clear
        if portal1_x != -1:
            self.rect1 = pygame.Rect(self.portal1_x, self.portal1_y, 150, 150)
        if portal2_x != -1:
            self.rect2 = pygame.Rect(self.portal2_x, self.portal2_y, 150, 150)
        if portal3_x != -1:
            self.rect3 = pygame.Rect(self.portal3_x, self.portal3_y, 150, 150)
        if portal4_x != -1:
            self.rect4 = pygame.Rect(self.portal4_x, self.portal4_y, 150, 150)


    def room_draw(self, screen, width, height, count_of_tile_x, count_of_tile_y, lvl):
        loc = self.location.splitlines()
        self.screen_w = width
        self.screen_h = height
        self.room_w = count_of_tile_x * 50
        self.room_h = count_of_tile_y * 50
        self.x_offset = (self.screen_w - self.room_w) // 2
        self.y_offset = (self.screen_h - self.room_h) // 2
        for y, line in enumerate(loc):
            for x, c in enumerate(line):
                if c == "U":
                    screen.blit(pygame.image.load(f"images\\{self.levels[lvl][0]}"), (x * 50 + self.x_offset, y * 50 + self.y_offset))
                    self.tiles.append(Tile(x * 50 + self.x_offset, y * 50 + self.y_offset, self.levels[lvl][0]))
                if c == "R":
                    screen.blit(pygame.image.load(f"images\\{self.levels[lvl][1]}"), (x * 50 + self.x_offset, y * 50 + self.y_offset))
                    self.tiles.append(Tile(x * 50 + self.x_offset, y * 50 + self.y_offset, self.levels[lvl][1]))
                if c == "D":
                    screen.blit(pygame.image.load(f"images\\{self.levels[lvl][2]}"), (x * 50 + self.x_offset, y * 50 + self.y_offset))
                    self.tiles.append(Tile(x * 50 + self.x_offset, y * 50 + self.y_offset, self.levels[lvl][2]))
                if c == "L":
                    screen.blit(pygame.image.load(f"images\\{self.levels[lvl][3]}"), (x * 50 + self.x_offset, y * 50 + self.y_offset))
                    self.tiles.append(Tile(x * 50 + self.x_offset, y * 50 + self.y_offset, self.levels[lvl][3]))
                if c == "A":
                    screen.blit(pygame.image.load(f"images\\{self.levels[lvl][4]}"), (x * 50 + self.x_offset, y * 50 + self.y_offset))
                    self.tiles.append(Tile(x * 50 + self.x_offset, y * 50 + self.y_offset, self.levels[lvl][4]))
                if c == "B":
                    screen.blit(pygame.image.load(f"images\\{self.levels[lvl][5]}"), (x * 50 + self.x_offset, y * 50 + self.y_offset))
                    self.tiles.append(Tile(x * 50 + self.x_offset, y * 50 + self.y_offset, self.levels[lvl][5]))
                if c == "C":
                    screen.blit(pygame.image.load(f"images\\{self.levels[lvl][6]}"), (x * 50 + self.x_offset, y * 50 + self.y_offset))
                    self.tiles.append(Tile(x * 50 + self.x_offset, y * 50 + self.y_offset, self.levels[lvl][6]))
                if c == "E":
                    screen.blit(pygame.image.load(f"images\\{self.levels[lvl][7]}"), (x * 50 + self.x_offset, y * 50 + self.y_offset))
                    self.tiles.append(Tile(x * 50 + self.x_offset, y * 50 + self.y_offset, self.levels[lvl][7]))
                if c == "G":
                    screen.blit(pygame.image.load(f"images\\{self.levels[lvl][8]}"), (x * 50 + self.x_offset, y * 50 + self.y_offset))
                    self.gates.append(Tile(x * 50 + self.x_offset, y * 50 + self.y_offset, self.levels[lvl][8]))
                if c == " ":
                    screen.blit(pygame.image.load(f"images\\{self.levels[lvl][9]}"), (x * 50 + self.x_offset, y * 50 + self.y_offset))
                if c == "1":
                    screen.blit(pygame.image.load(f"images\\{self.levels[lvl][10]}"), (x * 50 + self.x_offset, y * 50 + self.y_offset))
                if c == "2":
                    screen.blit(pygame.image.load(f"images\\{self.levels[lvl][11]}"), (x * 50 + self.x_offset, y * 50 + self.y_offset))
                if c == "3":
                    screen.blit(pygame.image.load(f"images\\{self.levels[lvl][12]}"), (x * 50 + self.x_offset, y * 50 + self.y_offset))
                if c == "4" and len(self.levels[lvl]) <= 13:
                    screen.blit(pygame.image.load(f"images\\{self.levels[lvl][len(self.levels[lvl]) % 13 - 1]}"), (x * 50 + self.x_offset, y * 50 + self.y_offset))
                elif c == "4":
                    screen.blit(pygame.image.load(f"images\\{self.levels[lvl][13]}"), (x * 50 + self.x_offset, y * 50 + self.y_offset))
                if c == "5" and len(self.levels[lvl]) <= 14:
                    screen.blit(pygame.image.load(f"images\\{self.levels[lvl][len(self.levels[lvl]) % 14 - 1]}"), (x * 50 + self.x_offset, y * 50 + self.y_offset))
                elif c == "5":
                    screen.blit(pygame.image.load(f"images\\{self.levels[lvl][14]}"), (x * 50 + self.x_offset, y * 50 + self.y_offset))
                if c == "6" and len(self.levels[lvl]) <= 15:
                    screen.blit(pygame.image.load(f"images\\{self.levels[lvl][len(self.levels[lvl]) % 15 - 1]}"), (x * 50 + self.x_offset, y * 50 + self.y_offset))
                elif c == "6":
                    screen.blit(pygame.image.load(f"images\\{self.levels[lvl][15]}"), (x * 50 + self.x_offset, y * 50 + self.y_offset))
                if c == "7" and len(self.levels[lvl]) <= 16:
                    screen.blit(pygame.image.load(f"images\\{self.levels[lvl][len(self.levels[lvl]) % 16 - 1]}"), (x * 50 + self.x_offset, y * 50 + self.y_offset))
                elif c == "7":
                    screen.blit(pygame.image.load(f"images\\{self.levels[lvl][16]}"), (x * 50 + self.x_offset, y * 50 + self.y_offset))
                if c == "8" and len(self.levels[lvl]) <= 17:
                    screen.blit(pygame.image.load(f"images\\{self.levels[lvl][len(self.levels[lvl]) % 17 - 1]}"), (x * 50 + self.x_offset, y * 50 + self.y_offset))
                elif c == "8":
                    screen.blit(pygame.image.load(f"images\\{self.levels[lvl][17]}"), (x * 50 + self.x_offset, y * 50 + self.y_offset))
                if c == "9" and len(self.levels[lvl]) <= 18:
                    screen.blit(pygame.image.load(f"images\\{self.levels[lvl][len(self.levels[lvl]) % 18 - 1]}"), (x * 50 + self.x_offset, y * 50 + self.y_offset))
                elif c == "9":
                    screen.blit(pygame.image.load(f"images\\{self.levels[lvl][18]}"), (x * 50 + self.x_offset, y * 50 + self.y_offset))
                if c == "0" and len(self.levels[lvl]) <= 19:
                    screen.blit(pygame.image.load(f"images\\{self.levels[lvl][len(self.levels[lvl]) % 19 - 1]}"), (x * 50 + self.x_offset, y * 50 + self.y_offset))
                elif c == "0":
                    screen.blit(pygame.image.load(f"images\\{self.levels[lvl][19]}"), (x * 50 + self.x_offset, y * 50 + self.y_offset))
                if c == "f" and len(self.levels[lvl]) <= 20:
                    screen.blit(pygame.image.load(f"images\\{self.levels[lvl][len(self.levels[lvl]) % 20 - 1]}"), (x * 50 + self.x_offset, y * 50 + self.y_offset))
                elif c == "f":
                    screen.blit(pygame.image.load(f"images\\{self.levels[lvl][20]}"), (x * 50 + self.x_offset, y * 50 + self.y_offset))
                if c == "F" and len(self.levels[lvl]) <= 21:
                    screen.blit(pygame.image.load(f"images\\{self.levels[lvl][len(self.levels[lvl]) % 21 - 1]}"), (x * 50 + self.x_offset, y * 50 + self.y_offset))
                elif c == "F":
                    screen.blit(pygame.image.load(f"images\\{self.levels[lvl][21]}"), (x * 50 + self.x_offset, y * 50 + self.y_offset))
                if c == "*" and len(self.levels[lvl]) <= 22:
                    screen.blit(pygame.image.load(f"images\\{self.levels[lvl][len(self.levels[lvl]) % 22 - 1]}"), (x * 50 + self.x_offset, y * 50 + self.y_offset))
                elif c == "*":
                    screen.blit(pygame.image.load(f"images\\{self.levels[lvl][22]}"), (x * 50 + self.x_offset, y * 50 + self.y_offset))
                if c == "P":
                    screen.blit(pygame.image.load(f"images\\{self.levels[lvl][9]}"), (x * 50 + self.x_offset, y * 50 + self.y_offset))

                    # self.tiles.append(Tile(x * 50 + self.x_offset, y * 50 + self.y_offset, self.floor_tile))
                if c == "W":
                    screen.blit(pygame.image.load(f"images\\{self.levels[lvl][8]}"), (x * 50 + self.x_offset, y * 50 + self.y_offset))
                    # self.tiles.append(Tile(x * 50 + self.x_offset, y * 50 + self.y_offset, self.floor_tile))
 # self.tiles.append(Tile(x * 50 + self.x_offset, y * 50 + self.y_offset, self.floor_tile))

    def update(self, enemy_cnt, max_enemy, room_cnt, screen, width, height, enemys):
        if self.kills_cnt == max_enemy and len(enemys) == 0 and self.is_clear == False:
            self.is_clear = True
            self.location = self.location.replace('G', 'P')

        elif self.is_clear == False:
            self.location = self.location.replace('P', 'G')



'''
import pygame.image

from main_hero import Hero
from tiles import Tile
from enemy import Enemy


class Room:
    def __init__(self, location: str, start_x, start_y, portal_x, portal_y):
        self.location = location
        self.wall_tile = "wall.png"
        self.floor_tile = "floor.png"
        self.gates_tile = "gate.png"
        self.tiles = pygame.sprite.Group()
        self.start_x = start_x
        self.start_y = start_y
        self.portal_x = portal_x
        self.portal_y = portal_y

    def room_draw(self, screen, hero: Hero, enemies: list):
        loc = self.location.splitlines()
        for y, line in enumerate(loc):
            for x, c in enumerate(line):
                if c == "W":
                    screen.blit(pygame.image.load(f"images\\{self.wall_tile}"), (x * 50, y * 50))
                    self.tiles.add(Tile(x * 50, y * 50, self.wall_tile))
                elif c == "G":
                    screen.blit(pygame.image.load(f"images\\{self.gates_tile}"), (x * 50, y * 50))
                    self.tiles.add(Tile(x * 50, y * 50, self.gates_tile))
                elif c == " ":
                    screen.blit(pygame.image.load(f"images\\{self.floor_tile}"), (x * 50, y * 50))


def screen_fade(screen):
    overlay = pygame.Surface((600, 600))
    overlay.set_alpha(0)
    for _ in range(3000):
        screen.blit(overlay, (0, 0))
        overlay.set_alpha(1)
        pygame.display.flip()


def rooms_update(rooms, curr_level_index, curr_room_index, hero, screen, enemies):
    if curr_room_index != len(rooms[curr_level_index]) - 1:
        if pygame.Rect.colliderect(hero.rect,
                                   pygame.Rect(rooms[curr_level_index][curr_room_index].portal_x,
                                               rooms[curr_level_index][curr_room_index].portal_y, 50, 5)):
            curr_room_index += 1
            hero.x = rooms[curr_level_index][curr_room_index].start_x
            hero.y = rooms[curr_level_index][curr_room_index].start_y
            pygame.time.delay(150)
    else:
        if curr_level_index != len(rooms) - 1:
            if pygame.Rect.colliderect(hero.rect,
                                       pygame.Rect(rooms[curr_level_index][curr_room_index].portal_x,
                                                   rooms[curr_level_index][curr_room_index].portal_y, 50, 5)):
                curr_level_index += 1
                curr_room_index = 0
                hero.x = rooms[curr_level_index][curr_room_index].start_x
                hero.y = rooms[curr_level_index][curr_room_index].start_y
                screen_fade(screen)
                rooms[curr_level_index][curr_room_index].room_draw(screen, hero, enemies)
                pygame.time.delay(150)

    rooms[curr_level_index][curr_room_index].room_draw(screen, hero, enemies)
    return curr_level_index, curr_room_index


'''
