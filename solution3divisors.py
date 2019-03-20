#Gary Cunningham. 19/03/19
# My program aims to all numbers between 1000 and 10000 which are divisible by 6 but not 12.
# Adapted from class lecture content, python.org tutorials, learn solo mobile application and w3schools interactive tutorial learning.
my_list = range(1000, 10000)
#using the range function to accurately get all numbers between 1000 and 10000.
divisors = list(filter(lambda x: (x % 6 == 0) and not (x % 12 == 0), my_list))
# called divisors = list() twice at first but then shortened the full (filter(lamba x : etc)) into one combined function for efficiency using "and not".
print(divisors)
# list() allowed placing all outputs in sequence surrounded by [] in attempy to make the programs output easier read and contained.
# filter() parameter was learned from w3schools tutorial and the understading of it and lambda () were further researched in python.or and programiz.com online.