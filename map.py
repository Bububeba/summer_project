import pygame.image

from main_hero import Hero


# from enemy import Enemy


class Room:
    def __init__(self, location: str):
        self.location = location

    def room_draw(self, screen, tile, hero: Hero, enemies: list):
        loc = self.location.splitlines()
        for y, line in enumerate(loc):
            for x, c in enumerate(line):
                if c == "W":
                    screen.blit(tile, (x * 50, y * 50))

    def update(self, hero: Hero, enemies: list):
        pass


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

tile = pygame.image.load("images/wall.png")
size = (600, 600)
screen = pygame.display.set_mode(size)
room1 = Room(r1)
denis = Hero(456, 256, "sprites/coin_1.png", 100, 0, 0, None)
donbass = []
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    room1.room_draw(screen, tile, denis, donbass)
    pygame.display.update()
