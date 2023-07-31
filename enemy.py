# import pygame


# class Enemy(pygame.sprite.Sprite):
#     def __init__(self, x, y, filename, hp, damage, speed, attack_speed, group, is_dead = False ):
#         pygame.sprite.Sprite.__init__(self)
#         self.hp = hp
#         self.damage = damage
#         self.speed = speed
#         self.attack_speed = attack_speed
#         self.is_dead = is_dead
#         self.last_hit = 0
#         self.x = x
#         self.y = y
#         self.image = pygame.image.load(filename)
#         self.rect = self.image.get_rect(center = (x, y))
#         self.add(group)

#     def update(self, animcount, tdji, Main_Hero, time):

#         if self.hp <= 0:
#             self.kill()

#         else:
#             if Main_Hero.rect.colliderect(self.rect) and  (time - self.last_hit >= self.attack_speed * 1000):
#                 # print(time)
               
#                 Main_Hero.hp -= self.damage
#                 self.last_hit = time
#             self.rect = self.image.get_rect(center = (self.x, self.y))


import random

import pygame
import time

class Enemy(pygame.sprite.Sprite):
    def __init__(self, x, y, filename, hp, damage, speed, attack_speed, group, is_dead = False, is_see = False):
        pygame.sprite.Sprite.__init__(self)
        self.hp = hp
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
        self.rect = self.image.get_rect(center=(x, y))
        self.add(group)

    def update(self, Main_Hero, time): #animcount, tdji
        if ((Main_Hero.x - self.x) ** 2 + (Main_Hero.y - self.y) ** 2) ** 0.5 <= self.range:
            self.is_see = True
        else:
            self.is_see = False


        if self.hp <= 0:
            pass
            #self.kill()
        else:

            if self.rect.collidepoint((self.move_x, self.move_y)): 
                self.move_x = random.randrange(25, 575)
                self.move_y = random.randrange(25, 575)

            if self.is_see:
                self.move_to(Main_Hero.x, Main_Hero.y)
                print(Main_Hero.x, Main_Hero.y)
            else:
                self.move_to(self.move_x, self.move_y)

            if Main_Hero.rect.colliderect(self.rect) and  (time - self.last_hit >= self.attack_speed * 1000):
                # print(time)
               
                Main_Hero.hp -= self.damage
                self.last_hit = time
            self.rect = self.image.get_rect(center = (self.x, self.y))


            

    def attack(self):
        pass

    def move_to(self, Point_x, Point_y):
        
        if (self.x < Point_x):
            self.x += (1 * self.speed)
        else:
            self.x -= (1 * self.speed)

        
        if (self.y < Point_y):
            self.y += (1 * self.speed)
        else:
            self.y -= (1 * self.speed)

    # def patrol(self, PatrolPoints = []):
    #     r = random.randint(0, len(PatrolPoints) - 1)
    #     while self.x != PatrolPoints[r][0] and self.y != PatrolPoints[r][1]:
    #         if (self.x < PatrolPoints[r][0]):
    #             self.x += (1 * self.speed)
    #         else:
    #             self.x -= (1 * self.speed)
    #         if (self.y < PatrolPoints[r][1]):
    #             self.y += (1 * self.speed)
    #         else:
    #             self.y -= (1 * self.speed)
    #     time.sleep(5)


