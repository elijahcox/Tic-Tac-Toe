#pass

def print_board(move_list):
    pass

def usage():
    print("Welcome to impossible Tic Tac Toe!\nThe board is laid out as follows:")
    moves = [1,2,3,4,5,6,7,8,9]
    print_board(moves)
    print("To play, simply enter 1-9 corresponding to the cell that you want to play on.")

move_arr = [0]*9
usage()