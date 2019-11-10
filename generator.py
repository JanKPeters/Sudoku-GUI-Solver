import random

''' 
This function generates a list of numbers that are valid for 
given position (row and column) of the puzzle board
'''
def create_basket(board, row, col):
    basket = []
    basket.extend(range(1,10))
    for i in range(0+(row//3)*3, 3+(row//3)*3):
        for j in range(0+(col//3)*3, 3+(col//3)*3):
            num = board[i][j]
            if num in basket:
                basket.remove(num)
    
    for i in range(9):
        num = board[i][col]
        if num in basket:
            basket.remove(num)
    
    for num in board[row]:
        if num in basket:
            basket.remove(num)
    
    return basket  


def zero_row(x):
    return x * 0

'''
The generator will fill the entire field with a random unique solution and then deletes 
single fields at random in one pass. The "empty_chance" value between 1 and 100 is the 
percent chance of a field getting set to zero. (The higher the number the harder the puzzle, 
more missing fields)
'''
def generate_board(empty_chance):
    # initiate a blank board
    board = []
    while len(board) < 9:
        board.append([0]*9)  

    # filling the board with a unique solution 
    counter = 0
    row = 0
    while row < len(board):
        col = 0
        while col < len(board[row]):
            basket = create_basket(board, row, col)
            if len(basket) > 0:
                random.shuffle(basket)
                board[row][col] = basket.pop(0)
                col += 1
            else:
                counter += 1
                if counter < 5:
                    board[row] = list(map(zero_row, board[row]))
                    col = 0
                else:
                    counter = 0
                    board[row] = list(map(zero_row, board[row]))
                    board[row-1] = list(map(zero_row, board[row-1]))
                    if row-2 <= 0:
                        row = 0
                    else:
                        row -= 2
                    break
        row += 1

    # deleting numbers from the board to generate the puzzle
    for row in range(len(board)):
        for col in range(len(board[row])):
            chance = random.randint(1,100)
            if chance <= empty_chance:
                board[row][col] = 0
            

    return board
