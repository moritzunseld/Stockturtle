import random
from IPython.display import display
import chess
import chess.svg

board = chess.Board()


for i in range(1, 1000):
    print("This is move", i)
    print("There are", board.legal_moves.count(), "legal moves.")
    board.push_san(str(random.choice(list(board.legal_moves))))

    # For Jupyter
    #display(chess.svg.board(board, size=350))
    # For Pycharm
    print(board)