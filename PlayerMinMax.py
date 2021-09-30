import Environment as e


class PlayerMinMax:
    def __init__(self, depth):
        self.wanted_depth = depth

    best_move = None

    # todo: Repeating moves "bug"
    def min_max(self, color, depth, alpha, beta):
        """MinMax algorithm for finding the best move within a given depth."""

        # Return the position's score if depth has been reached
        if depth == 0 or not list(e.board.legal_moves):
            return e.calculate_position(color)
        max = alpha

        # Iterate through all possible moves until depth is reached
        for move in list(e.board.legal_moves):
            e.board.push_san(str(move))
            value = - self.min_max(not color, depth - 1, -beta, -max)
            e.board.pop()
            if value > max:
                max = value

                # If the move is better than the best (until now) and depth has been reached, set new best move
                if depth == self.wanted_depth:
                    self.best_move = move

                # Break the loop to save resources if the current branch is worse than the max score until now
                if max >= beta:
                    break
        return max

    def move(self, color, moves):
        """Uses the MinMax algorithm to play a move with color."""

        score_beginning = e.calculate_position(color)
        score = self.min_max(color, self.wanted_depth, -1000, +1000)
        print("By moving, the score changed by ", score - score_beginning)
        return str(self.best_move)
