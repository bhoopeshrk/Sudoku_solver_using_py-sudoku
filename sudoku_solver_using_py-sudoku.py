#importing sudoku package
from sudoku import Sudoku

#creating the unsolved sudoku puzzle for which the solution needed
board = [[8, 0, 0,  6, 0, 0,  0, 0, 0],
         [0, 0, 0,  0, 7, 0,  3, 8, 0],
         [0, 0, 5,  0, 2, 0,  0, 0, 0],

         [5, 1, 9,  0, 0, 0,  0, 0, 0],
         [0, 6, 0,  0, 0, 0,  4, 0, 0],
         [0, 2, 0,  0, 0, 0,  6, 0, 7],
        
         [2, 0, 0,  0, 0, 5,  0, 0, 1],
         [0, 0, 0,  0, 0, 0,  0, 0, 9],
         [0, 0, 0,  9, 0, 1,  0, 6, 0 ]]

#defining the unsolved sudoku puzzle in the sudoku package
puzzle = Sudoku(3, 3, board=board)

#Displaying the unsolved sudoku puzzle
puzzle.show_full()
#Displaying the solution for the unsolved sudoku puzzle
puzzle.solve().show_full()
