#Gary Cunningham 29/03/19
#My program intends to calculate the square root of any inputted positive number and output an approximation to one decimal place.
#Adaptation from python tutorials, class content and w3schools.com interactive tutorials.

md = "Title: Moby Dick; or The Whale. Chapter 1. Call me Ishmael. Some years ago—never mind how long precisely—having little or no money in my purse, and nothing particular to interest me on shore, I thought I would sail about a little and see the watery part of the world. It is a way I have of driving off the spleen and regulating the circulation. Whenever I find myself growing grim about the mouth; whenever it is a damp, drizzly November in my soul; whenever I find myself involuntarily pausing before coffin warehouses, and bringing up the rear of every funeral I meet; and especially whenever my hypos get such an upper hand of me, that it requires a strong moral principle to prevent me from deliberately stepping into the street, and methodically knocking people’s hats off—then, I account it high time tozz get to sea as soon as I can. This is my substitute for pistol and ball. With a philosophical flourish Cato throws himself upon his sword; I quietly take to the ship. There is nothing surprising in this. If they but knew it, almost all men in their degree, some time or other, cherish very nearly the same feelings towards the ocean with me."
n = input("Enter the filename for problem 9: ")

file=open(n, "w+")

file.write(md)

file.close()

file=open(n, "r")

chapter1 = file.read()
second = (chapter1.split("."))
for words in chapter1:
    print('\n'.join(second[::2]))
    break

file.close()

