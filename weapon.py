import pygame
from coin import *
import random


class Weapon(pygame.sprite.Sprite):
    def __init__(self, x, y, filename, name, damage, range, attack_speed):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(filename).convert_alpha()
        self.rect = self.image.get_rect(center=(x, y))
        self.damage = damage
        self.name = name
        self.range = range
        self.attack_speed = attack_speed
        self.last_attack = 0
        self.x = x
        self.y = y
        self.anim_count = 0

    def hit(self, targets, cur_time):
        if cur_time - self.last_attack >= self.attack_speed * 1000:
            for item in targets:
                item.hp -= self.damage
                item.last_attacked = cur_time
            self.last_attack = cur_time
            


    def __str__(self):
        return (str(self.name)+
                "\nDamage:\t" + str(self.damage) +
                "\nRange :\t" + str(self.range)  +
                "\n")


class Range(pygame.sprite.Sprite):
    def __init__(self, x, y, filename):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(filename).convert_alpha()
        self.rect = self.image.get_rect(center=(x, y))
        self.x = x
        self.y = y