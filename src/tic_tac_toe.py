#pass

def print_board(move_list = [1,2,3,4,5,6,7,8,9]):
    line = ('\n---|---|---')
    print('\n')
    for i in range(1,10):
        print(' '+str(move_list[i-1])+ ' ',end="")
        if i % 3 != 0:
            print('|',end="")
        else:
            if i != 9:
                print(line)
    print('\n')

def usage():
    print("Welcome to impossible Tic Tac Toe!\nThe board is laid out as follows:")
    print_board()
    print("To play, simply enter 1-9 corresponding to the cell that you want to play on.")

move_arr = [' ']*9
player_move = ""
CPU_MOVE = 'O'
cur_move = -1
valid_move = False
usage()

while player_move.upper() != 'X' and player_move.upper() != 'O':
    player_move = str(input("Enter X to play first, O to play second. Enter Q to quit. Choice: "))
    if player_move.upper() == 'Q':
        exit()

if player_move == 'O':
    CPU_MOVE = 'X'
    #call cpu

print_board(['X','O','X','O','X','O','X','O','X'])
#if move order is O, make initial computer move
#else get user input

#move input logicx
while True: #while game != done
    while not valid_move:
        try:
            cur_move = str(input("Enter a move[1-9] or Q to quit: "))
            if cur_move.upper() == 'Q':
                exit()
            else:
                cur_move = int(cur_move)
            if cur_move in range(1,10):
                if move_arr[cur_move-1] == ' ':
                    valid_move = True
                    move_arr[cur_move-1] = player_move
                else:
                   print("This spot has already been played on.")
            else:
                raise ValueError
        except ValueError:
            print("Please enter a number within [1-9].")
    valid_move = False
    print_board(move_arr)
    #make cpu move