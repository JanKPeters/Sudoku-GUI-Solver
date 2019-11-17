import random

''' 
This function generates a list of numbers that are valid for 
given position (row and column) of the puzzle
'''
def create_basket(puzzle, row, col):
    # New full basket of numbers
    basket = []
    basket.extend(range(1,10))
    
    # Check numbers already set in the house (square) and remove these form the basket
    for i in range(0+(row//3)*3, 3+(row//3)*3):
        for j in range(0+(col//3)*3, 3+(col//3)*3):
            num = puzzle[i][j]
            if num in basket:
                basket.remove(num)
    
    # Check numbers already present in the same column and remove these form the basket
    for i in range(9):
        num = puzzle[i][col]
        if num in basket:
            basket.remove(num)
            
    # Check numbers already present in the same row and remove these form the basket
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

    puzzle = delete_numbers(puzzle, empty_chance)

    return puzzle

'''
The following function will take the filled board and delete numbers to generate a puzzle
'''
def delete_numbers(puzzle, empty_chance):
    puzzle_copy = puzzle.copy()
    # deleting numbers from the puzzle to generate the puzzle
    for row in range(len(puzzle)):
        for col in range(len(puzzle[row])):
            chance = random.randint(1,100)
            if chance <= empty_chance:
                if non_unique_quad(row, col, puzzle, puzzle_copy):
                    puzzle[row][col] = 0
    
    return puzzle

'''
Funktion that checks for non unique quadrilaterals. The goal is to prevent the deletion of same number pairs
either in a column of houses or in a row of houses. E.g.    
3 - 8
| | |
8 - 3
if all four fields are set to zero during the generation of the puzzle then the solution can be either combination of 
these pairs and is therefore not unique.
The goal is therefore to check if such a quadrilateral figure can be found and if all other fields are already set to zero 
to return False and prevent the deletion of the fourth field.
'''
def non_unique_quad(row, col, puzzle, puzzle_copy):
    # check all rows in a house column
    for i in range(0+(col//3)*3, 3+(col//3)*3):
        if i != col:
            # if the numbers in the same row of the house are not zero there is no point in checking the others
            if puzzle_copy[row][i] != 0:
                break
            else:
                num_pair = []
                num_pair.append(puzzle[row][col])
                num_pair.append(puzzle_copy[row][i])
            for j in range(0, 9):
                if j not in range(0+(row//3)*3, 3+(row//3)*3):
                    rownums = []
                    rownums.append(puzzle_copy[j][0+(col//3)*3])
                    rownums.append(puzzle_copy[j][1+(col//3)*3])
                    rownums.append(puzzle_copy[j][2+(col//3)*3])
                    if num_pair[0] in rownums and num_pair[1] in rownums:
                        r0 = rownums.index(num_pair[0])
                        r1 = rownums.index(num_pair[1])
                        if puzzle_copy[j][r0+(col//3)*3] == 0 and puzzle_copy[j][r1+(col//3)*3] == 0:
                            return False
    
    # Same thing as above for columns in the house row
    for i in range(0+(row//3)*3, 3+(row//3)*3):
        if i != row:
            if puzzle_copy[i][col] != 0:
                break
            else:
                num_pair = []
                num_pair.append(puzzle[row][col])
                num_pair.append(puzzle_copy[row][i])
            for j in range(0, 9):
                if j not in range(0+(row//3)*3, 3+(row//3)*3):
                    colnums = []
                    colnums.append(puzzle_copy[0+(row//3)*3][j])
                    colnums.append(puzzle_copy[1+(row//3)*3][j])
                    colnums.append(puzzle_copy[2+(row//3)*3][j])
                    if num_pair[0] in colnums and num_pair[1] in colnums:
                        if puzzle_copy[colnums.index(num_pair[0])+(col//3)*3][j] == 0 and puzzle_copy[colnums.index(num_pair[1])+(col//3)*3][j] == 0:
                            return False
                                            
    return True
