import random
from IPython.display import display
import chess
import chess.svg

board = chess.Board()

# "r" = random, "t" = take
mode = "t"


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


def choose_taking_move(color, moves):
    score = 0
    best_score = calculate_score(not color)
    best_move = random.choice(moves)
    for move in moves:
        board.push_san(str(move))
        score = calculate_score(not color)
        if score < best_score:
            best_score = score
            best_move = move
        board.pop()
    return best_move


if mode == "r":
    for i in range(1, 1000):
        print("This is move", i)
        print("There are", board.legal_moves.count(), "legal moves.")
        board.push_san(str(random.choice(list(board.legal_moves))))

        # For Jupyter
        # display(chess.svg.board(board, size=350))
        # For Pycharm
        print(calculate_score(board.turn))
        print(board)

if mode == "t":
    whiteWins, blackWins, remis = 0, 0, 0
    for i in range(1, 1000):
        if board.outcome() is None:
            print("This is move", i)
            print("There are", board.legal_moves.count(), "legal moves.")
            board.push_san(str(choose_taking_move(board.turn, list(board.legal_moves))))
        elif board.outcome().winner == chess.WHITE:
            whiteWins += 1
            break
        elif board.outcome().winner == chess.BLACK:
            blackWins += 1
            break
        else:
            remis += 1
            break

        # For Jupyter
        # display(chess.svg.board(board, size=350))
        # For Pycharm
        # print(calculate_score(board.turn))
        print(board)
    print(whiteWins, blackWins, remis)
