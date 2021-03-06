''' Instructions:
   Work with a partner to complete these tasks. You may assume that all variables/lists are declared and initialized (unless you are specifically asked to create/initialize a list); you need only write the code using the variables/lists indicated in the description. Write your solution below the commented description.
'''

''' 1. 
   Create a list of ints, faveNums, that holds 3 integers.
'''



''' 2. 
   Create a list of Strings, holidays, that holds 14 holidays.  
'''



''' 3. 
   Create a list of characters, grades, that holds 5 letter grades.
'''



''' 4. 
   Create a list of booleans, funny, the can keep track of whether 18 things are funny or not. 
'''
funny = {}
for i in range(18):
   a.append(True)


''' 5. 
   Create a list of doubles, salaries, that holds the salaries of all the employees at a university. The number of employees is stored in the int numEmployees.
'''



''' 6. 
   A picture's dimensions are stored in integer variables x and y. Create a single list of integers that can store the grayscale value for each pixel in the list.
'''
dimensions = {}
for i in range (x*y):
   dimensions.append(0)



''' 7. 
   In a class, each student has 0, 1, 2 or 3 siblings. The numbers of students with no siblings is stored in the variable noSiblings, the number of students with one sibling is stored in the variable oneSibling, the number of students with two siblings is stored in the variable twoSiblings, and the number of students with three siblings is stored in the variable threeSiblings. Create a list that holds all the names of the students in the class, as well as the names of all their siblings.
'''



''' 8. 
   Create a list that holds all the months in the year. (No loop.)
'''
months = {January, Febuary, March, April, May, June, July, August, September, October, November, December}


''' 9. 
   Create a list that holds all the days of the week. (No loop.)
'''



''' 10. 
   Create a list that holds all the possible values for boolean variables. (No loop.)
'''

booleanvariable = {True, False}


''' 11. 
   Create a list that holds the names of all the 3rd form dorms on campus. (No loop.)
'''



''' 12.  
   Create a list that holds 3 random numbers with values between 0 and 1. (Loop optional.)
'''

import random

randomnumbers = {random.randint(0,1),random.randint(0,1),random.randint(0,1)}

''' 13. 
   Create a list that will represent a deck of cards. Some example data for cards would be AS (ace of spaces), 5H (5 of hearts), JC (jack of clubs), 9D (9 diamonds). (Loop required.) 
'''



''' 14. 
   Write a Yahtzee program that simulates the rolling of five dice and prints "Yahtzee" if all five dice are the same; otherwise it should print "Try again."
'''

import random
Yahtzee = [random.randint(0,6), random.randint(0,6), random.randint(0,6), random.randint(0,6), random.randint(0,6)]
if Yahtzee[0] ==  Yahtzee[1] and Yahtzee[0] ==  Yahtzee[2] and Yahtzee[0] ==  Yahtzee[3] and Yahtzee[0] ==  Yahtzee[4]:
   print ("Yahtzee")

''' 15. 
   In a list, specials are numbers in a list that have an even number before them, an odd number behind them, and they themselves are divisible by 3. Given a list of ints called numbers, print out the location in the list of the specials, as well as the value in front of them, their value, and the value behind them. For example:
   position 4: 14, 9, 25
'''



''' 16. 
   Write a program to search for the "saddle points" in a 5 by 5 list of integers. A saddle point is a cell whose value is greater than or equal to any in its row, and less than or equal to any in its column. There may be more than one saddle point in the list. Print out the coordinates of any saddle points your program finds. Print out "No saddle points" if there are none.
'''

import random
saddlepoint = ["No saddlepoint"]
board=[[random.randint(1,10), random.randint(1,10), random.randint(1,10), random.randint(1,10), random.randint(1,10)] for i in range(5)]
for i in range(5):
   print(*board[i])
for x in range(5):
   for y in range(5):
      if board[x][0] <= board[x][y] and board[x][1] <= board[x][y] and board[x][2] <= board[x][y] and board[x][3] <= board[x][y] and board[x][4] <= board[x][y]:
         if board[x][y] <= board[0][y] and board[x][y] <= board[1][y] and board[x][y] <= board[2][y] and board[x][y] <= board[3][y] and board[x][y] <= board[4][y]:
            saddlepoint.append(board[x][y])
            saddlepoint.remove("No saddlepoint")
