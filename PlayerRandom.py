import random


class PlayerRandom:
    def move(self, color, moves):
        return str(random.choice(moves))
