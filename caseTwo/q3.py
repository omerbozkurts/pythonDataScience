import seaborn as sns
df = sns.load_dataset('car_crashes')

og_list = ['abbrev','no_previous']

df[[data for data in df if data not in og_list]]