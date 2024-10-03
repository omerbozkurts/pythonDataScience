import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

pd.set_option('display.max_columns', None)
pd.set_option('display.width', 500)
df = sns.load_dataset('Titanic')

df.head()

def grab_col_names(dataframe, cat_th = 10, car_th = 20):

    cat_cols = [ col for col in dataframe.columns if str(dataframe[col].dtypes) in ['category','object','bool']]
    num_but_cat = [ col for col in dataframe.columns if dataframe[col].nunique() < cat_th and dataframe[col].dtypes in ['int64','float64']]
    cat_but_car = [ col for col in dataframe.columns if dataframe[col].nunique() > car_th and
                    str(dataframe[col].dtypes) in ['object','category']]
    cat_cols = cat_cols + num_but_cat
    cat_cols = [ col for col in cat_cols if col not in cat_but_car]

    num_col = [ col for col in dataframe.columns if df[col].dtypes in ['int64','float64']]
    num_col = [ col for col in dataframe.columns if col not in cat_col]

    print(f'Observations: {dataframe.shape[0]}')
    print(f'Variables: {dataframe.shape[1]}')
    print(f'cat_cols: {len(cat_col)}')
    print(f'num_cols: {len(num_col)}')
    print(f'cat_but_car: {len(cat_but_car)}')
    print(f'num_but_cat: {len(num_but_cat)}')

    return num_col, cat_cols, cat_but_car


num_col, cat_cols, cat_but_car = grab_col_names(df)


def cat_summary(dataframe, col_name, plot = False):
    print(pd.DataFrame( { col_name : dataframe[col_name].value_counts(),
                        'Ratio' : 100 * dataframe[col_name].value_counts() / len(dataframe) } ) )

    if plot:
        plt.title(col_name)
        sns.countplot(x = dataframe[col_name], data = dataframe)
        plt.show(block = True)


for col in cat_cols:
    cat_summary(df,col,plot=True)


def num_summary(dataframe, numerical_col, plot = False):
    print(dataframe[numerical_col].describe().T)

    if plot:
        dataframe[numerical_col].hist()
        plt.xlabel(numerical_col)
        plt.title(numerical_col)
        plt.show(block = True)


for col in df.columns:
    num_summary(df, col, plot = True)


def target_summary_with_cat(dataframe, target, categorical_col):
    print(pd.DataFrame({"TARGET MEAN: " : dataframe.groupby(categorical_col)[target].mean()}))

target_summary_with_cat(df, 'survived','sex')

for col in cat_cols:
    target_summary_with_cat(df,'survived', col)




