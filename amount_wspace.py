import pandas as pd

pd.set_option('display.max_columns', 50)
pd.set_option('display.width', 320)

amount_df = pd.read_csv('Amount_Details_crosstab.csv', sep='\t', encoding='utf-16le')
amount_df.dropna(axis=1, inplace=True)
print(amount_df.head())

val = 3