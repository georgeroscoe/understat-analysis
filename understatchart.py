#!python3
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import csv

df = pd.read_csv('understatdata.csv',sep=',',encoding="utf8")

lst = []

npxGxA_threshold = df['npxGxA/90'] > 1.1

xA_threshold = df['xA/90'] > 0.4

min_threshold = df['time'] > 1500

df2 = df[min_threshold]

df3 = df2[npxGxA_threshold]

df4 = df2[xA_threshold]

df3 = df3.sort_values(by=['npxGxA/90','time'],axis=0,ascending=True)

df3.to_csv('understattopxgxadata.csv')


players = df3.iloc[:,2] + " " + df3.iloc[:,-4]

teams = df3.iloc[:,15]

npxg_per90 = df3.iloc[:,-2]

xa_per90 = df3.iloc[:,-3]

npxg_xa_per90 = df3.iloc[:,-1]

idx = np.arange(len(df3))

graph_npxg = plt.barh(y=idx,width=npxg_per90)

graph_xa = plt.barh(y=idx,width=xa_per90,left=npxg_per90)

plt.yticks(idx, players)

plt.tight_layout()

plt.legend((graph_npxg[0], graph_xa[0]), ('NPxG/90', 'xA/90'),fontsize='small')

plt.show()
