#Gary Cunningham 29/03/19
#My program intends to output the date and time in the format Day, Month Date Year at Time(am/pm).
#Adaptation from python tutorials, class content and w3schools.com interactive tutorials.


def ordinal(num):
    # Trying to create my own function for the ordinal numbers for all possibilities in a month.

    if num == 1 or 21 or 31:
        print(num + "st")
        # To get 1st, 21st, 31st.
    elif num == 2 or 22:
        print(num + "nd")
        # To get 2nd, 22nd.
    elif num == 3 or 23:
        print(num + "rd")
        #To get 3rd, 23rd.
    else:
        print(num + "th")
        # All else between 1 - 31 except above end with "th".
    return(str(num))
      
import datetime
date = datetime.datetime.now()
# Called datetime as learned in tutorials and previous solution.
    
a = date.strftime("%A, %B")
b = date.strftime("%d")
c = date.strftime("%Y at %H:%M%p")
# Utilized datetime.datetime.now() as previous but had to consult the python.org
# for the directive table of datetime inputs to ensure accurate output as per problem set.
print(a, end = " ")
ordinal(b)
print(c)
#Calling function as well as datetimes surrounding it to get the correct datetime format and output as close as possible.
#Found difficulty in combining the output on one line as the ordinal() was returning errors as Nonetype and would not allow end = "" or be printed accurately.