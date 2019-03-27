#Gary Cunningham 27/03/19
#My program intends to calculate the square root of any inputted positive number and output an approximation to one decimal place.
#Adaptation from python tutorials, class content and w3schools.com interactive tutorials.
n = float(input("Please enter a positive number: "))
# Instead of using int(), we require all real numbers so the float() inputting tool was used instead.
import math
ans = math.sqrt(n)
# Found this built in function on the Python.org tutorial page. 
print("The square root of", n, "is approx", round(ans, 1))
# Print the suggested outputted including the round() function to ensure the float is limited to one decimal place.



#The below function was tried and tested as an alternate to the import math = math.sqrt() built in function.
# In place of lines 7 and 9 the following 2 lines can be inputted for similar outputs.
#ans = n**(.5)
#print("The square root of", n, "is approx", round(ans, 1))
