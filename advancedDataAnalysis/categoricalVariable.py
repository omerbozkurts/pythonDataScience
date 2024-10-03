import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

pd.set_option('display.max_columns', None)
pd.set_option('display.width',500)
df = sns.load_dataset('titanic')

df.head()


cat_cols = [col for col in df.columns if str(df[col].dtypes) in ['category','object','bool']]

num_but_cat = [col for col in df.columns if df[col].nunique() < 10 and df[col].dtypes in ['int64','float64']]

cat_but_car = [col for col in df.columns if df[col].nunique() > 20 and str(df[col].dtypes) in ['category','object','bool']]

cat_cols = cat_cols + num_but_cat

cat_cols = [col for col in cat_cols if col not in cat_but_car]


def cat_summary(dataframe, col_name, plot = False):
    print(pd.DataFrame( { col_name : dataframe[col_name].value_counts(),
                        'Ratio' : 100 * dataframe[col_name].value_counts() / len(dataframe) } ) )

    if plot:
        plt.title(col_name)
        sns.countplot(x = dataframe[col_name], data = dataframe)
        plt.show(block = True)

cat_summary(df, 'sex',True)

for col in cat_cols:
    cat_summary(df,col,plot=True)



