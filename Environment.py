import chess
import chess.svg

board = chess.Board()

white_pawn_square_values = [0, 0, 0, 0, 0, 0, 0, 0,
                            .1, .1, .1, .1, .1, .1, .1, .1,
                            .2, .2, .2, .2, .2, .2, .2, .2,
                            .3, .3, .3, .3, .3, .3, .3, .3,
                            .4, .4, .4, .4, .4, .4, .4, .4,
                            .5, .5, .5, .5, .5, .5, .5, .5,
                            .6, .6, .6, .6, .6, .6, .6, .6,
                            .7, .7, .7, .7, .7, .7, .7, .7]

white_knight_square_values = [0, 0, 0, 0, 0, 0, 0, 0,
                              0, .2, .2, .2, .2, .2, .2, 0,
                              0, .2, .4, .4, .4, .4, .2, 0,
                              0, .2, .4, .8, .8, .4, .2, 0,
                              0, .2, .4, .8, .8, .4, .2, 0,
                              0, .2, .4, .4, .4, .4, .2, 0,
                              0, .2, .2, .2, .2, .2, .2, 0,
                              0, 0, 0, 0, 0, 0, 0, 0]

white_bishop_square_values = [.6, .6, .6, .6, .6, .6, .6, .6,
                              .6, .4, .4, .4, .4, .4, .4, .6,
                              .6, .4, .2, .2, .2, .2, .4, .6,
                              .6, .4, .2, 0, 0, .2, .4, .6,
                              .6, .4, .2, 0, 0, .2, .4, .6,
                              .6, .4, .2, .2, .2, .2, .4, .6,
                              .6, .4, .4, .4, .4, .4, .4, .6,
                              .6, .6, .6, .6, .6, .6, .6, .6]

white_rook_square_values = white_bishop_square_values

white_queen_square_values = white_knight_square_values


def calculate_score(color):
    score = 0
    for i in range(0, 64):
        piece = board.piece_at(chess.SQUARES[i])
        if piece is not None:
            if piece.color == color:
                if piece.piece_type == chess.PAWN:
                    score += 1
                elif piece.piece_type == chess.KNIGHT:
                    score += 3
                elif piece.piece_type == chess.BISHOP:
                    score += 3
                elif piece.piece_type == chess.ROOK:
                    score += 5
                elif piece.piece_type == chess.QUEEN:
                    score += 9
    return score


def calculate_position(color):
    score = 0
    if board.outcome() is not None and board.outcome().result() == "1/2-1/2":
        return 0
    elif board.outcome() is not None and board.outcome().winner == color:
        return 1000
    elif board.outcome() is not None and board.outcome().winner == (not color):
        return -1000
    if color == chess.WHITE:
        for i in range(0, 64):
            piece = board.piece_at(chess.SQUARES[i])
            if piece is not None:
                if piece.color == chess.WHITE:
                    if piece.piece_type == chess.PAWN:
                        score += 1
                        score += white_pawn_square_values[i]
                    elif piece.piece_type == chess.KNIGHT:
                        score += 3
                        score += white_knight_square_values[i]
                    elif piece.piece_type == chess.BISHOP:
                        score += 3
                        score += white_bishop_square_values[i]
                    elif piece.piece_type == chess.ROOK:
                        score += 5
                        score += white_rook_square_values[i]
                    elif piece.piece_type == chess.QUEEN:
                        score += 9
                        score += white_queen_square_values[i]
                else:
                    if piece.piece_type == chess.PAWN:
                        score -= 1
                        score -= list(reversed(white_pawn_square_values))[i]
                    elif piece.piece_type == chess.KNIGHT:
                        score -= 3
                        score -= white_knight_square_values[i]
                    elif piece.piece_type == chess.BISHOP:
                        score -= 3
                        score -= white_bishop_square_values[i]
                    elif piece.piece_type == chess.ROOK:
                        score -= 5
                        score -= white_rook_square_values[i]
                    elif piece.piece_type == chess.QUEEN:
                        score -= 9
                        score -= white_queen_square_values[i]
    else:
        for i in range(0, 64):
            piece = board.piece_at(chess.SQUARES[i])
            if piece is not None:
                if piece.color == chess.WHITE:
                    if piece.piece_type == chess.PAWN:
                        score -= 1
                        score -= white_pawn_square_values[i]
                    elif piece.piece_type == chess.KNIGHT:
                        score -= 3
                        score -= white_knight_square_values[i]
                    elif piece.piece_type == chess.BISHOP:
                        score -= 3
                        score -= white_bishop_square_values[i]
                    elif piece.piece_type == chess.ROOK:
                        score -= 5
                        score -= white_rook_square_values[i]
                    elif piece.piece_type == chess.QUEEN:
                        score -= 9
                        score -= white_queen_square_values[i]
                else:
                    if piece.piece_type == chess.PAWN:
                        score += 1
                        score += list(reversed(white_pawn_square_values))[i]
                    elif piece.piece_type == chess.KNIGHT:
                        score += 3
                        score += white_knight_square_values[i]
                    elif piece.piece_type == chess.BISHOP:
                        score += 3
                        score += white_bishop_square_values[i]
                    elif piece.piece_type == chess.ROOK:
                        score += 5
                        score += white_rook_square_values[i]
                    elif piece.piece_type == chess.QUEEN:
                        score += 9
                        score += white_queen_square_values[i]
    return score
