# pands-problem-set
Gary Cunningham
Problem Set 2019 Programming and Scripting
Work for Module in Programming and Scripting
Kept up to date with the content in the lecture videos and thought I had the grasp of programming and scripting as a complete beginner.
Began the problem set the week after it was released. And realised I had no idea what I was doing.
I took a break and focused on following content and completing exercises in other modules.
Came back at the beginning of March and it took quite a while to complete problem 1 as I wanted to try my own algorithms and input unique codes. Found this very difficult so then I began looking at supplementary reading and resources.

The following is a list of references which were used while compiling this problem set.
Reference List:
1) Github. https://github.com/.
2)GMIT. Quality assurance framework. https://www.gmit.ie/general/quality-assurance-framework.
3) Python.org Tutorials. https://www.docs.python.org/.
4) w3Schools Interative Tutorials. https://www.w3schools.com/.
5) Programiz Tutorials and Examples. https://www.programiz.com.
6) Stackoverflow Examples. https://stackoverflow.com

The following is the Problem Set Questions followed by info on each Solution in repository.

1. Write a program that asks the user to input any positive integer and outputs the
sum of all numbers between one and that number.

Solutions 1. This was completed with the help of class content and python.org tutorials. Using the input() and range() functions to allow sum up to take place accurately.

2. Write a program that outputs whether or not today is a day that begins with the
letter T.

Solution 2. I had continued trying to learn as much about Python as possible before returning to the problem set but still had a difficult time creating the solution. I finally had a eureka moment when completing the Begins with T program. I done a lot of interactive tutorial work on w3schools.com and I found these very helpful and hope to use these alongside other resources to learn and understand further.

3. Write a program that prints all numbers between 1,000 and 10,000 that are divisible
by 6 but not 12.

Solution 3. I found the formatting getting easier and the algorithm constructed was done by;
1. Learning to get divisors of any number.
2. Testing it in both 1000 and 10000 and then as part of the range.
3. Finding function of lambda and how it is constructed from various learning resources but mainly w3schools.com.
4. Compiling and testing the program using range (), list (), filter () and lambda () as well as using the "%", "and" and "and not" to accurately produce output.  

4. Write a program that asks the user to input any positive integer and outputs the
successive values of the following calculation. At each step calculate the next value
by taking the current value and, if it is even, divide it by two, but if it is odd, multiply
it by three and add one. Have the program end if the current value is one.

Solution 4. This was completed with a lot of class tutorial content and the code basis was built alone through trial and error. The difficulty arose in using the newly seen functions def(), especially the recalling of it and the while loop and I had to consult w3schools and python.org for further information, which was there was quite an amount for this program and the processes contained.

5. Write a program that asks the user to input a positive integer and tells the user
whether or not the number is a prime.

Solution 5. The problem set question for the prime numbers was the first program which I attempted almost entirely by myself from reusing variations of learned class content and processes from Solutions 1 - 4. The "Eureka moment" has given confidence in programming and Python. Reused the def() function and completed it using if, elif and else statements. Tested function using a range of inputs to see if they were outputted as correctly as prime numbers or not.

6. Write a program that takes a user input string and outputs every second word.

Solution 6. I attempted to complete as much of the program by myself but the use of the new functions for myself using strings such as split() and join() required me utilize the Python tutorial to fully complete it. I had gotten as far as printing the sentences in list format and needed to research to find how to combine or join list into strings. Tested function using example sentence and extended them to ensure accuracy.

7. Write a program that that takes a positive floating point number as input and outputs
an approximation of its square root.

Solution 7. With its built in function capability I found this was one of the easier problems in this set. The round(). sqrt() and float() were all used for the first time. Testing of the program was done from multiple inputs and even an attempt at an alternative function that which was imported was tried to increase learning and understanding.

8. Write a program that outputs today’s date and time in the format “Monday, January
10th 2019 at 1:15pm”.

Solution 8. This was one of the more difficult and time consuming on a personal level. Attempted to create my own function for ordinal numbers which went well for direct outputs of ordinal(num) with num ranging between 1 - 31 for all possible days of the month. The gathering and consulting of datetime directives on python.org was interesting in calling %A, %B, %d, etc. and beginning to understand the differences. The difficulty arose in combing my def() function and simple print() of datetime functions surrounding it. Many errors were experienced while testing including EOF while parsing and "noneobject", and so on. Where there was a challenge there was a lot of learning and what seemed as simple as creating a function for ordinal number allowed greater understanding of Python overall for myself through research and testing.

9. Write a program that reads in a text file and outputs every second line. The program
should take the filename from an argument on the command line.

Solution 9. The solution was begun by learning how to create a file from class notes and python.org. A file was created, written into and closed using w+. Then reopened as a read only with the inputted data for Moby Dick, being chapter 1 taking off google books. Then adapting the code for Solution 6 the program every second sentence split and joined with a ".". The file closes and the program outputs every second sentence. Being able to alter how the strings are split or joined was very informative and were tested in various ways to ensure accuracy.

10. Write a program that displays a plot of the functions x, x2 and 2x in the range [0, 4].

Solution 10. The final problem in the set was attempted by learning basics and examples of using matplotlib first from python.org tutorials alongside introduction from class content. The functionality and the calling of these functions were very comprehendable and the lead up for it as problem 10 allowed a greater ease for completion. After importing matplotlib, the x, x^2 and 2^x in the range(0, 4) and using the matplotlib functions of plot, title, axis labels, legend and show to output the graph showing the functions.

Final commit on 31/03/19 after testing functions and ensuring outputs are accurate.