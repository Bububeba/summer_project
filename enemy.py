import pygame


class Enemy(pygame.sprite.Sprite):
    def __init__(self, x, y, filename, hp, speed, is_dead = False):
        pygame.sprite.Sprite.__init__(self)
        self.hp = hp
        self.speed = speed
        self.is_dead = is_dead
        self.x = x
        self.y = y
        self.image = pygame.image.load(filename)
        self.rect = self.image.get_rect(center=(x, y))

    def update(self, animcount):

        if self.is_dead:
            print("end")
        else:
            self.rect = self.image.get_rect(center=(self.x, self.y))
