import pygame



class Hero(pygame.sprite.Sprite):
    def __init__(self, x, y, filename, hp, coins_score, speed, weapon = None, range = None):
        pygame.sprite.Sprite.__init__(self)
        self.hp = hp
        self.max_hp = hp
        self.coins_score = coins_score
        self.speed = speed
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
               fllast_move_is_right, room):

        if ():
            pass
            # self.kill()
            # print("end")
        else:
            if flmove_down:
                if fllast_move_is_right:
                    self.image = move_right[animcount // 5]
                else:
                    self.image = move_left[animcount // 5]

                self.y += (1 * self.speed)
                self.rect = self.image.get_rect(center = (self.x, self.y))
                # self.rect.centery += (1 * self.speed)

                if (pygame.Rect.collidelist(self.rect, [i.rect for i in room.tiles]) != -1) or pygame.Rect.collidelist(self.rect, [i.rect for i in room.gates]) != -1:
                    self.y -= (1 * self.speed)
                    self.rect.centery -= (1 * self.speed)


                  
            if flmove_up:
                if fllast_move_is_right:
                    self.image = move_right[animcount // 5]
                else:
                    self.image = move_left[animcount // 5]

                self.y -= (1 * self.speed)
                self.rect.centery -= (1 * self.speed)
                if pygame.Rect.collidelist(self.rect, [i.rect for i in room.tiles]) != -1 or pygame.Rect.collidelist(self.rect, [i.rect for i in room.gates]) != -1:
                    self.y += (1 * self.speed)
                    self.rect.centery += (1 * self.speed)
                    
            

            if flmove_right:
                self.image = move_right[animcount // 5]
                
                self.x += (1 * self.speed)
                self.rect.centerx += (1 * self.speed)
                
                if pygame.Rect.collidelist(self.rect, [i.rect for i in room.tiles]) != -1 or pygame.Rect.collidelist(self.rect, [i.rect for i in room.gates]) != -1:
                    self.x -= (1 * self.speed)
                    self.rect.centerx -= (1 * self.speed)
              

            if flmove_left:
                self.image = move_left[animcount // 5]

                self.x -= (1 * self.speed)
                self.rect.centerx -= (1 * self.speed)

                if pygame.Rect.collidelist(self.rect, [i.rect for i in room.tiles]) != -1 or pygame.Rect.collidelist(self.rect, [i.rect for i in room.gates]) != -1:
                    self.x += (1 * self.speed)
                    self.rect.centerx += (1 * self.speed)
        
            if not (flmove_down and flmove_up and flmove_left and flmove_right):
                if fllast_move_is_right:
                    self.image = move_right[animcount // 5]
                else:
                    self.image = move_left[animcount // 5]
              

            self.rect = self.image.get_rect(center = (self.x, self.y))

    def update_weapon(self, animcount,
                      fllast_move_is_right, weapon, image_weapon, range, image_range, image_range_hit, group, coins, cur_time):
        if fllast_move_is_right:
            weapon.rect.center = (self.rect.centerx + 30, self.rect.centery - 15)
            weapon.image = image_weapon
        else:
            weapon.rect.center = (self.rect.centerx - 60, self.rect.centery - 15)
            weapon.image = pygame.transform.flip(image_weapon, True, False)

        # target_hit = self
        is_hit = False
        targets_hit = pygame.sprite.Group()
        for item in group:
            if (((self.rect.centerx - item.rect.centerx) ** 2 + (self.rect.centery - item.rect.centery) ** 2 ) ** 0.5) <= self.weapon.range / 2:
                is_hit = True
                targets_hit.add(item)
        # print(targets_hit)
        if is_hit:
            range.image = pygame.transform.scale(image_range_hit, (image_range_hit.get_width() * (self.weapon.range / 100) + animcount // 2, image_range_hit.get_height() * (self.weapon.range / 100) + animcount//2))
            self.weapon.hit(targets_hit, cur_time)
        else:
            range.image = pygame.transform.scale(image_range, (image_range.get_width() * (self.weapon.range / 100) + animcount // 2, image_range.get_height() * (self.weapon.range / 100) + animcount//2))
        targets_hit.empty()
        # print(targets_hit)
        # range.image = pygame.transform.scale(pygame.transform.rotate(image_range, animcount * 0.5), (image_range.get_width() * (self.weapon.range / 100), image_range.get_height() * (self.weapon.range / 100)))
        # range.image = pygame.transform.scale(image_range, (image_range.get_width() * (self.weapon.range / 100) - animcount // 2, image_range.get_height() * (self.weapon.range / 100) - animcount//2))

        # range.image = pygame.transform.scale(range_anim[animcount // 5], (range_anim[animcount // 5].get_width() * (self.weapon.range / 100), range_anim[animcount // 5].get_height() * (self.weapon.range / 100)))
        



        #  self.image = move_right[animcount // 5]
        range.rect = range.image.get_rect()       
        range.rect.center = (self.rect.centerx, self.rect.centery)
        

    def get_weapon(self):
        pass