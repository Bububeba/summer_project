import pygame

from main_hero import Hero
from tiles import Tile
from enemy import Enemy


class Room:
    def __init__(self, location: str, width, height, 
                portal1_x: int, portal1_y: int, portal2_x: int, portal2_y: int,
                portal3_x: int, portal3_y: int, portal4_x: int, portal4_y: int,
                count_of_tile_x, count_of_tile_y, kills_cnt = 0, is_clear = False):
                    #1 - up, 2 - right, 3 - down, 4 - left
        self.location = location
        self.wall_tile = "wall.png"
        self.floor_tile = "floor.png"
        self.gates_tile = "gate.png"
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
        self.kills_cnt = kills_cnt
        self.is_clear = is_clear
        if portal1_x != -1:
            self.rect1 = pygame.Rect(self.portal1_x, self.portal1_y, 50, 50)
        if portal2_x != -1:
            self.rect2 = pygame.Rect(self.portal2_x, self.portal2_y, 50, 50)
        if portal3_x != -1:
            self.rect3 = pygame.Rect(self.portal3_x, self.portal3_y, 50, 50)
        if portal4_x != -1:
            self.rect4 = pygame.Rect(self.portal4_x, self.portal4_y, 50, 50)


    def room_draw(self, screen, width, height, count_of_tile_x, count_of_tile_y):
        loc = self.location.splitlines()
        self.screen_w = width
        self.screen_h = height
        self.room_w = count_of_tile_x * 50
        self.room_h = count_of_tile_y * 50
        self.x_offset = (self.screen_w - self.room_w) // 2
        self.y_offset = (self.screen_h - self.room_h) // 2
        for y, line in enumerate(loc):
            for x, c in enumerate(line):
                if c == "W":
                    screen.blit(pygame.image.load(f"images\\{self.wall_tile}"), (x * 50 + self.x_offset, y * 50 + self.y_offset))
                    self.tiles.append(Tile(x * 50 + self.x_offset, y * 50 + self.y_offset, self.wall_tile))
                if c == "G":
                    screen.blit(pygame.image.load(f"images\\{self.gates_tile}"), (x * 50 + self.x_offset, y * 50 + self.y_offset))
                    self.gates.append(Tile(x * 50 + self.x_offset, y * 50 + self.y_offset, self.gates_tile))
                if c == " ":
                    screen.blit(pygame.image.load(f"images\\{self.floor_tile}"), (x * 50 + self.x_offset, y * 50 + self.y_offset))
                    # self.tiles.append(Tile(x * 50 + self.x_offset, y * 50 + self.y_offset, self.floor_tile))
                if c == "P":
                    screen.blit(pygame.image.load(f"images\\{self.floor_tile}"), (x * 50 + self.x_offset, y * 50 + self.y_offset))
                    # self.tiles.append(Tile(x * 50 + self.x_offset, y * 50 + self.y_offset, self.floor_tile))

    def update(self, enemy_cnt, max_enemy, room_cnt, screen, width, height, enemys):
        # print(self.kills_cnt, max_enemy)
        if self.kills_cnt == max_enemy and len(enemys) == 0 and self.is_clear == False:
            # print (" -> ", enemy_cnt, len(enemys))
            # print('idi nahui')
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
