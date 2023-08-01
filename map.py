import pygame.image

from main_hero import Hero
from tiles import Tile
from enemy import Enemy


class Room:
    def __init__(self, location: str, start_x, start_y, portal_x, portal_y):
        self.location = location
        self.wall_tile = "wall.png"
        self.water_tile = "water.png"
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


def rooms_update(rooms, curr_room_index, hero, screen, enemies):
    if curr_room_index != len(rooms) - 1:
        if pygame.Rect.colliderect(hero.rect,
                                   pygame.Rect(rooms[curr_room_index].portal_x, rooms[curr_room_index].portal_y, 50,  5)):

            curr_room_index += 1
            hero.x = rooms[curr_room_index].start_x
            hero.y = rooms[curr_room_index].start_y
            pygame.time.delay(150)
    rooms[curr_room_index].room_draw(screen, hero, enemies)
    return curr_room_index


'''
import pygame

from main_hero import Hero
from tiles import Tile
from enemy import Enemy


class Room:
    def __init__(self, location: str, width, height, count_of_tile_x, count_of_tile_y):
        self.location = location
        self.wall_tile = "wall.png"
        self.floor_tile = "floor.png"
        self.gates_tile = "gate.png"
        self.tiles = []
        self.screen_w = width
        self.screen_h = height
        self.room_w = count_of_tile_x * 50
        self.room_h = count_of_tile_y * 50
        self.x_offset = (self.screen_w - self.room_w) // 2
        self.y_offset = (self.screen_h - self.room_h) // 2


    def room_draw(self, screen, hero: Hero, enemies: list, width, height, count_of_tile_x, count_of_tile_y):
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
                if c == "F":
                    screen.blit(pygame.image.load(f"images\\{self.wall_tile}"), (x * 50 + self.x_offset, y * 50 + self.y_offset))
                    self.tiles.append(Tile(x * 50 + self.x_offset, y * 50 + self.y_offset, self.wall_tile))
                if c == " ":
                    screen.blit(pygame.image.load(f"images\\{self.floor_tile}"), (x * 50 + self.x_offset, y * 50 + self.y_offset))
                    self.tiles.append(Tile(x * 50 + self.x_offset, y * 50 + self.y_offset, self.wall_tile))

    def update(self, hero: Hero, enemies: list):
        if len(enemies) <= 0:
'''


