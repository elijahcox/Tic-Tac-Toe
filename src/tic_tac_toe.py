class tic_tac_toe:
    move_arr = [' ']*9
    def __init__(self):
        self.usage()
        self.player_move = ''
        while self.player_move != 'X' and self.player_move != 'O':
            self.player_move = str(input("Enter X to play first, O to play second. Enter Q to quit. Choice: ")).upper()
            if self.player_move == 'Q':
                exit()
        self.cpu_move = 'O' if self.player_move == 'X'  else 'X'
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

    def usage(self):
        print("Welcome to impossible Tic Tac Toe!\nThe board is laid out as follows:")
        self.print_board([1,2,3,4,5,6,7,8,9])
        print("To play, simply enter 1-9 corresponding to the cell that you want to play on.")

    def check_for_two(self,to_find, fork_check = False):
        count = 0
        for i in range(0,7,3): #rows : [0-1-2], [3-4-5], [6-7-8]
            st = "".join(self.move_arr[i:i+3])
            if st.count(to_find) == 2 and st.count(" ") == 1:
                if fork_check:
                    count += 1
                else:
                    self.move_arr[st.find(' ') + i] = self.cpu_move
                    return True

        for i in range(0,3,1): #cols : [0-3-6], [1,4,7], [2,5,8]
            st = "".join(self.move_arr[i]+self.move_arr[i+3]+self.move_arr[i+6])
            if st.count(to_find) == 2 and st.count(" ") == 1:
                if fork_check:
                    count += 1
                else:
                    self.move_arr[st.find(' ')*3 + i] = self.cpu_move
                    return True

        for i in range(0,3,2):
            if i == 0:
                st = "".join(self.move_arr[i]+self.move_arr[i+4]+self.move_arr[i+8])
                if st.count(to_find) == 2 and st.count(" ") == 1:
                    if fork_check:
                        count += 1
                    else:
                        self.move_arr[st.find(' ')*4 + i] = self.cpu_move
                        return True       
            else:
                st = "".join(self.move_arr[i]+self.move_arr[i+2]+self.move_arr[i+4])
                if st.count(to_find) == 2 and st.count(" ") == 1:
                    if fork_check:
                        count += 1
                    else:
                        self.move_arr[st.find(' ')*2 + i] = self.cpu_move
                        return True             
        
        if fork_check:
            return count >= 2
        else:
            return False

    def check_fork(self,move):
        self.move_arr[4] = move #only middle can be used for fork under cpu strat
        if self.check_for_two(move,True) == True:
            if move != self.cpu_move:
                self.move_arr[4] = self.cpu_move #remove opponent move and place cpu move to block fork 
            return True
        else:
            self.move_arr[4] = ' '
            return False

    def get_cpu_move(self):
        if self.check_for_two(self.cpu_move): #1.  Win: If you have two in a row, play the third to get three in a row.
            print("CPU wins! Better luck next time!")
            self.print_board()
            exit()

        if self.check_for_two(self.player_move): #2. Block: If the opponent has two in a row, play the third to block them.
            return
   
        if self.move_arr[4] == ' ': #3. Fork: Create an opportunity where you can win in two ways.
            if self.check_fork(self.cpu_move):
                #cpu fork placed
                return
        
        if self.move_arr[4] == ' ': #4. Block Opponent's Fork:
            if self.check_fork(self.player_move):
                return

        if self.move_arr[4] == ' ': #5. Center: Play the center.
            self.move_arr[4] = self.cpu_move
            return

        #6. Opposite Corner: If the opponent is in the corner, play the opposite corner.
        corner_1 = str(self.move_arr[0]) + str(self.move_arr[8])
        corner_2 = str(self.move_arr[2]) + str(self.move_arr[6])
        empty_1 = " " + self.player_move
        empty_2 = self.player_move + " "
        if corner_1 == empty_1 or corner_1 == empty_2:
            if self.move_arr[0] == " ":
                self.move_arr[0] = self.cpu_move
            else:
                self.move_arr[8] = self.cpu_move
            return
        elif corner_2 == empty_1 or corner_2 == empty_2:
            if self.move_arr[2] == " ":
                self.move_arr[2] = self.cpu_move
            else:
                self.move_arr[6] = self.cpu_move
            return

        #7. Empty Corner: Play an empty corner.
        for i in range(0,9,2):
            if self.move_arr[i] == " ":
                self.move_arr[i] = self.cpu_move
                return

        #8. Empty Side: Play an empty side.
        for i in range(0,7,6): #sides: 0,1,2 and  6,7,8
            if "".join(self.move_arr[i:i+3]) == "   ":
                self.move_arr[i] = self.cpu_move
                return

        for i in range(0,3,2): #sides 0,3,6 and 2,5,8
            if self.move_arr[i]+self.move_arr[i+3]+self.move_arr[i+6] == "   ":
                self.move_arr[i] = self.cpu_move
                return
        
        #9. play somewhere random for now
        self.move_arr[self.move_arr.index(' ')] = self.cpu_move

    def get_user_move(self):
        while True:
            try:
                cur_move = str(input("Enter a move[1-9] or Q to quit: "))
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
                cpu_turn = False
            else:
                self.get_user_move()
                print("Your Move: ")
                self.print_board()
                cpu_turn = True
        print("Tie game! Better luck next time!")
        self.print_board()
        exit()
        
def main():
    game = tic_tac_toe()

if __name__ == "__main__":
    main()