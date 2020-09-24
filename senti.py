#!/usr/bin/env python
# coding: utf-8

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from jupyterthemes import jtplot
import string

jtplot.style(theme='monokai',context='notebook',ticks=True,grid=False)
t = pd.read_csv("train.csv")
t.info()
t = t.drop(['id'],axis = 1)
t['length']=t['tweet'].apply(len)
t
t.describe()
pos = t[t['label']==0]
pos

neg = t[t['label']==1]
neg

get_ipython().system('pip install WordCloud')

sen = t['tweet'].tolist()
onestr = " ".join(sen)
onestr

string.punctuation
onestr_nopunc = []
for char in onestr:
    if char not in string.punctuation:
        onestr_nopunc.append(char)

onestr_nop = ' '.join(onestr_nopunc)
onestr_nop


nltk.download("stopwords")
stopwords.words('english')

onestr_nopclean1 = [word for word in onestr_nop.split()]
onestr_nopclean1





