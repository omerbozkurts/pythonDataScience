import seaborn as sns
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

pd.set_option('display.max_columns', None)
pd.set_option('display.width', 500)
df = sns.load_dataset('Titanic')

df.head()

df[['age','fare']].describe().T

[ col for col in df.columns if df[col].dtypes in ['int64','float64']]


def num_summary(dataframe, numerical_col, plot = False):
    print(dataframe[numerical_col].describe().T)

    if plot:
        dataframe[numerical_col].hist()
        plt.xlabel(numerical_col)
        plt.title(numerical_col)
        plt.show(block = True)

num_summary(df,'sex')


for col in df.columns:
    num_summary(df, col, plot = True)


