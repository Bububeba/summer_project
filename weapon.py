import pygame
from coin import *
import random


class Weapon(pygame.sprite.Sprite):
    def __init__(self, x, y, filename, name, damage, range):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(filename).convert_alpha()
        self.rect = self.image.get_rect(center=(x, y))
        self.damage = damage
        self.name = name
        self.range = range
        self.x = x
        self.y = y

    def hit(self, target, coins):
            print(target.hp)
            target.hp -= self.damage
            if target.hp <= 0:
                Coin(target.x, target.y, 'sprites\coin_1.png', coins)
                target.kill()


    def __str__(self):
        return (str(self.name) +
                "\nDamage:\t" + str(self.damage) +
                "\nRange :\t" + str(self.range) +
                "\n")


class Range(pygame.sprite.Sprite):
    def __init__(self, x, y, filename):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(filename).convert_alpha()
        self.rect = self.image.get_rect(center=(x, y))
        self.x = x
        self.y = y
