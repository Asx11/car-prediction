#!/usr/bin/env python
# coding: utf-8

# In[21]:


import re
import pandas as pd
from datetime import datetime
import os


def df_text_cleaning(text):
    #text = df.column

    for i in range(len(text)):
        clean_text = re.sub("https://[A-Za-z0-9./_]+", " ", text[i]).strip()
        clean_text = clean_text.lower()
        clean_text = re.sub("@[A-Za-z0-9_]+ ", "", clean_text) 
        clean_text = re.sub("#[A-Za-z0-9_]+ ", "", clean_text)
        whitelist = set("'abcdefghijklmnopqrstuvwxyz ")
        clean_text = re.sub(":", " ", clean_text)
        clean_text = ''.join(filter(whitelist.__contains__, clean_text))
        clean_text = clean_text.strip()
        text[i] = clean_text

    return text

def data_check(df):
    a= df.isna().any().sum()
    b= df.duplicated().sum()
    c= df.isnull().any().sum()
    return print(' This Df contains {} NAN, {} NULL and {} dublicate line'.format(a,c,b))

def idcheck(df1, a : pd.Series, b: pd.Series):

    
    check = df1.assign(result=a.isin(b).astype(int))
    # mettre une excution qui enregistre les fichiers csv des id manquant
    if check[(check['result'] != 1)].shape[0] > 0:
        print(f"There is " + str(check[(check['result'] != 1)].shape[0]) + 
              " missing line between dataframe")
        return check[check['result']!=1]
    else:
        if a.name != b.name : 
            print(f"There is no missing id between {a.name} and {b.name} columns")
        else:
            print(f"There is no missing id between {a.name} columns")

PATH_DIR = '..\data'

def record(dfram, file_name, folder_name):
    if not os.path.exists(f"{PATH_DIR}/{folder_name}"):
        os.makedirs(f"{PATH_DIR}/{folder_name}")
        dfram.to_csv(f"{PATH_DIR}/{folder_name }/{ file_name }.csv",index=False, index_label= None, encoding="UTF8", header=True)
    dfram.to_csv(f"{PATH_DIR}/{folder_name}/{ file_name }.csv",index=False, index_label= None, encoding="UTF8", header=True)


