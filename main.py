# x create the board
# x choose an initial player
# x until someone wins, check for a winner
# x show the board
# x  choose location, mark it
# x toggle active player

# x game over!, active player won



def main():
    print()
    print("Welcome to TIC TAC TOE from TALK PYTHON")
    print()

    # CREATE BOARD
    # Board is a list of rows
    # Rows are a list of cells
    board = [
        [None, None, None],
        [None, None, None],
        [None, None, None],
    ]


    # CHOOSE INITIAL PLAYER
    active_player_index = 0
    players = ["You", "computer"]
    symbols = ["X", "O"]
    player = players[active_player_index]

    # UNTIL SOMEONE WINS

    while not find_winner(board):
        # SHOW THE BOARD
        player = players[active_player_index]
        symbol = symbols[active_player_index]

        announce_turn(player)
        show_board(board)
        # input("paused")
        if not choose_location(board, symbol):
            print("That isn't an option, try again.")
            continue

        # TOGGLE ACTIVE PLAYER
        active_player_index = (active_player_index + 1) % len(players)

    print()
    print(f"Game over! {player} has won with the board: ")
    show_board(board)
    print()

def choose_location(board, symbol):
    row = int(input("Choose which row: ")) 
    column = int(input("Choose which column:  "))

    row -= 1
    column -= 1
    if row < 0 or row >= len(board):
        return False
    if column < 0 or column >= len(board[0]):
        return False

    cell = board[row][column]
    if cell is not None:
        return False

    board[row][column] = symbol
    return True

def show_board(board):
    for row in board:
        print("| ", end='')
        for cell in row:
            symbol = cell if cell is not None else "_"
            print(symbol, end=" | ")
        print()


def announce_turn(player):
    print()
    print(f"It's {player}'s turn. Here is the board: ")
    print()
    # show_board(board )


def find_winner(board):
    # TODO: Implement how we check for a winner  

    sequences = get_winning_sequences(board)

    for cells in sequences:
        symbol1 = cells[0]
        if symbol1 and all(symbol1 == cell for cell in cells):
            return True

    return False


def get_winning_sequences(board):
    sequences = []

    # Win by rows
    rows = board
    sequences.extend(rows)
    # for row in rows:
        # symbol1 = row[0]
        # if not symbol1:
        #     continue

        # for cell in row:
        #     if cell != symbol1:
        #         continue
 
        # return True

    # Win by columns
    # columns = []
    for col_idx in range(0, 3):
        col = [
            board[0][col_idx],
            board[1][col_idx],
            board[2][col_idx]
        ]
        sequences.append(col)
        
    # Win by diagonals
    diagonals = [
        [board[0][0], board[1][1], board[2][2]],
        [board[0][2], board[1][1], board[2][0]],
    ]
    sequences.extend(diagonals)

    return sequences


if __name__ == '__main__':
    main()