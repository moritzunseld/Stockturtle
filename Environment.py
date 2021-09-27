import random
from IPython.display import display
import chess
import chess.svg

board = chess.Board()


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


def calculate_position():
    score = 0
    for i in range(0, 64):
        piece = board.piece_at(chess.SQUARES[i])
        if piece is not None:
            if piece.color == chess.WHITE:
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
            else:
                if piece.piece_type == chess.PAWN:
                    score -= 1
                elif piece.piece_type == chess.KNIGHT:
                    score -= 3
                elif piece.piece_type == chess.BISHOP:
                    score -= 3
                elif piece.piece_type == chess.ROOK:
                    score -= 5
                elif piece.piece_type == chess.QUEEN:
                    score -= 9
    return score
