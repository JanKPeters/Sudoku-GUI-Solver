import random

''' 
This function generates a list of numbers that are valid for 
given position (row and column) of the puzzle
'''
def create_basket(puzzle, row, col):
    basket = []
    basket.extend(range(1,10))
    for i in range(0+(row//3)*3, 3+(row//3)*3):
        for j in range(0+(col//3)*3, 3+(col//3)*3):
            num = puzzle[i][j]
            if num in basket:
                basket.remove(num)
    
    for i in range(9):
        num = puzzle[i][col]
        if num in basket:
            basket.remove(num)
    
    for num in puzzle[row]:
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
def generate_puzzle(empty_chance):
    # initiate a blank puzzle
    puzzle = []
    while len(puzzle) < 9:
        puzzle.append([0]*9)  

    # filling the puzzle with a unique solution 
    counter = 0
    row = 0
    while row < len(puzzle):
        col = 0
        while col < len(puzzle[row]):
            basket = create_basket(puzzle, row, col)
            if len(basket) > 0:
                random.shuffle(basket)
                puzzle[row][col] = basket.pop(0)
                col += 1
            else:
                counter += 1
                if counter < 5:
                    puzzle[row] = list(map(zero_row, puzzle[row]))
                    col = 0
                else:
                    counter = 0
                    puzzle[row] = list(map(zero_row, puzzle[row]))
                    puzzle[row-1] = list(map(zero_row, puzzle[row-1]))
                    if row-2 <= 0:
                        row = 0
                    else:
                        row -= 2
                    break
        row += 1

    # deleting numbers from the puzzle to generate the puzzle
    for row in range(len(puzzle)):
        for col in range(len(puzzle[row])):
            chance = random.randint(1,100)
            if chance <= empty_chance:
                puzzle[row][col] = 0
            

    return puzzle
