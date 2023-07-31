import pygame.image

from main_hero import Hero
from tiles import Tile
from enemy import Enemy


class Room:
    def __init__(self, location: str):
        self.location = location
        self.wall_tile = "wall.png"
        self.water_tile = "water.png"
        self.tiles = []

    def room_draw(self, screen, hero: Hero, enemies: list):
        loc = self.location.splitlines()
        for y, line in enumerate(loc):
            for x, c in enumerate(line):
                if c == "W":
                    screen.blit(pygame.image.load(f"images\\{self.wall_tile}"), (x * 50, y * 50))
                    self.tiles.append(Tile(x * 50, y * 50, self.wall_tile))


def rooms_update(rooms, curr_room_index, hero, screen, enemies):
    if 0 <= hero.x <= 600 and hero.y == 50:
        if curr_room_index != len(rooms) - 1:
            curr_room_index += 1
            hero.x = 300
            hero.y = 300
    rooms[curr_room_index].room_draw(screen, hero, enemies)



