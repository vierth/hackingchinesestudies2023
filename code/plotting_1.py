# we will need a specific modiule from matplotlib to do our plotting
import matplotlib.pyplot as plt

# most of the detials her you can find at https://matplotlib.org/users/pyplot_tutorial.html

# plot a line!
my_data = [i*2 for i in range(0,10)]
my_data_2 = [i/2 for i in range(0,10)]

plt.plot(my_data, label="first line")
plt.plot(my_data_2, label="second line")
plt.title("This is the title of the graph")
plt.ylabel("Made up number")
plt.xlabel("Index of number")
plt.legend()
plt.savefig("my_figure.pdf")