import pandas as pd

s = pd.Series([10,41,15,32,19])
type(s)
s.index
s.dtype
s.size
s.ndim
s.values
type(s.values)
s.head(3)
s.tail(2)

df = pd.read_csv("advertising.csv")

df.head()

import pandas as pd
import seaborn as sns

df = sns.load_dataset('titanic')
df.head()
df.tail()
df.shape
df.info()
df.columns
df.index
df.describe().T
df.isnull().values.any()
df["sex"].head()
df["sex"].value_counts()
df[0:13]
df.drop(0, axis = 0).head()
delete_indexes = [1,3,5,7]
df.drop(delete_indexes, axis= 0).head(10)
# degisikligi kalici hale getirebilmek icin inplace = True olarak parametre seklinde verilmelidir

df['age'].head()
df.age.head()

df.index = df['age']
df.drop('age',axis=1).head()
df.head()

df.loc[:,df.columns.str.containes('age')].head


import pandas as pd
import seaborn as sns
pd.set_option('display.max_columns',None)
df = sns.load_dataset('titanic')
df.head()

df.iloc[0:3]
df.iloc[0,0]

df.loc[0:3]

df.iloc[0:3,0:3]

df.loc[0:3, 'age']

col_names = ['age','embarked','alive']
df.loc[0:3,col_names]

df[df['age']>50].head()

df[df["age"]>50]["age"].count()

df.loc[(df['age']>50) & (df['sex']=='male'),['age','class']].head()

df.loc[(df['age'] > 50)
      & (df['sex'] == 'male')
      & ((df['embark_town'] == 'Cherbourg') | (df['embark_town'] == 'Southampton')),
      ['age','class','embark_town']].head()


df.groupby("sex")['age'].mean()

df.groupby('sex').agg({'age':['mean','sum','count']})

df.groupby(['sex','embark_town','class']).agg({'age':['mean','sum','count'],
                                       'survived':'mean'})

df.pivot_table('survived','sex','embarked')

df.pivot_table('survived','sex',['embarked','class'])

df['new_age'] = pd.cut(df['age'],[0,10,18,25,40,90])

df.head()

df.pivot_table('survived','sex','new_age')


