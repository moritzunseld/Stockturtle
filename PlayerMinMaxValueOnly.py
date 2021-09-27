import random
import chess

import Environment as e


class PlayerMinMaxValueOnly:
    def __init__(self, depth):
        self.depth = depth

    best_move = None

    def max_it(self, d):
        if d == 0:
            return e.calculate_position()
        max = -1000
        for move in list(e.board.legal_moves):
            e.board.push_san(str(move))
            value = self.min_it(d - 1)
            e.board.pop()
            if value > max:
                max = value
                if d == self.depth:
                    self.best_move = move
        return max

    def min_it(self, d):
        if d == 0:
            return e.calculate_position()
        min = 1000
        for move in list(e.board.legal_moves):
            e.board.push_san(str(move))
            value = self.max_it(d - 1)
            e.board.pop()
            if value < min:
                min = value
            # Why no depth check?
        return min

    def move(self, color, moves):
        score_beginning = e.calculate_position()
        score = 0
        if color == chess.WHITE:
            score = self.max_it(self.depth)
            #print("Playing this move with score: ", score)
            #print("The baseline position had score: ", score_beginning)
            if score<score_beginning:
                # Why??
                print("Baseline score was higher!")
            if score > score_beginning:
                return str(self.best_move)
            else:
                return str(random.choice(list(e.board.legal_moves)))
        else:
            score = self.min_it(self.depth)
            if score < score_beginning:
                return str(self.best_move)
            else:
                return str(random.choice(list(e.board.legal_moves)))