print(saddlepoint)




''' 17. 
   In the game of chess, a queen can attack pieces which are on the same row, column, or diagonal. A chessboard can be represented by an 8 by 8 list. A 1 in the list represents a queen on the corresponding square, and a O in the list represents an unoccupied square. Given the two locations for queens (row1, col1, row2, col2), place the queens in the 2D list, chessboard. Then process the board and indicate whether or not the two queens are positioned so that they attack each other. 
'''



''' 18. 
   Given a list, write code that will reverse the order of the elements in the list. For example, dog, cat, bunny should become bunny, cat, dog.
'''
mylist = []
mylist.reverse()
print(mylist)

''' 19. 
   Given a list, doorknobs, that holds strings, swap the elements at positions 1 and 3, if possible.
'''



''' 20. 
   In a list of ints called numbers, find the largest number in the list and place it at the end of the list.
'''

numbers = []
greatest = numbers[0]
for i in range(len(numbers)):
   if greatest < numbers[i]:
      greatest = numbers[i]
numbers.remove(greatest)
numbers.append(greatest)

''' 21. 
   In a 2D list with dimensions w by h, filled with random numbers from from 1 to 100, replace every odd number with either 2 or 22; 2 if the number was a single digit number, 22 if the number was a 2-digit number. 
'''



''' 22. 
   In a 2D list with dimensions w by h, holding grayscale values for an image, adjust the colors so the image is inverted. All light portions should be dark, all dark portions should be light. A value of 200 should be 5, a value of 100 should be 155, etc. Remember, there are 256 levels for color, including 0.
'''

dimensions = {}
for i in range (x*y):
   dimensions.append(abs(255-number))


''' 23.
   In a list, shifters, holding ints, shift all elements forward 1 position. For example, position 2 should move to position 1, position 1 to position 0, and position 0 to the end of the list (etc.)
'''



''' 24. 
   Given an N-by-N grid of elevation values (in meters), a peak is a grid point for which all four neighboring cells are strictly lower. Write a code fragment that counts the number of peaks in a given N-by-N grid.
'''
peaks = 0 
grid = []
for x in range (N):
   for y in range (N):
      if grid[x][y] > grid[x+1][y] and grid[x][y] > grid[x+1][y+1] and grid[x][y] > grid[x+1][y-1] and grid[x][y] > grid[x][y] and grid[x][y] > grid[x][y+1] and grid[x][y] > grid[x][y-1]grid[x][y] > grid[x-1][y] and grid[x][y] > grid[x-1][y+1] and grid[x][y] > grid[x-1][y-1]:
         peaks = peaks + 1

''' 25. 
   90% of incoming college students rate themselves as above average. Write some code that, given a list of student rankings (stored in integer list rankings), prints the fraction of values that are strictly above the average value.
'''



''' 26. 
   Given a 9-by-9 list of integers between 1 and 9, check if it is a valid solution to a Sudoku puzzle: each row, column, and block should contain the 9 integers exactly once.
'''
board=[[random.randint(1,9), random.randint(1,9), random.randint(1,9), random.randint(1,9), random.randint(1,9),  random.randint(1,9), random.randint(1,9), random.randint(1,9), random.randint(1,9)] for i in range(9)]
correct = 0
for i in range (9):
   if board[i][0] + board[i][2] + board[i][3] + board[i][4] + board[i][5] + board[i][6] + board[i][7] + board[i][8] == 45:
      correct = correct+1
for i in range (9):
   if board[0][i] + board[2][i] + board[3][i] + board[4][i] + board[5][i] + board[6][i] + board[7][i] + board[8][i] == 45:
      correct = correct+1
if correct == 18:
   Sudoku = True
   print(*board)


'''
	27. Create a list of 100 numbers between 1 and 10 (inclusive), create a new list whose first value is the number of 1s in the original list, whose 2nd value is the number of 2s in the original list, and so on. Average the number of occurences of each number in the list over 100 repetitions. Average the averages. Print the result to the screen.
'''



''' Sources
   http://users.csc.calpoly.edu/~jdalbey/103/Projects/ProgrammingPractice.html
   http://introcs.cs.princeton.edu/java/14array/
'''