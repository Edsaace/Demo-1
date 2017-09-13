from random import randint #Import the randomizer function

board = [] #Create empty list

for x in range(5):              #loop 5 times
    board.append(["O"] * 5)     #append 5 "O" in the empty list

def print_board(board):         #create function "print_board"
    for row in board:           #for every ROW in board list
        print " ".join(row)     #do this - add space every "O" and print each row

print "Let's play Battleship!"  #print this
print_board(board)              #print the board list by calling the function

def random_row(board):                      #create function random_row
    return randint(0, len(board) - 1)       #return a random number from 0 to 4

def random_col(board):                      #create function random_col
    return randint(0, len(board[0]) - 1)    #return a random number from 0 to 4

ship_row = str(random_row(board))           #convert the int to str
ship_col = str(random_col(board))           #convert the int to str


# Everything from here on should go in your for loop!
# Be sure to indent four spaces!
for turn in range(4):                           #you have 4 turns
    guess_row = int(raw_input("Guess Row:"))    #input your guess row       this is a matrix
    guess_col = int(raw_input("Guess Col:"))    #input your guess column

    if guess_row == ship_row and guess_col == ship_col:     
        print "Congratulations! You sunk my battleship!"
        break
    else:
        if (guess_row < 0 or guess_row > 4) or (guess_col < 0 or guess_col > 4):
            print "Oops, that's not even in the ocean."
        elif(board[guess_row][guess_col] == "X"):
            print "You guessed that one already."
        else:
            print "You missed my battleship!"
        board[guess_row][guess_col] = "X"
    # Print (turn + 1) here!
        print "Turn", turn + 1
        print_board(board)
        if turn == 3:
            print "Game Over"
            print "The ship is on the " + ship_row + " , " + ship_col