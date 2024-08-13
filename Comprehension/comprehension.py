
salaries = [12300,30122,21023,18932,35874]

def newSalary(x):
    return x * 1.2

nullList = []

for salary in salaries:
    nullList.append(newSalary(salary))

nullList = []

for salary in salaries:
    if salary > 3000:
        nullList.append(newSalary(salary))
    else:
        nullList.appned(newSalary(salary*2))


salaries = [12300,30122,21023,18932,35874]

[salary * 2 for salary in salaries]

[salary *2 for salary in salaries if salary > 20000]

[ salary * 2 if salary > 20000 else salary * 0 for salary in salaries]


def newSalary(x):
    return x * 1.2

[ newSalary(salary) if salary > 25000 else newSalary(salary * 0.8) for salary in salaries]

dict = {
    'a' : 2,
    'b' : 3,
    'c' : 4,
    'd' : 5
}

{k:v ** 2 for (k,v) in dict.items()}

{k.upper() : v * 2 for (k,v) in dict.items()}

numbers = range(10)
newDict = {}

for n in numbers:
    if n % 2 == 0:
        newDict[n] = n ** 2
    else:
        newDict[n] = n


{ n: n**2 for n in numbers if n % 2== 0}


#['total','speeding','alcohol','not_distracted','no_previous','ins_premium','ins_losses','abbrev']
#['TOTAL','SPEEDING','ALCOHOL','NOT_DISTACTED','NO_PREVIOUS','INS_PREMIUM','INS_LOSSES','ABBREV']

import seaborn as sns
df = sns.load_dataset('car_crashes')

for col in df.columns:
    print(col.upper())

A = []

for col in df.columns:
    A.append(col.upper())

df.columns = A

df.columns = [col.upper() for col in df.columns]

df.columns = [ 'FLAG' + col if 'INS' in col else 'NO_FLAG' + col for col in df.columns ]

import seaborn as sns
df = sns.load_dataset('car_crashes')
df.columns


num_cols = [col for col in df.columns if df[col].dtype != 'O']


import seaborn as sns
df = sns.load_dataset('car_crashes')
df.columns

num_cols = [col for col in df.columns if df[col].dtype!= "O"]
soz = {}
agg_list = ['mean','min','max','sum']

for col in num_cols:
    soz[col] = agg_list

{col: agg_list for col in num_cols}

df[num_cols].agg(new_dict)


original_dict = {'ahmet': 38, 'mehmet': 48, 'ali': 57, 'veli': 33}

dict2 = {k: v for (k, v) in original_dict.items() if v % 2 == 0}
print(dict2)