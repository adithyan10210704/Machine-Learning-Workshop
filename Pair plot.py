import seaborn as sns
import matplotlib.pyplot as plt
data=[1,2,2,3,3,3,4,4,4,4]
tips=sns.load_dataset("tips")
sns.pairplot(tips)
plt.title("Pair plot")
plt.show()