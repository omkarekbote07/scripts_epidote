import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv('E.coli lopatkin db.csv')
df.info()
#df1 = df[['X.label' , 'asm_acc' , 'asm_level' , 'host' , 'scientific_name' , 'ftppaths']]
#df1.info()
#unq = df1['host'].unique()
#print(unq)
human_df = df[df['host'] == 'Homo sapiens']
human_df.info()

unq1 = human_df['host'].unique()
print(unq1)

unq2 = human_df['scientific_name'].unique()
print(unq2)

#for i in range(len(unq2)):
 #   print(unq2[i])

unq2_df = pd.DataFrame(unq2, columns=['scientific_name'])
unq2_df.to_csv('sci_names.csv')

df4 = human_df[~human_df['scientific_name'].astype(str).str.startswith('Shigella')]
#df4.to_csv('Lopatkin_curated.csv')
df4.info()

unq3 = df4['scientific_name'].unique()
print(unq3)

#for i in range(len(unq3)):
 #   print(unq3[i])