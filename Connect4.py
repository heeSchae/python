#Earlier in the course, you implemented a function that could
#find if someone had won a particular game of either tic-tac-
#toe or mancala based on a 2D list or tuple representing the
#current game board.
#
#In this problem, you'll do the same thing, but for the game
#Connect 4. Write a function called check_winner which takes
#as input a 2D list. It should return "X" if there are four
#adjacent "X" values anywhere in the list (row, column,
#diagonal); "O" if there are four adjacent "O" values
#anywhere in the list; and None if there are neither.
#
#Here are the ways Connect-4 is different from tic-tac-toe:
#
# - Connect-4 is played with 6 rows and 7 columns, not 3
#   rows and 3 columns.
# - You must have 4 in a row (or column or diagonal) to win
#   instead of 3.
# - You may only place pieces in the bottom-most empty
#   space in a column (e.g. you "drop" the pieces in the
#   column and they fall to the first empty spot). Note,
#   though, that this shouldn't affect your reasoning.
#
#To keep things simple, we'll still use "X" and "O" to
#represent the players, and None to represent empty spots.
#You may assume there will be only one winner per board,
#no characters besides "X", "O", and None, and you don't
#have to worry about whether the board is actually a
#valid game of Connect 4.
#
#Hints:
# - Don't forget both kinds of diagonals, top-left to
#   bottom-right and bottom-left to top-right.
# - This board is too large to check every possible place
#   for a winner: there are 69 places a player could win.
# - Remember, if you put a negative index in a list,
#   Python "wraps around" and checks the last value. You
#   may have to control for this.


#Write your function here!
def check_winner(twoDList):
    
    #Check horizontal locations for win
    winner = None
    
    for r in range(6):
        for c in range(7-3):
            if twoDList[r][c] == twoDList[r][c+1] and twoDList[r][c+1] == twoDList[r][c+2] and twoDList[r][c+2] == twoDList[r][c+3] and not twoDList[r][c] == None:
                winner = twoDList[r][c]
    
 
    for r in range(6-3):
        for c in range(7):
            if twoDList[r][c] == twoDList[r+1][c] and twoDList[r+1][c] == twoDList[r+2][c] and twoDList[r+2][c] == twoDList[r+3][c] and not twoDList[r][c] == None:
                winner = twoDList[r][c]
                
    for r in range(3, 6):
        for c in range(7-3):
            if twoDList[r][c] == twoDList[r-1][c+1] and twoDList[r-1][c+1] == twoDList[r-2][c+2] and twoDList[r-2][c+2] == twoDList[r-3][c+3] and not twoDList[r][c] == None:
                winner = twoDList[r][c]            
         #Negatively       
    for r in range(6-3):
        for c in range(7-3):
            if twoDList[r][c] == twoDList[r+1][c+1] and twoDList[r+1][c+1] == twoDList[r+2][c+2] and twoDList[r+2][c+2] == twoDList[r+3][c+3] and not twoDList[r][c] == None:
                winner = twoDList[r][c] 
                
    return winner

    
#The code below tests your function on three Connect-4
#boards. Remember, the line breaks are not needed to create
#a 2D tuple; they're used here just for readability.
xwins = ((None, None, None, None, None, None, None),
         ("X", None, None, None, None, None, None),
         ("O", None, None, None, "X" , None, None),
         ("X", "O", None, "X" , "O" , "O", None),
         ("X", "O" , "O" , "X" , "O" , "X", None),
         ("O" , "X" , "X" , "O" , "O" , "X" , "X"))
owins = ((None, None, None, None, None, None, None),
         (None, None, None, None, None, None, None),
         ("O" , "O" , "O" , "O" , None, None, None),
         ("O" , "X" , "X" , "X" , None, None, None),
         ("X" , "X" , "X" , "O" , "X" , None, None),
         ("X" , "O" , "O" , "X" , "O" , None, None))
nowins =(("X" , "X" , None, None, None, None, None),
         ("O" , "O" , None, None, None, None, None),
         ("O" , "X" , "O" , "O" , None, "O" , "O" ),
         ("O" , "X" , "X" , "X" , None, "X" , "X" ),
         ("X" , "X" , "X" , "O" , "X" , "X" , "O" ),
         ("X" , "O" , "O" , "X" , "O" , "X" , "O" ))
         
print(check_winner(xwins))
