#Gary Cunningham 29/03/19
#My program intends to calculate the square root of any inputted positive number and output an approximation to one decimal place.
#Adaptation from python tutorials, class content and w3schools.com interactive tutorials

import datetime
# Called datetime as learned in tutorials and previous solution.
a = datetime.datetime.now().strftime("%A, %B")
b = datetime.datetime.now().strftime("%d")
c = datetime.datetime.now().strftime("%Y at %H:%M%p")
# Utilized datetime.datetime.now() as previous but had to consult the python.org
# directive table of datetime inputs to ensure accurate output as per problem set.

def ordinal(num):
    # Trying to create my own function for the ordinal numbers for all possibilities in a month.
        if num == 1 or num == 21 or num == 31:
            print(num + "st")
            # To get 1st, 21st, 31st.
        elif num == 2 or num == 22:
            print(num + "nd")
            # To get 2nd, 22nd.
        elif num == 3 or num == 23:
            print(num + "rd")
            #To get 3rd, 23rd.
        else:
            print(num + "th")
            # All else between 1 - 31 except above end with "th".
        return(str(num))
      
print(a, end =" ") 
ordinal(b) 
print(c)
#Calling function as well as datetimes surrounding it to get the correct datetime format and output.