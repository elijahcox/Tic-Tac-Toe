
'''
    Win: If you have two in a row, play the third to get three in a row.

    Block: If the opponent has two in a row, play the third to block them.

    Fork: Create an opportunity where you can win in two ways.

    Block Opponent's Fork:

    Option 1: Create two in a row to force the opponent into defending, as long as it doesn't result in them creating a fork or winning. For example, if "X" has a corner, "O" has the center, and "X" has the opposite corner as well, "O" must not play a corner in order to win. (Playing a corner in this scenario creates a fork for "X" to win.)

    Option 2: If there is a configuration where the opponent can fork, block that fork.

    Center: Play the center.

    Opposite Corner: If the opponent is in the corner, play the opposite corner.

    Empty Corner: Play an empty corner.

    Empty Side: Play an empty side.
'''

def get_cpu_move(move_list):
    pass


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
cpu_move = 'O'
cur_move = -1
valid_move = False
usage()

while player_move.upper() != 'X' and player_move.upper() != 'O':
    player_move = str(input("Enter X to play first, O to play second. Enter Q to quit. Choice: "))
    if player_move.upper() == 'Q':
        exit()

if player_move == 'O':
    cpu_move = 'X'
    get_cpu_move(move_arr) #call cpu, edits move_arr
    print_board()

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