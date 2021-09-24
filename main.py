import random
from IPython.display import display
import chess
import chess.svg
import Environment as e
from PlayerRandom import PlayerRandom
from PlayerTaking import PlayerTaking


def play_a_thousand_games(player1, player2):
    whiteWins, blackWins, remis = 0, 0, 0
    moves = 0
    for j in range(0, 1000):
        for i in range(1, 10000):
            if e.board.outcome() is None:
                if e.board.turn == chess.WHITE:
                    e.board.push_san(player1.move(e.board.turn, list(e.board.legal_moves)))
                    moves += 1
                else:
                    e.board.push_san(player2.move(e.board.turn, list(e.board.legal_moves)))
                    moves += 1
            elif e.board.outcome().winner == chess.WHITE:
                whiteWins += 1
                # print("White won after", i, "moves")
                e.board.reset()
                break
            elif e.board.outcome().winner == chess.BLACK:
                blackWins += 1
                # print("Black won after", i, "moves")
                e.board.reset()
                break
            else:
                remis += 1
                # print("Remis after", i, "moves")
                e.board.reset()
                break

            # For Jupyter
            # display(chess.svg.board(board, size=350))
            # For Pycharm
            # print(calculate_score(board.turn))
            # print(e.board)
            # print("\n")
        print(whiteWins, blackWins, remis)
        print(moves / (whiteWins + blackWins + remis))


play_a_thousand_games(PlayerRandom(), PlayerTaking())
