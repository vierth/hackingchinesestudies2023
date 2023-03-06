# we will need a specific modiule from matplotlib to do our plotting
import matplotlib.pyplot as plt
import random
import seaborn as sns

# most of the detials her you can find at https://matplotlib.org/users/pyplot_tutorial.html

# plot a line!
sns.set()
x_data = [random.randint(0, 10) for i in range(0,10)]
y_data = [random.randint(0, 10) for i in range(0,10)]

sizes = [i*10 for i in range(1, 11)]

colors = ["magenta" for i in range(0,10)]
colors[4] = "blue"
colors[8] = "cyan"

for x,y,s,c in zip(x_data,y_data,sizes,colors):
    print(x,y,s,c)

plt.scatter(x_data, y_data, s=sizes, c=colors)
plt.title("This is the title of the graph")
plt.ylabel("Random number")
plt.xlabel("Other random number")
plt.legend()
# plt.show()