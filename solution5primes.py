#Gary Cunningham. 25/03/19
#My program intends to show whether or not an inputted positive integer is a prime number.
#Adaptation from python tutorials, class content and w3schools.com interactive tutorials.
#Attempted this solution alongside the inputs from  the learnings of previous solutions in this problem set.
n = int(input("Please enter a positive integer: "))
def primes(num):
#Defining the function for calling later.
    if (n <= 1):
        print("That is not a prime number")
#Calling 1 as not a prime number if inputted into the funtion. 
    elif (n <= 3):
        print("That is a prime number")
#Calling 2 and 3 as prime numbers, the first two in the set. using "Elif".
    elif (n % 2 == 0) or (n % 3 == 0):
        print("That is not a prime number")
# Using the modulo function for any number greated than 3 to calculated if their is a remainder when divided by 2 or 3.
# These outputs are not prime numbers.
    else:
        print("That is a prime number")
#Any numbers not divisiable by 2 and 3 evenly, and that are not 2 or 3 themselves, are prime numbers.
num = primes(int(n))
# Calling function at the end.