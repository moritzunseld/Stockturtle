import collections
import chess
import chess.svg
import Environment as e
import chess.pgn
import random

import time
import yaml

import json

from Lichess import Lichess
from PlayerMinMax import PlayerMinMax
from PlayerRandom import PlayerRandom
from PlayerTaking import PlayerTaking


def play_games(player1, player2, num=1000):
    """Simulate num amount of games between two player agent classes."""

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


def play_game_on_lichess(player, challenge_id):
    """Accept and play a lichess challenge using the player class that should be playing and the challenge_id."""

    # In case loaded_response gets accessed before being assigned
    global loaded_response
    with open('config.yml', 'r') as f:
        token = yaml.load(f)["token"]
        url = "https://lichess.org/"
    lichess = Lichess(token, url, "v1")
    lichess.accept_challenge(challenge_id)
    while True:
        if e.board.turn == chess.WHITE:
            move = str(player.move(chess.WHITE, list(e.board.legal_moves)))
            lichess.make_move(challenge_id, move)
            e.board.push_san(move)

            # Wait a second to catch edge cases in the endless loop (maybe not needed)
            time.sleep(1)
        else:
            response = lichess.get_game_stream(challenge_id)
            lines = response.iter_lines()

            # The Lichess stream sometimes throws a JSONDecodeError. Catch it and resume the game.
            try:
                loaded_response = json.loads(next(lines).decode('utf-8'))
            except json.decoder.JSONDecodeError:
                print("JSON Decode Error!")

            moves = loaded_response["state"]["moves"]
            move = moves.split()[-1]

            # Check if the last move is legal to play in this situation (maybe not needed)
            if chess.Move.from_uci(move) in e.board.generate_legal_moves():
                e.board.push_san(move)

                # Send evaluation of the position into the chat
                if e.calculate_position(chess.WHITE) > 0:
                    message = "I think that my position is " + str(round(e.calculate_position(chess.WHITE), 1)) +\
                              " point(s) better than yours! "
                else:
                    message = "I think that your position is " + str(round(e.calculate_position(chess.BLACK), 1)) +\
                              " point(s) better than mine!"
                lichess.chat(challenge_id, "player", message)

            # Wait a second until checking again if the enemy has moved because or rate-limitation.
            time.sleep(1)


# adjusted from https://github.com/niklasf/python-chess/issues/63
def print_game():
    """Prints the played game as PGN format."""

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


# play_games(PlayerMinMax(2), PlayerRandom())
# play_game_on_lichess(PlayerMinMax(4), "sIKG94n7")
