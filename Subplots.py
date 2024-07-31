import matplotlib.pyplot as plt
x=[1,2,3,4,5]
y=[2,3,5,7,11]
categories=['A','B','C','D']
values=[4,7,1,8]
plt.subplot(1,2,1)
plt.plot(x,y)
plt.title("Plot1")
plt.subplot(1,2,2)
plt.bar(categories,values)
plt.title("Plot2")
plt.show()