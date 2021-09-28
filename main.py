import collections
import chess
import chess.svg
import Environment as e
import chess.pgn

import random
from PlayerMinMax import PlayerMinMax
from PlayerRandom import PlayerRandom
from PlayerTaking import PlayerTaking


# adjusted from https://github.com/niklasf/python-chess/issues/63
def print_game():
    game = chess.pgn.Game()

    # Undo all moves.
    switchyard = collections.deque()
    while e.board.move_stack:
        switchyard.append(e.board.pop())

    game.setup(e.board)
    node = game

    # Replay all moves.
    while switchyard:
        move = switchyard.pop()
        node = node.add_variation(move)
        e.board.push(move)

    game.headers["Result"] = e.board.result()
    print(game)


def play_games(player1, player2, num=1000):
    white_wins, black_wins, remis = 0, 0, 0
    moves = 0
    for j in range(0, num):
        for i in range(1, 10000):
            if e.board.outcome() is None:
                if e.board.turn == chess.WHITE:
                    # Random first move to avoid same games vs same enemy
                    if i == 1:
                        move_san = str(random.choice(list(e.board.legal_moves)))
                    else:
                        move_san = player1.move(chess.WHITE, list(e.board.legal_moves))
                    e.board.push_san(move_san)
                    # print("White played ", move_san)
                    moves += 1
                else:
                    # Random first move to avoid same games vs same enemy
                    if i == 2:
                        move_san = str(random.choice(list(e.board.legal_moves)))

                    else:
                        move_san = player2.move(chess.BLACK, list(e.board.legal_moves))
                    e.board.push_san(move_san)
                    # print("Black played ", move_san)
                    moves += 1
            elif e.board.outcome().winner == chess.WHITE:
                white_wins += 1
                print_game()
                e.board.reset()
                break
            elif e.board.outcome().winner == chess.BLACK:
                black_wins += 1
                print_game()
                e.board.reset()
                break
            else:
                remis += 1
                print_game()
                e.board.reset()
                break
        print(white_wins, remis, black_wins)
        print(moves / (white_wins + black_wins + remis))


play_games(PlayerMinMax(3), PlayerRandom())
