import pygame


class Hero(pygame.sprite.Sprite):
    def __init__(self, x, y, filename, hp, speed, weapon, is_dead=False):
        pygame.sprite.Sprite.__init__(self)
        self.hp = hp
        self.speed = speed
        self.is_dead = is_dead
        self.coins = 0
        self.hero_weapon = weapon
        self.x = x
        self.y = y
        self.sprite = pygame.image.load(filename)
        self.rect = self.sprite.get_rect(center=(x, y))

    def update(self):
        pass

    def get_weapon(self):
        pass
