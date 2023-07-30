import pygame


class Enemy(pygame.sprite.Sprite):
    def __init__(self, x, y, filename, hp, damage, speed, group, is_dead = False ):
        pygame.sprite.Sprite.__init__(self)
        self.hp = hp
        self.damage = damage
        self.speed = speed
        self.is_dead = is_dead
        self.x = x
        self.y = y
        self.image = pygame.image.load(filename)
        self.rect = self.image.get_rect(center = (x, y))
        self.add(group)

    def update(self, animcount, tdji, Main_Hero):

        if self.hp <= 0:
            self.kill()
        else:
            if Main_Hero.rect.colliderect(self.rect):
                Main_Hero.hp -= self.damage
            self.rect = self.image.get_rect(center = (self.x, self.y))
