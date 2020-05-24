#!python3
import pandas as pd
import csv
import numpy as np
import matplotlib.pyplot as plt
from adjustText import adjust_text

df = pd.read_csv('understatdata.csv',sep=',',encoding="utf8")

df2 = df.groupby(['player_name'])['npg','time','xA'].sum().reset_index()

df2['npg/90'] = df2['npg']/(df2['time']/90)

df2['xA/90'] = df2['xA']/(df2['time']/90)

minutes = df2['time'] > 6999

filter = (df2['npg/90'] + 3*df2['xA/90']) > 0.65

df2 = df2[filter]

df2 = df2[minutes]

df2 = df2.sort_values(by=['npg/90','xA/90'],axis=0,ascending=False)

df2.to_csv('understatforr.csv')


# print(df2.head())
#
#
# players = df2.iloc[:,0]
#
# npg_per90 = df2.iloc[:,-2]
#
# xa_per90 = df2.iloc[:,-1]
#
# idx = np.arange(len(df2))
#
# players_list = list(players)
#
# surname_list = []
#
# for i in players_list:
#     words = i.split()
#     if len(words) == 2:
#         surname_list.append(i)
#     elif len(words) == 3:
#         surname_list.append(" ".join(words[-2:]))
#     elif len(words) > 3:
#         surname_list.append(" ".join(words[1:]))
#
#
#
# npg_per90_list = list(npg_per90)
#
# xa_per90_list = list(xa_per90)
#
# plt.figure(figsize=(20,10))
#
# plt.axvline(max(xa_per90_list)/2, color='k', linestyle='dashed', linewidth=1)
#
# plt.axhline(max(npg_per90_list)/2, color='k', linestyle='dashed', linewidth=1)
#
# plt.ylim((0,1))
#
# plt.xlim((0,0.5))
#
# plt.scatter(xa_per90_list,npg_per90_list)
#
#
# # texts = []
# # for x, y, s in zip(xa_per90_list, npg_per90_list, surname_list):
# #
# #         texts.append(plt.text(x, y, s, fontsize=8.5))
# #
# # adjust_text(texts,only_move={'points':'y', 'texts':'y'},arrowprops=dict(arrowstyle="-", color="r"))
#
#
# plt.ylabel("NPG/90")
#
# plt.xlabel("xA/90")

plt.show()
