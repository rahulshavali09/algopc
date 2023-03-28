#                                                 Practical – 1 


#A - Program to find sum of elements in an array

# Take user input to create array 
##arr = [] 
##n = int(input("Enter the number of elements in the array: ")) 
##print("Enter the elements of the array:") 
##for i in range(n): 
## arr.append(int(input())) 
### Calculate the sum of all elements in the array 
##sum = 0 
##for i in range(n): 
## sum += arr[i] 
### Print the sum of all elements in the array 
##print("The sum of all elements in the array is:", sum)



#B - Program to find minimum or maximum element in an array
##import time
### Take user input to create array 
##arr = [] 
##n = int(input("Enter the number of elements in the array: ")) 
##print("Enter the elements of the array:") 
##for i in range(n): 
## arr.append(int(input())) 
### Find the minimum and maximum elements in the array 
##start_time = time.time()
##min_element = arr[0] 
##max_element = arr[0] 
##for i in range(1, n): 
## if arr[i] < min_element:
##     min_element = arr[i] 
## if arr[i] > max_element: 
##     max_element = arr[i] 
##end_time = time.time()
### Print the minimum and maximum elements in the array and time complexity 
##print("The minimum element in the array is:", min_element) 
##print("The maximum element in the array is:", max_element) 
##print("Time complexity:", end_time - start_time, "seconds")
##


#C - program to count number of even and odd elements in an array 
# Take user input to create array 
##arr = [] 
##n = int(input("Enter the number of elements in the array: ")) 
##print("Enter the elements of the array:") 
##for i in range(n): 
## arr.append(int(input())) 
### Count the number of even and odd elements in the array 
##count_even = 0 
##count_odd = 0 
##for i in range(n): 
## if arr[i] % 2 == 0: 
##     count_even += 1 
## else: 
##     count_odd += 1 
### Print the number of even and odd elements in the array 
##print("The number of even elements in the array is:", count_even) 
##print("The number of odd elements in the array is:", count_odd)





#                                        Practical 2
#
#A  : Sum of row element, column element and diagonal element. 
# Take user input to create square matrix 
##n = int(input("Enter the size of the square matrix: ")) 
##print("Enter the elements of the matrix:") 
##matrix = [] 
##for i in range(n):
##    row = list(map(int, input().split())) 
##    matrix.append(row) 
### Calculate the sum of row elements, column elements, and diagonal elements 
##sum_row = [sum(row) for row in matrix] 
##sum_column = [sum(column) for column in zip(*matrix)] 
##sum_diagonal1 = sum(matrix[i][i] for i in range(n)) 
##sum_diagonal2 = sum(matrix[i][n-i-1] for i in range(n)) 
### Print the sum of row elements, column elements, and diagonal elements 
##print("Sum of row elements:", sum_row) 
##print("Sum of column elements:", sum_column) 
##print("Sum of diagonal elements:", [sum_diagonal1, sum_diagonal2])






#      B- Sum of two matrices.





##                     Practical - 3 
##a. Program to create a list-based stack and perform various stack operations



##stack = [] # create an empty list to use as a stack 
### push items onto the stack 
##stack.append(1) 
##stack.append(2) 
##stack.append(3) 
### print the stack 
##print("Stack:", stack) 
### pop an item from the stack 
##item = stack.pop() 
##print("Popped item:", item) 
### print the stack again 
##print("Stack:", stack) 
### peek at the top item of the stack 
##top_item = stack[-1]
##
##print("Top item:", top_item) 
### check if the stack is empty 
##if not stack: 
## print("Stack is empty") 
##else: 
## print("Stack is not empty") 
### get the size of the stack 
##size = len(stack) 
##print("Stack size:", size) 
### clear the stack 
##stack.clear() 
##print("Cleared stack:", stack)






##b. Program to create infix to posƞix expression conversion using stack



### define a funcƟon to convert infix to posƞix
##def infix_to_posƞix(expression):
## # iniƟalize an empty stack and an empty output string
## stack = [] 
## output = "" 
## # define a dicƟonary to store operator precedence
## precedence = {"+": 1, "-": 1, "*": 2, "/": 2, "^": 3} 
## # loop through each character in the expression 
## for char in expression: 
## # if the character is an operand, add it to the output string 
##     if char.isalnum(): 
##         output += char 
## # if the character is an operator 
##     elif char in precedence: 
## # pop operators off the stack and add them to the output string 
## # while they have higher or equal precedence 
##         while stack and stack[-1] != "(" and precedence[char] <= precedence.get(stack[-1], 0): 
##             output += stack.pop() 
## # push the current operator onto the stack 
##             stack.append(char) 
## # if the character is a leŌ parenthesis, push it onto the stack
##     elif char == "(": 
##         stack.append(char) 
## # if the character is a right parenthesis, pop operators off the stack 
## # and add them to the output string unƟl a leŌ parenthesis is found
##     elif char == ")": 
##         while stack and stack[-1] != "(": 
##             output += stack.pop() 
## # remove the leŌ parenthesis from the stack
## if stack and stack[-1] == "(": 
##     stack.pop() 
## # pop any remaining operators off the stack and add them to the output string 
## while stack: 
##     output += stack.pop() 
## return output 
### example usage 
##expression = "a + b * c - d / e ^ f" 
##posƞix_expression = infix_to_posƞix(expression)
##print("Infix expression:", expression) 
##print("Posƞix expression:", posƞix_expression)
##
##
##
##                                         PracƟcal -4 
##
##
##a) Linear search 
##def linear_search(arr, x):
##    for i in range(len(arr)): 
##         if arr[i] == x: 
##             return i 
##    return -1 
### example usage 
##arr = [3, 5, 2, 8, 4, 9] 
##x = 8 
##index = linear_search(arr, x) 
##if index != -1: 
##     print(f"{x} found at index {index}") 
##else: 
##     print(f"{x} not found")

#                         b) Binary search(IteraƟve method)
##def binary_search(arr, x): 
##     left, right = 0, len(arr) - 1 
##     while left <= right:
##         mid = (left+ right) // 2
##         if arr[mid] == x: 
##             return mid 
##         elif arr[mid] < x: 
##             left = mid + 1
##         else: 
##             right = mid - 1 
##             return -1 
### example usage 
##arr = [1, 3, 5, 7, 9, 11, 13] 
##x = 7 
##index = binary_search(arr, x) 
##if index != -1: 
## print(f"{x} found at index {index}") 
##else: 
## print(f"{x} not found")


















