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

    def update(self, hero: Hero, enemies: list):
        pass


