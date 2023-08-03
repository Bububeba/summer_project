import shelve
from map import *


class Save:
    def __init__(self, hero, curr_level_index, curr_room_index):
        self.file = shelve.open("progress")
        self.info = {
            'start_x': hero.x,
            'start_y': hero.y,
            'coins': hero.coins_score,
            'hp': hero.hp,
            'level': curr_level_index,
            'room': curr_room_index
        }

    def save_data(self):
        self.file['Info'] = self.info

    def update(self, hero, curr_level_index, curr_room_index):
        self.info = {
            'start_x': hero.x,
            'start_y': hero.y,
            'coins': hero.coins_score,
            'hp': hero.hp,
            'level': curr_level_index,
            'room': curr_room_index
        }

        self.save_data()

    def get_data(self):
        load_data = self.file['Info']
        return load_data['start_x'], load_data['start_y'], load_data['coins'], \
            load_data['hp'], load_data['level'], load_data['room']

    def __del__(self):
        self.file.close()
