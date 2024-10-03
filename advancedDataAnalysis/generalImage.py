import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt

pd.set_option('display.max_columns',None)
pd.set_option('display.width',500)
df = sns.load_dataset('Titanic')
df.head()


def df_check(dataframe, head=5):
    print('****************** shape ******************')
    print(dataframe.shape)
    print('****************** types ******************')
    print(dataframe.dtypes)
    print('****************** head ******************')
    print(dataframe.head(head))
    print('****************** tail ******************')
    print(dataframe.tail(head))
    print('****************** NaN Frequency ******************')
    print(dataframe.isnull().sum())
    print('****************** Quantiles ******************')
    print(dataframe.describe([0,0.05,0.10,0.50,0.75,0.95,1]))


df_check(df)