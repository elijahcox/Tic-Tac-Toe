#pass

def print_board(move_list = [1,2,3,4,5,6,7,8,9]):
    pass

def usage():
    print("Welcome to impossible Tic Tac Toe!\nThe board is laid out as follows:")
    print_board()
    print("To play, simply enter 1-9 corresponding to the cell that you want to play on.")

move_arr = [0]*9
move_order = ""
cur_move = -1
valid_move = False
usage()

while move_order.upper() != 'X' and move_order.upper() != 'O':
    move_order = str(input("Enter X to play first, O to play second. Enter Q to quit. Choice: "))
    if move_order.upper() == 'Q':
        exit()

#if move order is O, make initial computer move
#else get user input

#move input logic
while True:
    while not valid_move:
        try:
            cur_move = str(input("Enter a move[1-9] or Q to quit: "))
            if cur_move.upper() == 'Q':
                exit()
            else:
                cur_move = int(cur_move)
            if cur_move in range(1,10):
                if move_arr[cur_move-1] == 0:
                    valid_move = True
                else:
                   print("This spot has already been played on.")
            else:
                raise ValueError
        except ValueError:
            print("Please enter a number within [1-9].")
    valid_move = False