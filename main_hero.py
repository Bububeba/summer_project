import pygame


class Hero(pygame.sprite.Sprite):
    def __init__(self, x, y, filename, hp, coins_score, speed, weapon, is_dead=False):
        pygame.sprite.Sprite.__init__(self)
        self.hp = hp
        self.coins_score = coins_score
        self.speed = speed
        self.is_dead = is_dead
        self.weapon = weapon
        self.x = x
        self.y = y
        self.sprite = pygame.image.load(filename)
        self.rect = self.sprite.get_rect(center=(x, y))

    def update(self, animcount,
               move_right, move_left,
               flmove_up, flmove_down,
               flmove_left, flmove_right,
               fllast_move_is_right):

        if self.is_dead:
            print("end")
        else:

            if flmove_down:
                if fllast_move_is_right:
                    self.image = move_right[animcount // 5]
                else:
                    self.image = move_left[animcount // 5]
                self.y += (1 * self.speed)
                # animcount += 1

            if flmove_up:
                if fllast_move_is_right:
                    self.image = move_right[animcount // 5]
                else:
                    self.image = move_left[animcount // 5]

                self.y -= (1 * self.speed)
                # animcount += 1

            if flmove_right:
                self.image = move_right[animcount // 5]
                self.x += (1 * self.speed)
                # animcount += 1

            if flmove_left:
                self.image = move_left[animcount // 5]
                self.x -= (1 * self.speed)
                # animcount += 1

            if not (flmove_down and flmove_up and flmove_left and flmove_right):
                if fllast_move_is_right:
                    self.image = move_right[animcount // 5]
                else:
                    self.image = move_left[animcount // 5]
                # animcount += 1

            self.rect = self.image.get_rect(center=(self.x, self.y))

    def update_weapon(self, animcount,
                      fllast_move_is_right, weapon, image_weapon):
        if fllast_move_is_right:
            weapon.rect.center = (self.rect.centerx + 30, self.rect.centery - 15)
            weapon.image = image_weapon
        else:
            weapon.rect.center = (self.rect.centerx - 60, self.rect.centery - 15)
            weapon.image = pygame.transform.flip(image_weapon, True, False)

    def get_weapon(self):
        pass
