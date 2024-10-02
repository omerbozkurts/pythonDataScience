#  Görev 1:  List Comprehension yapısı kullanarak car_crashes verisindeki numeric değişkenlerin isimlerini büyük
#  harfe çeviriniz ve başına NUM ekleyiniz.


import pandas as pd
import seaborn as sns

df = sns.load_dataset('car_crashes')
df.columns

['NUM_'+col.upper() for col in df.columns]