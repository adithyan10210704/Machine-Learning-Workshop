import matplotlib.pyplot as plt
x=[1,2,3,4,5]
y=[2,3,5,7,11]
plt.plot(x,y,label="Prime numbers")
plt.title("Line Plot with grid and legend")
plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.grid(True)
plt.legend()
plt.show()