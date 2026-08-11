# x create the board
# x choose an initial player
# x until someone wins, check for a winner
#   show the board
#   choose location, mark it
#   toggle active player

# game over!, active player won

def main():
    # CREATE BOARD
    # Board is a list of rows
    # Rows are a list of cells
    board = [
        [None, None, None],
        [None, None, None],
        [None, None, None]
    ]


    # CHOOSE INITIAL PLAYER
    active_player_index = 0
    players = ["You", "computer"]
    symbols = ["X", "O"]

    # UNTIL SOMEONE WINS

    while not find_winner(board):
        # SHOW THE BOARD
        player = players[active_player_index]

        announce_turn(player)
        show_board(board)
        input("paused")

def show_board(board):
    for row in board:
        for cell in row:
            print(cell, end=" | ")
        print()


def announce_turn(player):
    print()
    print(f"It's {players} turn. Here is the board: ")
    print()
    show_board()


def find_winner(board):
    # TODO: Implement how we check for a winner  
    return False

if __name__ == ' main ':
    main()