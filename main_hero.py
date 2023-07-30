import pygame


class Hero(pygame.sprite.Sprite):
    def __init__(self, x, y, filename, hp, coins_score, speed, weapon, range, is_dead = False):
        pygame.sprite.Sprite.__init__(self)
        self.hp = hp
        self.coins_score = coins_score
        self.speed = speed
        self.is_dead = is_dead
        self.weapon = weapon
        self.range  = range 
        self.x = x
        self.y = y
        self.image = pygame.image.load(filename)
        self.rect = self.image.get_rect(center = (x, y))

    def update(self, animcount,
               move_right, move_left,
               flmove_up, flmove_down,
               flmove_left, flmove_right,
               fllast_move_is_right):

        if self.hp <= 0:
            self.kill()
            print("end")
        else:
            if flmove_down:
                if fllast_move_is_right:
                    self.image = move_right[animcount // 5]
                else:
                    self.image = move_left[animcount // 5]
                self.y += (1 * self.speed)

            if flmove_up:
                if fllast_move_is_right:
                    self.image = move_right[animcount // 5]
                else:
                    self.image = move_left[animcount // 5]

                self.y -= (1 * self.speed)
            

            if flmove_right:
                self.image = move_right[animcount // 5]
                self.x += (1 * self.speed)
              

            if flmove_left:
                self.image = move_left[animcount // 5]
                self.x -= (1 * self.speed)
        
            if not (flmove_down and flmove_up and flmove_left and flmove_right):
                if fllast_move_is_right:
                    self.image = move_right[animcount // 5]
                else:
                    self.image = move_left[animcount // 5]
              

            self.rect = self.image.get_rect(center=(self.x, self.y))

    def update_weapon(self, animcount,
                      fllast_move_is_right, weapon, image_weapon, range, image_range, image_range_hit, group):
        if fllast_move_is_right:
            weapon.rect.center = (self.rect.centerx + 30, self.rect.centery - 15)
            weapon.image = image_weapon
        else:
            weapon.rect.center = (self.rect.centerx - 60, self.rect.centery - 15)
            weapon.image = pygame.transform.flip(image_weapon, True, False)

        target_hit = self
        is_hit = False
        for item in group:
            if self.range.rect.collidepoint(item.rect.center):
                is_hit = True
                target_hit = item
                break

        if is_hit and (((self.rect.centerx - target_hit.rect.centerx) ** 2 + (self.rect.centery - target_hit.rect.centery) ** 2 ) ** 0.5) <= self.weapon.range:
            range.image = pygame.transform.scale(image_range_hit, (image_range_hit.get_width() * (self.weapon.range / 100) + animcount // 2, image_range_hit.get_height() * (self.weapon.range / 100) + animcount//2))
        else:
            range.image = pygame.transform.scale(image_range, (image_range.get_width() * (self.weapon.range / 100) + animcount // 2, image_range.get_height() * (self.weapon.range / 100) + animcount//2))
        # range.image = pygame.transform.scale(pygame.transform.rotate(image_range, animcount * 0.5), (image_range.get_width() * (self.weapon.range / 100), image_range.get_height() * (self.weapon.range / 100)))
        # range.image = pygame.transform.scale(image_range, (image_range.get_width() * (self.weapon.range / 100) - animcount // 2, image_range.get_height() * (self.weapon.range / 100) - animcount//2))

        # range.image = pygame.transform.scale(range_anim[animcount // 5], (range_anim[animcount // 5].get_width() * (self.weapon.range / 100), range_anim[animcount // 5].get_height() * (self.weapon.range / 100)))
        



        #  self.image = move_right[animcount // 5]
        range.rect = range.image.get_rect()       
        range.rect.center = (self.rect.centerx, self.rect.centery)
        

    def get_weapon(self):
        pass
