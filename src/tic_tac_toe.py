class tic_tac_toe:
    move_arr = [' ']*9
    def __init__(self):
        print("Welcome to impossible Tic Tac Toe!\nThe board is laid out as follows:")
        self.print_board([1,2,3,4,5,6,7,8,9])
        print("To play, simply enter 1-9 corresponding to the cell that you want to play on.")
        self.player_move = ''
        while self.player_move != 'X' and self.player_move != 'O':
            self.player_move = str(input("Enter X to play first, O to play second. Enter Q to quit. Choice: ")).upper()
            if self.player_move == 'Q':
                exit()
        self.cpu_move = 'O' if self.player_move == 'X' else 'X'
        self.game_handler(self.cpu_move == 'X')

    def print_board(self,move_list = None):
        move_list = self.move_arr if move_list == None else move_list
        print('\n')
        for i in range(1,10):
            print(' '+str(move_list[i-1])+ ' ',end="")
            if i % 3 != 0:
                print('|',end="")
            else:
                if i != 9:
                    print('\n---|---|---')
        print('\n')

    def check_for_two(self,to_find, fork_check = False):
        count = 0
        for i in range(0,7,3): #rows : [0-1-2], [3-4-5], [6-7-8]
            st = "".join(self.move_arr[i:i+3]) #create string of rows
            if st.count(to_find) == 2 and st.count(" ") == 1:
                if fork_check:
                    count += 1 #if 2 in row found but not playing to win or block, increment fork counter
                else:
                    self.move_arr[st.find(' ') + i] = self.cpu_move
                    return True

        for i in range(0,3,1): #cols : [0-3-6], [1,4,7], [2,5,8]
            st = "".join(self.move_arr[i:9:3]) #create string of cols
            if st.count(to_find) == 2 and st.count(" ") == 1:
                if fork_check:
                    count += 1 #if 2 in row found but not playing to win or block, increment fork counter
                else:
                    self.move_arr[st.find(' ')*3 + i] = self.cpu_move #transform i to move_arr index
                    return True

        for arr in [[0,4,8],[2,4,6]]:
            st = "".join(self.move_arr[arr[0]]+self.move_arr[arr[1]]+self.move_arr[arr[2]])
            if st.count(to_find) == 2 and st.count(" ") == 1:
                if fork_check:
                    count += 1
                else:
                    self.move_arr[arr[st.find(' ')]] = self.cpu_move
                    return True 
        
        if fork_check:
            return count >= 2 #fork has created two 
        else:
            return False #no 2 in row found

    def check_fork(self,move):
        self.move_arr[4] = move #only middle can be used for fork under cpu strat, temporarily place move in middle
        if self.check_for_two(move,True) == True: #check if placed move results in at 2 ways to win
            if move != self.cpu_move:
                self.move_arr[4] = self.cpu_move #remove opponent move and place cpu move to block fork
            return True
        else:
            self.move_arr[4] = ' ' #fork not created, remove placement
            return False

    def check_corner(self): # [0,8] or [2,6]
        corner_strings = [] #list of empty corners to check incase corner opposite of opponent scenario doesn't exist
        for corner in [[0,8],[2,6]]: #check array of corners
            st = self.move_arr[corner[0]] + self.move_arr[corner[1]] #string of two corners
            if st.count(' ') > 0:
                mapped_index = corner[st.index(' ')] 
                if st.count(self.player_move) == st.count(' '): #if one player move one blank space
                    self.move_arr[mapped_index] = self.cpu_move
                    return True
                else:
                    corner_strings.append(mapped_index) #else two blank spaces, add first corner to mapped_index
        if len(corner_strings) > 0:
            self.move_arr[corner_strings[0]] = self.cpu_move #mark first entered blank forner
            return True
        return False #no corner found

    def get_cpu_move(self):
        if self.check_for_two(self.cpu_move): #1.  Win: If you have two in a row, play the third to get three in a row.
            print("CPU wins! Better luck next time!")
            self.print_board()
            exit()

        if self.check_for_two(self.player_move): #2. Block: If the opponent has two in a row, play the third to block them.
            return
   
        if self.move_arr[4] == ' ':
            if self.check_fork(self.cpu_move): #3. Fork: Create an opportunity where you can win in two ways.
                pass
            elif self.check_fork(self.player_move): #4. Block Opponent's Fork:
                pass
            else:
                self.move_arr[4] = self.cpu_move #5. Center: Play the center.
            return

        if self.check_corner(): #6. Opposite Corner: If the opponent is in the corner, play the opposite corner. 
            return #7. Empty Corner: Play an empty corner.

        side_str = "".join(self.move_arr[1:9:2]) #8. Empty Side: Play an empty side (only middle of each, get string of all sides)
        if ' ' in side_str:
            self.move_arr[side_str.index(' ')*2 +1] = self.cpu_move #mark first empty side

    def get_user_move(self):
        while True:
            try:
                cur_move = input("Enter a move[1-9] or Q to quit: ")
                if cur_move.upper() == 'Q':
                    exit()
                else:
                    cur_move = int(cur_move)
                    if cur_move in range(1,10):
                        if self.move_arr[cur_move-1] == ' ':
                            self.move_arr[cur_move-1] = self.player_move
                            return
                        else:
                            print("This spot has already been played on.")
                    else:
                        raise ValueError
            except ValueError:
                print("Please enter a number within [1-9].")

    def game_handler(self,cpu_turn):    
        while ' ' in self.move_arr:
            if cpu_turn:
                self.get_cpu_move()
                print("CPU Move: ")
                self.print_board()
                cpu_turn = False #use cpu_turn to alternate conditionals
            else:
                self.get_user_move()
                print("Your Move: ")
                self.print_board()
                cpu_turn = True
        print("Tie game!")
        self.print_board()

game = tic_tac_toe() #create instance, run game