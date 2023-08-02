import random
import pygame
import math


class Enemy(pygame.sprite.Sprite):
    def __init__(self, x, y, filename, hp, damage, speed, attack_speed, group, room, is_see=False):
        pygame.sprite.Sprite.__init__(self)
        self.hp = hp
        self.damage = damage
        self.speed = speed
        self.attack_speed = attack_speed
        self.last_hit = 0
        #
        self.is_see = is_see
        self.x = x
        self.y = y
        self.range = 100  
        self.move_x = random.randrange(300, 550)
        self.move_y = random.randrange(300, 550)
        self.image = pygame.image.load(filename)
        self.rect = self.image.get_rect(center = (x, y))
        self.room = room
        self.add(group)

    def update(self, animcount, enemy_anim, Main_Hero, current_time, room):

        if self.hp <= 0:
            # print("KILL")
            room.kills_cnt += 1
            # print( room.kills_cnt)
            self.kill()

        else:

            self.image = enemy_anim[animcount // 5]

            if ((Main_Hero.x - self.x) ** 2 + (Main_Hero.y - self.y) ** 2) ** 0.5 <= self.range:
                self.is_see = True

            if self.rect.collidepoint((self.move_x, self.move_y)):
                self.move_x = random.randint(1000//2 - self.room.room_w // 2 + 50, 1000//2 + self.room.room_w // 2 - 50)
                self.move_y = random.randint( 800//2 - self.room.room_h // 2 + 50,  800//2 + self.room.room_h // 2 - 50)

            if self.is_see:
                self.move_to(Main_Hero.x, Main_Hero.y)
            else:
                self.move_to(self.move_x, self.move_y)

            if Main_Hero.rect.colliderect(self.rect) and (current_time - self.last_hit >= self.attack_speed * 1000):
                Main_Hero.hp -= self.damage
                self.last_hit = current_time

            self.rect = self.image.get_rect(center=(self.x, self.y))


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




class Cross(pygame.sprite.Sprite):
    def __init__(self, x, y, filename, time_create, group):
        pygame.sprite.Sprite.__init__(self)
        self.x = x
        self.y = y
        self.time_create = time_create
        self.image = pygame.image.load(filename)
        self.rect = self.image.get_rect(center = (x, y))
        self.add(group)

    def update(self, animcount, cross_anim, current_time, enemys, room, hp, damage, speed):
        self.image = cross_anim[animcount // 5]
        if current_time - self.time_create >= 2000:
            self.kill()
            Enemy(self.x, self.y, 'sprites\enemy_1.png', 
                hp, damage, speed, 1, enemys,  room)
        
        