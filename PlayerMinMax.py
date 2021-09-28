import Environment as e


class PlayerMinMax:
    def __init__(self, depth):
        self.wanted_depth = depth

    best_move = None

    # todo: Repeating moves bug
    def min_max(self, color, depth, alpha, beta):
        if depth == 0 or not list(e.board.legal_moves):
            return e.calculate_position(color)
        max = alpha
        for move in list(e.board.legal_moves):
            e.board.push_san(str(move))
            value = - self.min_max(not color, depth - 1, -beta, -max)
            e.board.pop()
            if value > max:
                max = value
                if depth == self.wanted_depth:
                    self.best_move = move
                if max >= beta:
                    break
        return max

    def move(self, color, moves):
        score_beginning = e.calculate_position(color)
        score = self.min_max(color, self.wanted_depth, -1000, +1000)
        # print("By moving, the score changed by ", score - score_beginning)
        return str(self.best_move)
