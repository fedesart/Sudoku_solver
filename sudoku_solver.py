#%% Sudoku solver
# 06/04/2022
# Federico Sartori

from copy import deepcopy
from unittest import TestSuite

sudoku = [
    [8,5,0,0,7,0,0,0,9],
    [6,0,0,4,0,0,0,7,0],
    [2,0,0,0,5,0,0,1,0],
    [0,6,0,8,3,0,0,0,1],
    [0,0,0,1,4,7,0,0,8],
    [0,1,8,0,0,2,7,0,0],
    [0,0,3,0,8,1,6,0,0],
    [0,2,7,3,0,0,1,0,0],
    [0,0,0,0,0,0,9,5,0]
    ]

numbers = [i for i in range(1,10)]


def unwrap(square):
    # convert square to array
    return [y for x in square for y in x]


def wrap(array):
    # convert array to square
    return [[array[int(j + 9*i)]for j in range(9)] for i in range(9)]


def check(array):
    # check if a set of numbers has unique values (1 to 9)
    for n in numbers:
        if array.count(n) > 1:
            return False
    return True


def check_sudoku(sudoku):
    # check if sudoku solution is valid

    # check each row
    for row in sudoku:
        if not(check(row)):
            return False
    
    # check each column
    columns = map(list, zip(*sudoku)) # transposed sudoku
    for column in columns:
        if not(check(column)):
            return False

    # check each 3x3 square
    for i in range(0,9,3):
        for j in range(0,9,3):
            square = [[row[j], row[j+1], row[j+2]] for row in [sudoku[i], sudoku[i+1], sudoku[i+2]]]
            if not check(unwrap(square)):
                return False

    return True

def print_sudoku(sudoku):
    for row in sudoku:
        print(row)

def solve(sudoku_unwrap):
    solution = [sudoku_unwrap]
    free_slots = [i for i in range(len(solution[0])) if solution[0][i] == 0]

    i_slot = 0
    last_sol = solution[-1]

    while solution[-1].count(0) > 0:
        slot = free_slots[i_slot]
        val = last_sol[slot]
        test_values = range(val + 1, numbers[-1] + 1) # from next available value to 9

        if len(test_values)==0:
            solution = solution[:i_slot]
            i_slot -= 1

        for n in test_values:
            test = solution[-1].copy()
            test[slot] = n
            if check_sudoku(wrap(test)):
                i_slot += 1
                solution.append(test)
                last_sol = solution[-1]
                break
            elif (n == numbers[-1]) and not(check_sudoku(wrap(test))):
                i_slot -= 1
                last_sol = solution.pop()

    return solution[-1]

print('Problem:')
print_sudoku(sudoku)
sol = wrap(solve(unwrap(sudoku)))
print('Solution:')
print_sudoku(sol)
print(check_sudoku(sol))


        

