#Gary Cunningham. 27/03/19
#My program intends to convert the string inputted by removing every second word on the output.
#Adaptation from python tutorials, class content and w3schools.com interactive tutorials.
#Attempted this solution alongside the inputs from the learnings of previous solutions in this problem set.

n = input("Please enter a sentence: ")
secondstring = (n.split())
# Using the split() function as found in python tutorials and practiced on the w3schools tutorials to understand its uses.
for words in secondstring:
# Created the loop so that the split can continue regardless of the length of the inputted sentence.
    print(' '.join(secondstring[::2]))
# Included the (::2) so that the second word of the input is removed from the program and outputted. 
# Was unsure how to join the outputted list to a string and found the ' '.join() function allowed accurate output.
    break
# Included a break in the loop to ensure accuracy during testing.