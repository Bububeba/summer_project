import shelve


class Save:
    def __init__(self, hero, curr_level_index, curr_room_index, rooms_to_next_lvl):
        self.file = shelve.open("progress")
        self.info = {
            'start_x': hero.x,
            'start_y': hero.y,
            'coins': hero.coins_score,
            'max_hp': hero.max_hp,
            'hp': hero.hp,
            'speed': hero.speed,
            'level': curr_level_index,
            'room': curr_room_index,
            'need_rooms': rooms_to_next_lvl
        }

    def save_data(self):
        self.file['Info'] = self.info

    def update(self, hero, curr_level_index, curr_room_index, rooms_to_next_lvl):
        self.info = {
            'start_x': hero.x,
            'start_y': hero.y,
            'coins': hero.coins_score,
            'max_hp': hero.max_hp,
            'hp': hero.hp,
            'speed': hero.speed,
            'level': curr_level_index,
            'room': curr_room_index,
            'need_rooms': rooms_to_next_lvl
        }
        self.save_data()

    def get_data(self):
        load_data = self.file['Info']
        return load_data['start_x'], load_data['start_y'], load_data['coins'], \
            load_data['max_hp'], load_data['hp'], load_data['speed'], load_data['level'], load_data['room'],\
            load_data['need_rooms']

    def __del__(self):
        self.file.close()
