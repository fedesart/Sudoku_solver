#%% Sudoku solver
# 06/04/2022
# Federico Sartori

import timeit


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


def print_sudoku(sudoku):
    for row in sudoku:
        print(row)


def check_duplicates(array):
    # check if a set of numbers has unique values (0 excluded, 1 to 9)
    for n in numbers:
        if array.count(n) > 1:
            return False
    return True


def check_sudoku(sudoku):
    # check if sudoku solution is valid

    # check each row for duplicates
    for row in sudoku:
        if not(check_duplicates(row)):
            return False
    
    # check each column for duplicates
    columns = map(list, zip(*sudoku)) # transposed sudoku
    for column in columns:
        if not(check_duplicates(column)):
            return False

    # check each 3x3 square for duplicates
    for i in range(0,9,3):
        for j in range(0,9,3):
            square = [[row[j+k] for k in range(3)] for row in [sudoku[i+k] for k in range(3)]]
            if not check_duplicates(unwrap(square)):
                return False

    return True


def solve(sudoku_unwrap):
    # Solve sudoku
    # Input in list format

    solution_partial = sudoku_unwrap.copy() # test solution
    solution_final = [] # final solution
    free_slots = [i for i in range(len(solution_partial)) if solution_partial[i] == 0]

    if not(free_slots): # check if solution is complete
        return wrap(solution_partial)
    else:
        slot = free_slots[0]
        for n in numbers:
            solution_partial[slot] = n
            if check_sudoku(wrap(solution_partial)):
                # if solution is feasible
                # try to solve the rest of the sudoku
                solution_final = solve(solution_partial)
                if solution_final:
                    return solution_final
                

start = timeit.timeit()

print('Problem:')
print_sudoku(sudoku)
sol = solve(unwrap(sudoku))
print('Solution:')
print_sudoku(sol)
end = timeit.timeit()
print(end - start)

        

