#Gary Cunningham. 31/03/19
#My program intends to plot functions x, x^2 and 2^x in the range 0, 1, 2, 3, 4 using matplotlib.
#Adaptation from python tutorials @www.docs.python.org and class tutorials using matplotlib.
import matplotlib.pyplot as pl
# Importing the plotting function as pl.
x = [i for i in range (5)]
y = [i**2 for i in x]
z = [2**i for i in x]
# Defining x, x^2 and 2^x in range (0,4).
pl.figure(figsize=(15,5))
# Defining figure size.
pl.plot(x, y)
pl.plot(x, z)
# Plot y and z on Y Axis versus x on the X axis.
pl.title('Solution 10 - Plot')
# Giving the graph a Title.
pl.xlabel('X Axis')
pl.ylabel('Y Axis')
# Labelling the Axes.
pl.legend(['x^2', '2^x'], loc=0)
# Giving the plots labels and locating the legend box at point in top left of screen.
pl.show()
# Outputting the plot.