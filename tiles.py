import pygame.sprite


class Tile(pygame.sprite.Sprite):
    def __init__(self, x, y, filename):
        pygame.sprite.Sprite.__init__(self)
        self.x = x
        self.y = y
        self.image = pygame.image.load(f"images\\{filename}")
        self.rect = self.image.get_rect(topleft  = (x, y))

