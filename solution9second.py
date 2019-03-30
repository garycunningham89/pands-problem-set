#Gary Cunningham 29/03/19
#My program intends to calculate the square root of any inputted positive number and output an approximation to one decimal place.
#Adaptation from python tutorials, class content and w3schools.com interactive tutorials.

md = "Title: Moby Dick; or The Whale. Chapter 1. Call me Ishmael. Some years ago—never mind how long precisely—having little or no money in my purse, and nothing particular to interest me on shore, I thought I would sail about a little and see the watery part of the world. It is a way I have of driving off the spleen and regulating the circulation. Whenever I find myself growing grim about the mouth; whenever it is a damp, drizzly November in my soul; whenever I find myself involuntarily pausing before coffin warehouses, and bringing up the rear of every funeral I meet; and especially whenever my hypos get such an upper hand of me, that it requires a strong moral principle to prevent me from deliberately stepping into the street, and methodically knocking people’s hats off—then, I account it high time tozz get to sea as soon as I can. This is my substitute for pistol and ball. With a philosophical flourish Cato throws himself upon his sword; I quietly take to the ship. There is nothing surprising in this. If they but knew it, almost all men in their degree, some time or other, cherish very nearly the same feelings towards the ocean with me."
# Using md as the call for entering the first paragraph of Moby Dick including Title of Book and Chapter number.
n = input("Enter the filename as moby-dick.txt: ")
# Allowing the user input the file name on their device as per the problem set.
file=open(n, "w+")
# Opening file as per the standad fileouput = ("file_name", "access_mode") as learned from class content and python.org.
# Using "w+" as the creator of the file operator.
file.write(md)
# using the write() function to input the md as showm above.
file.close()
# Close the file to save it in the directory.
file=open(n, "r")
# Reopening the file using the open() function again but utilising the "r" so that it is read only as per class content and python.org.
chapter1 = file.read()
# Calling chapter1 as file.read() so to contine the editing of the output.
second = (chapter1.split("."))
# Using similar function as Problem 6 so that the output is split at "." for every second sentence.
for words in chapter1:
    print('.'.join(second[::2]))
    break
# Same function as solution 6 where ::2 was used for every second line and break to finish loop. This time joined with ".".
# Using "." instead of "\n" or " " so that sentences are outputted same as where they were split.
file.close()
# Ensuring to close file to complete program.
