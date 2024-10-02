import seaborn
import seaborn as sns
import pandas as pd
df = sns.load_dataset('Titanic')
df = pd.DataFrame(df)

df['sex'].value_counts()

df.nunique()

df['pclass'].nunique()

df[['pclass','parch']].nunique()

type(df['embarked'])
df['embarked'].dtypes
df['embarked'] = df['embarked'].astype('category')

df[df['embarked']=='C']

df[df['embarked'] != 'S']

df[(df['sex'] == 'female') & (df['age'] < 30)]

df[(df['fare'] > 500) | (df['age'] > 70)]

df[df.columns].isna().sum()

df.pop('who')

df['deck'].fillna(df['deck'].mode()[0],inplace = True)

df[df['age' == 'NaN']].replace(df['age'].mean(),inplace=True)

df.groupby(['pclass','sex']).agg({'survived':['sum','count','mean']})

[1 if value < 30  else 0 for value in df['age']]

df.insert(column='age_flag',value=[1 if value < 30  else 0 for value in df['age']],loc=10)
