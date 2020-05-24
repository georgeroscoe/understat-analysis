#!python3
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import csv
from adjustText import adjust_text

df = pd.read_csv('understatdata.csv',sep=',',encoding="utf8")

lst = []

npxGxA_threshold = df['npxGxA/90'] > 1.2

xA_threshold = df['xA/90'] > 0.4

min_threshold = df['time'] > 1500

df2 = df[min_threshold]

df3 = df2[npxGxA_threshold]

#df4 = df2[xA_threshold]

df3 = df3.sort_values(by=['npxGxA/90','time'],axis=0,ascending=True)

df3.to_csv('understattopxgxadata.csv')


players = df3.iloc[:,2] + " " + df3.iloc[:,-4]

teams = df3.iloc[:,15]

npxg_per90 = df3.iloc[:,-2]

xa_per90 = df3.iloc[:,-3]

npxg_xa_per90 = df3.iloc[:,-1]

idx = np.arange(len(df3))

players_list = list(players)

surname_list = []

for i in players_list:
    words = i.split()
    if len(words) == 2:
        surname_list.append(i)
    elif len(words) == 3:
        surname_list.append(" ".join(words[-2:]))
    elif len(words) > 3:
        surname_list.append(" ".join(words[1:]))



npxg_per90_list = list(npxg_per90)

xa_per90_list = list(xa_per90)



plt.scatter(npxg_per90_list,xa_per90_list)

texts = []
for x, y, s in zip(npxg_per90_list,xa_per90_list, surname_list):
        if x > 0.7 or y > 0.3:
            texts.append(plt.text(x, y, s, fontsize=8.5))

adjust_text(texts,only_move={'points':'y', 'texts':'y'})


plt.xlabel("NPxG/90")

plt.ylabel("xA/90")

plt.show()
