import random

def create_basket(board, r, c):
    basket = []
    basket.extend(range(1,10))
    for i in range(0+(r//3)*3, 3+(r//3)*3):
        for j in range(0+(c//3)*3, 3+(c//3)*3):
            num = board[i][j]
            if num in basket:
                basket.remove(num)
    
    for i in range(9):
        num = board[i][c]
        if num in basket:
            basket.remove(num)
    
    for i in range(9):
        num = board[r][i]
        if num in basket:
            basket.remove(num)
    
    return basket  


def zero_row(x):
    return x * 0


def generate_board(empty_chance):
    # initiate a blank board
    board = []
    while len(board) < 9:
        board.append([0]*9)  

    counter = 0
    r = 0
    while r < len(board):
        c = 0
        while c < len(board[r]):
            basket = create_basket(board, r, c)
            if len(basket) > 0:
                random.shuffle(basket)
                board[r][c] = basket.pop(0)
                c += 1
            else:
                counter += 1
                if counter < 5:
                    board[r] = list(map(zero_row, board[r]))
                    c = 0
                else:
                    counter = 0
                    board[r] = list(map(zero_row, board[r]))
                    board[r-1] = list(map(zero_row, board[r-1]))
                    if r-2 <= 0:
                        r = 0
                    else:
                        r -= 2
                    break
        r += 1

    for r in range(len(board)):
        for c in range(len(board[r])):
            chance = random.randint(1,100)
            if chance <= empty_chance:
                board[r][c] = 0
            

    return board
