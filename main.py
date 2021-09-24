import collections
import random
from IPython.display import display
import chess
import chess.svg
import Environment as e
import chess.pgn
from PlayerRandom import PlayerRandom
from PlayerTaking import PlayerTaking

# from https://github.com/niklasf/python-chess/issues/63
def board_to_game(board):
    game = chess.pgn.Game()

    # Undo all moves.
    switchyard = collections.deque()
    while board.move_stack:
        switchyard.append(board.pop())

    game.setup(board)
    node = game

    # Replay all moves.
    while switchyard:
        move = switchyard.pop()
        node = node.add_variation(move)
        board.push(move)

    game.headers["Result"] = board.result()
    return game

def play_a_thousand_games(player1, player2):
    whiteWins, blackWins, remis = 0, 0, 0
    moves = 0
    for j in range(0, 1000):
        for i in range(1, 10000):
            if e.board.outcome() is None:
                if e.board.turn == chess.WHITE:
                    move_san = player1.move(e.board.turn, list(e.board.legal_moves))
                    e.board.push_san(move_san)
                    moves += 1
                else:
                    move_san = player2.move(e.board.turn, list(e.board.legal_moves))
                    e.board.push_san(move_san)
                    moves += 1
            elif e.board.outcome().winner == chess.WHITE:
                whiteWins += 1
                # print("White won after", i, "moves")
                print(board_to_game(e.board))
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


play_a_thousand_games(PlayerTaking(), PlayerTaking())
