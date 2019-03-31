#Gary Cunningham. 03/03/19
#My program intends to show the sum of all the numbers for, and including, the inputted integer from number 1.
#Adaptation from python tutorials @www.docs.python.org and class tutorials.
n = input("Please enter a positive integer: ")
# Inputting the first line of the program as per the requested format.
n = int(n)
# Use of int() to ensure use of postive integers.
sum = 0
# Defining base number for program.
for num in range(1, n+1, 1):
    sum = sum+num
# Creeating the range with increases to n added together within the range.
print("Sum of all numbers between 1 and", n, "is:", sum)
# Ensuring the output is explained in the program.