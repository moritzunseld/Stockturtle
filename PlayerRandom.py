import random


class PlayerRandom:
    def move(self, color, moves):
        """Plays a random move."""

        return str(random.choice(moves))
