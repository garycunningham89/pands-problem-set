#Gary Cunningham. 20/03/19
#My program intends to show the inputting of a positive integer, either odd or even numbers, where odds are multiplied by 3 and increase by 1 and evens are halved.
#The program will loop until the input reaches 1 and output the list of figures to get to 1.
#Adaptation from python tutorials @www.docs.python.org and class tutorials.
def collatz(num):
# Using the def() to instigate the program known as collatz.
    if (num % 2 == 0): # % 2 == 0 used for figuring out whether a number is even.
        print(num // 2)
        return num // 2 
        # Returning the number to continue loop.
    else: 
        # if/else = if or if not i.e. even in this example.
        oddnum = ((num * 3) + 1) 
        # Odd numbers follow this calculation.
        print(oddnum)
        return oddnum
n = input("Please enter a posiitive integer: ")
while n != 1:
#Using while loop to keep the program running until it reaches 1.
    n = collatz(int(n))
# Finishing by calling collatz() for n as an integer (int()) and running program.