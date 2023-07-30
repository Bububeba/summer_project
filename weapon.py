import pygame
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

    def hit(self, target, target_list, money_list):
        if target.distance_to_MainHero <= self.range:
            target.HP -= self.damage
            if target.HP <= 0:
                # money_list.append(Coin(random.randint(1, 10) ))
                target_list.pop(target)

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
