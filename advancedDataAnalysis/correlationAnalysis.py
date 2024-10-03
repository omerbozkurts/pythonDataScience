import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

pd.set_option('display.max_columns', None)
pd.set_option('display.width', 500)
df = pd.read_csv('advancedDataAnalysis/breast_cancer.csv')

df = df.iloc[:,1:-1]
df.head()


num_cols = [ col for col in df.columns if df[col].dtype in [int,float]]

corr = df[num_cols].corr()

sns.set(rc = {'figure.figsize' : (12, 12)})
sns.heatmap(corr, cmap='RdBu')
plt.show()



import matplotlib.pyplot as plt

notlar = [68, 74, 82, 90, 78, 85, 92, 88, 76, 61, 79, 73, 89, 81, 72, 95, 70, 83, 77, 75]

plt.hist(notlar, bins=10, edgecolor='r', alpha=0.7)
plt.xlabel('Notlar')
plt.ylabel('Frekans')
plt.title('Sınav Notları Dağılımı')
plt.show()




