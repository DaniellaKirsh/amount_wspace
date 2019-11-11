import sys
import pandas as pd
import numpy as np


# slicing float where whitspace would be
def slice_wspace_num(x):
    s_x = str(x)
    if '.' not in s_x:
        return x[-min(len(s_x), 3):]
    else:
        # getting index of index from end of number
        i = len(s_x) - s_x.index('.')
        r = s_x[-min(len(s_x), 3 + i):]
        return float(r)


# setting initial df
def set_df(path):
    df = pd.read_csv(path, sep='\t', encoding='utf-16le')
    df.dropna(axis=1, inplace=True)
    return df


# creating a new df with rows with whitespace issues
def update_df_ws(df):
    orig_columns = list(df.columns)
    print(orig_columns)
    # renaming columns for comfort
    df.columns = ['Changed_Amount', 'image croppedImageId', 'Extd amount', 'Actl amount', 'Day of Ts Created']
    df['Actl cut'] = ""
    # cutting the actual amount mased off where whitespace would poentially be
    df['Actl cut'] = df['Actl amount'].map(slice_wspace_num)
    # take all rows where 'actl cut' = 'extd amount'
    df['Cut_eq_extd'] = df['Extd amount'] == df['Actl cut']
    orig_columns += ['Actl cut', 'Cut_eq_extd']
    df.columns = orig_columns
    new_df = df.loc[df['Cut_eq_extd']]
    new_df = new_df.loc[:, :'Day of Ts Created']
    return new_df


def main():
    pd.set_option('display.max_columns', 50)
    pd.set_option('display.width', 320)

    # creating df from cvs path
    df = set_df(sys.argv[1])

    # creating new df according requested update
    new_df = update_df_ws(df)
    new_csv = new_df.to_csv(path_or_buf='/Users/daniellakirshenbaum/PycharmProjects/amount_ws/new_amounts.csv', sep='\t', encoding='utf-16le')
    return new_csv


if __name__ == "__main__":
    main()
