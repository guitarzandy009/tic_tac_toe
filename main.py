# create the board
# choose an initial player
# until someone wins, check for a winner
#   show the board
#   choose location, mark it
#   toggle active player

# game over!, active player won

def main():
    # Board is a list of rows
    # Rows are a list of cells
    board = [
        [None, None, None],
        [None, None, None],
        [None, None, None]
    ]
    # board.get("1,2")
    # board[2]

    # board = {
    #     "0,0": None,
    #     "0,1": None,
    #     "0,2": None,
    #     "1,0": None,
    #     "2,0": None,

    # }

    board = [
        [cell1, cell2, cell3],
        [r2_c1, r2_c2, r2_c3],
        [r3_c1, r3_c2, r3_c3]
    ]

if __name__ == ' main ':
    main()