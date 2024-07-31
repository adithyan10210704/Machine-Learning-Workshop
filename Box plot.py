import seaborn as sns
import matplotlib.pyplot as plt
data=[1,2,2,3,3,3,4,4,4,4]
tips=sns.load_dataset('tips')
sns.boxplot(x='day',y='total_bill',data=tips)
plt.title("Box plot")
plt.show()