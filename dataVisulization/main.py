import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

pd.set_option('display.max_columns',None)
pd.set_option('display.width',500)

df = sns.load_dataset('Titanic')
df['sex'].value_counts().plot(kind = 'bar')
plt.show()

plt.hist(df['age'])
plt.show()

plt.boxplot(df['fare'])
plt.show()

x = np.array([1,8])
y = np.array([0,150])

plt.plot(x,y)
plt.show()

plt.plot(x,y,'o')
plt.show()


x = np.random.randint(20,100,5)
y = np.random.randint(4,32,5)

plt.plot(x,y,'x')
plt.show()

y = np.random.randint(20,140,14)

plt.plot(y, marker = 'x')
plt.show()

plt.plot(y, linestyle = 'dashed', color = 'pink')
plt.show()

plt.plot(x, linestyle = 'dotted', color = 'blue')
plt.plot(y, linestyle = 'dashdot', color = 'yellow')
plt.show()

x = np.random.randint(500,1000,10)
y = np.random.randint(500,1000,10)

plt.plot(x,y,'x')
plt.title('veriler')
plt.xlabel('yatay eksen')
plt.ylabel('dikey eksen')
plt.grid()
plt.show

plt.subplot(1,2,1)
plt.title('number 1')
plt.plot(x,y,'o')

plt.subplot(1,2,2)
plt.title('number 2')
plt.plot(x,'o')

plt.show()

df = sns.load_dataset('tips')
sns.countplot(x=df['sex'],data=df)
plt.show()

df['sex'].value_counts().plot(kind='bar')
plt.show()

sns.boxplot(x = df['total_bill'])
plt.show()