# we will need a specific modiule from matplotlib to do our plotting
import matplotlib.pyplot as plt
import random

# most of the detials her you can find at https://matplotlib.org/users/pyplot_tutorial.html

# plot a line!
x_data = [random.randint(0, 10) for i in range(0,10)]
y_data = [random.randint(0, 10) for i in range(0,10)]

plt.plot(x_data, y_data, label="first line")
plt.title("This is the title of the graph")
plt.ylabel("Random number")
plt.xlabel("Other random number")
plt.legend()
plt.show()