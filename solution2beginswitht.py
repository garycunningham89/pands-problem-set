#Gary Cunningham. 19/03/19
# My program aims to input today in the form of a string with the hope of outputting if it begins with a T.
# Adapted from class lecture content, python.org tutorials and w3schools interactive tutorial learning.
import datetime
#Found function from class notes and through Python.org
#x = datetime.datetime.now()
#practised various variations on code but found similar function on w3schools.com for this and other problems.
# print (x.strftime("%A")) - first finding of the ability to print today in name, both above removed from final code submission.
x = datetime.datetime.now().strftime("%A")
# able to alter the variable to allow the name be forwarded to final print function.
if x.startswith("T"):
    print("Yes, today does begin with a T.")
#use of if function to see if datetime corresponds with the startswith *found on w3schools.
if not x.startswith("T"):
    print ("No, today does not begin with a T.")
#and finish with if not function to those that do not begin with a T.