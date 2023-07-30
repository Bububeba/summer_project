
import pygame
import random      

class Weapon(pygame.sprite.Sprite):
    def __init__(self, x, y, filename, name, damage, range,):
        pygame.sprite.Sprite.__init__(self)
        self.image   = pygame.image.load(filename).convert_alpha()
        self.rect    = self.image.get_rect(center = (x, y))
        self.damage  = damage
        self.name    = name
        self.range   = range
        self.x       = x
        self.y       = y  

    def hit(self, target, target_list, money_list):
        if target.distance_to_MainHero <= self.range :
            target.HP -= self.damage
            if  target.HP <= 0:
                # money_list.append(Coin(random.randint(1, 10) ))
                target_list.pop(target)


    def __str__(self):
        return (str(self.name) +
                "\nDamage:\t" + str(self.damage) +
                "\nRange :\t" + str(self.range ) +
                "\n")
    
    
 

# class Weapon:
    # def __init__(self, name, damage, range, sprites):
    #     self.damage = damage
    #     self.name = name
    #     self.range  = range 
    #     # self.sprites = sprites


    # def hit(self, target, target_list, money_list):
    #     if target.distance_to_MainHero <= self.range :
    #         target.HP -= self.damage
    #         if  target.HP <= 0:
    #             money_list.append(Coin(random.randint(1, 10) ))
    #             target_list.pop(target)


    # def __str__(self):
    #     return (str(self.name) +
    #             "\nDamage:\t" + str(self.damage) +
    #             "\nRange :\t" + str(self.range ) +
    #             "\n")
    


# icon_scythe = pygame.image.load("scythe.png").convert_alpha()
# scythe = Weapon("Sword", 5, 1, icon_scythe)


# # width, N = map(int,input().split())

# pygame.init()
# screen = pygame.display.set_mode()

# scythe = Weapon(100, 100, "scythe.png", "Scythe", 5, 100)

# print(scythe)

# # screen.fill(WHITE)
# # pygame.display.flip() 
# # running = True     



# screen.blit(scythe.image, scythe.rect)
# pygame.display.flip() 
# # clock = pygame.time.Clock()
# # FPS = 60

# # pygame.display.flip() 

# while 1:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             exit()
#     # clock.tick(FPS)

# pygame.quit()


