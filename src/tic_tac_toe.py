#pass

def print_board(move_list):
    pass

def usage():
    print("Welcome to impossible Tic Tac Toe!\nThe board is laid out as follows:")
    moves = [1,2,3,4,5,6,7,8,9]
    print_board(moves)
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

#move input logic
while True:
    #get move
    #check that it is num
    #if num, that it is [1-9]
    #if [1-9] that it isn't taken
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