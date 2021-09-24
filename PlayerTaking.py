import random
import chess
import Environment


class PlayerTaking:
    def move(self, color, moves):
        score = 0
        best_score = Environment.calculate_score(not color)
        best_move = random.choice(moves)
        for move in moves:
            Environment.board.push_san(str(move))
            score = Environment.calculate_score(not color)
            if score < best_score:
                best_score = score
                best_move = move
            Environment.board.pop()
        return str(best_move)
