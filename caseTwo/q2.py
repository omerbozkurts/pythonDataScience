import seaborn as sns
df = sns.load_dataset('car_crashes')

[col.upper() + '_FLAG' if 'no' not in col else col.upper() for col in df.columns ]