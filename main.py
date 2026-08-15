# x create the board
# x choose an initial player
# x until someone wins, check for a winner
# x show the board
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


        announce_turn(player, board)
        show_board(board)
        input("paused")

def show_board(board):
    for row in board:
        print("| ", end='')
        for cell in row:
            symbol = cell if cell is not None else "_"
            print(symbol, end=" | ")
        print()


def announce_turn(player, board):
    print()
    print(f"It's {player}'s turn. Here is the board: ")
    print()
    show_board(board)


def find_winner(board):
    # TODO: Implement how we check for a winner  
    return False

if __name__ == "__main__":
    main()