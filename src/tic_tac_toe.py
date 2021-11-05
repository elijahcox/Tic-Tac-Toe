
def check_for_two(move_list,move): #returns array of indices with first 2 in a row found
    #corners: [0-1,0-3] [2-1,2-5] [6-7,6-3] [8-7,8-5] 
    
    #middle: [4-1,4-3,4-5,4-7]
    if move_list[4] == move:
        for i in range(1,8,2):
            if move_list[i] == move:
                return [4,i]
    return -1


def get_cpu_move(move_list,cpu_move,opponent_move):
    #1.  Win: If you have two in a row, play the third to get three in a row.
    two_in_row = check_for_two(move_list,cpu_move)

    

    #2. Block: If the opponent has two in a row, play the third to block them.
    #check corners and middle
    two_in_row = check_for_two(move_list,opponent_move)

    #3. Fork: Create an opportunity where you can win in two ways.

    #4. Block Opponent's Fork:
    #4.1.  Create two in a row to force the opponent into defending, as long as it doesn't result in them creating a fork or winning. 
    # For example, if "X" has a corner, "O" has the center, and "X" has the opposite corner as well, "O" must not play a corner in order to win. 
    # (Playing a corner in this scenario creates a fork for "X" to win.)
    #4.2. If there is a configuration where the opponent can fork, block that fork.
    
    #5. Center: Play the center.
    if move_list[4] == ' ':
        move_list[4] = cpu_move
        return move_list
    
    #6. Opposite Corner: If the opponent is in the corner, play the opposite corner.
    corner_1 = str(move_list[0]) + str(move_list[8])
    corner_2 = str(move_list[2]) + str(move_list[6])
    empty_1 = " " + opponent_move
    empty_2 = opponent_move + " "
    if corner_1 == empty_1 or corner_1 == empty_2:
        if move_list[0] == " ":
            move_list[0] = cpu_move
        else:
            move_list[8] = cpu_move
        return move_list
    elif corner_2 == empty_1 or corner_2 == empty_2:
        if move_list[2] == " ":
            move_list[2] = cpu_move
        else:
            move_list[6] = cpu_move
        return move_list
    
    #7. Empty Corner: Play an empty corner.
    for i in range(0,9,2):
        if move_list[i] == " ":
            move_list[i] = cpu_move
            return move_list

    #8. Empty Side: Play an empty side.
    for i in range(0,7,6): #sides: 0,1,2 and  6,7,8
        if "".join(move_list[i:i+3]) == "   ":
            move_list[i] = cpu_move
            return move_list
    
    for i in range(0,3,2): #sides 0,3,6 and 2,5,8
        if move_list[i]+move_list[i+3]+move_list[i+6] == "   ":
            move_list[i] = cpu_move
            return move_list

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
    move_arr = get_cpu_move(move_arr,cpu_move,player_move) #call cpu for first move, edits move_arr
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