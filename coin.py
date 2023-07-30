import pygame
import random


class Coin(pygame.sprite.Sprite):
    def __init__(self, x, y, filename, group):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(filename).convert_alpha()
        self.rect  = self.image.get_rect(center = (x, y))
        self.x     = x
        self.y     = y
        self.value = random.randint(1, 3)
        self.add(group)

    def update(self, animcount, coin_anim, Main_Hero):  
       
        if Main_Hero.rect.collidepoint(self.rect.center):
            Main_Hero.coins_score += self.value
            # print("->" , coins_score, "->"  , end = " ")
            self.kill()
        else: #если нет коллизии с главным героем'''
            # print("-> " , animcount)
            self.image = coin_anim[animcount // 5]
            # self.rect = self.image.get_rect()

        
           

 
        