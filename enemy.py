
import random
import math
import pygame


class Enemy(pygame.sprite.Sprite):
    def __init__(self, x, y, filename, hp, damage, speed, attack_speed, group, is_dead = False, is_see = False):
        pygame.sprite.Sprite.__init__(self)
        self.hp = hp
        self.damage = damage
        self.speed = speed
        self.attack_speed = attack_speed
        self.last_hit = 0
        self.is_dead = is_dead
        self.is_see = is_see
        self.x = x
        self.y = y
        self.range = 100 #радиус видимости
        self.move_x = random.randrange(25, 575)
        self.move_y = random.randrange(25, 575)
        self.image = pygame.transform.scale(pygame.image.load(filename), (85, 95))
        self.rect = self.image.get_rect(center = (x, y))
        self.add(group)

    def update(self, Main_Hero, time): 
        
        if ((Main_Hero.x - self.x) ** 2 + (Main_Hero.y - self.y) ** 2) ** 0.5 <= self.range:
            self.is_see = True
        else:
            self.is_see = False


        if False:
            pass
            #self.kill()
        else:

            if self.rect.collidepoint((self.move_x, self.move_y)):
                self.move_x = random.randrange(25, 575)
                self.move_y = random.randrange(25, 575)

            if self.is_see:
                self.move_to(Main_Hero.x, Main_Hero.y)
                # print(Main_Hero.x, Main_Hero.y)
            else:
                self.move_to(self.move_x, self.move_y)

            if Main_Hero.rect.colliderect(self.rect) and  (time - self.last_hit >= self.attack_speed * 1000):
                Main_Hero.hp -= self.damage
                self.last_hit = time

            self.rect = self.image.get_rect(center = (self.x, self.y))


            

    def attack(self):
        pass

    def move_to(self, Point_x, Point_y):
        dx = Point_x - self.x
        dy = Point_y - self.y
        distance = math.hypot(dx, dy)

        if distance < self.speed: # Если объект достаточно близко к целевой точке, останавливаем его
            x = Point_x
            y = Point_y
        else: # Интерполируем координаты объекта для плавного движения
            self.x += dx / distance * self.speed
            self.y += dy / distance * self.speed

'''
import random

import pygame
import time
import math


class Enemy(pygame.sprite.Sprite):
    def __init__(self, x, y, filename, hp, damage, speed, attack_speed, group, is_dead=False, is_see=False):
        pygame.sprite.Sprite.__init__(self)
        self.hp = hp
        self.damage = damage
        self.speed = speed
        self.attack_speed = attack_speed
        self.last_hit = 0
        self.is_dead = is_dead
        self.is_see = is_see
        self.x = x
        self.y = y
        self.range = 100  # радиус видимости
        self.move_x = random.randrange(300, 550)
        self.move_y = random.randrange(300, 550)
        self.image = pygame.transform.scale(pygame.image.load(filename), (85, 95))
        self.rect = self.image.get_rect(center=(x, y))
        self.add(group)

    def update(self, Main_Hero, t, x1, x2, y1, y2):
        if ((Main_Hero.x - self.x) ** 2 + (Main_Hero.y - self.y) ** 2) ** 0.5 <= self.range:
            self.is_see = True

        if self.hp <= 0:
            self.kill()
        else:
            if self.rect.collidepoint((self.move_x, self.move_y)):
                self.move_x = random.randrange(x1, x2)
                self.move_y = random.randint(y1, y2)

            if self.is_see:
                self.move_to(Main_Hero.x, Main_Hero.y)
            else:
                self.move_to(self.move_x, self.move_y)

            if Main_Hero.rect.colliderect(self.rect) and (t - self.last_hit >= self.attack_speed * 1000):
                Main_Hero.hp -= self.damage
                #
                self.hp -= 100
                #
                self.last_hit = t

            self.rect = self.image.get_rect(center=(self.x, self.y))

    def attack(self):
        pass

    def move_to(self, Point_x, Point_y):
        dx = Point_x - self.x
        dy = Point_y - self.y
        distance = math.hypot(dx, dy)

        if distance < self.speed: # Если объект достаточно близко к целевой точке, останавливаем его
            self.x = Point_x
            self.y = Point_y
        else: # Интерполируем координаты объекта для плавного движения
            self.x += dx / distance * self.speed
            self.y += dy / distance * self.speed
'''

