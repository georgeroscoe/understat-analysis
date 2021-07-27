#!python3
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


def load_data():
    df = pd.read_csv('understatdata.csv', sep=',', encoding="utf8")
    df.replace('Kylian Mbappe-Lottin', 'Kylian Mbappe', inplace=True)
    return df


def get_elite_seasons(df):
    data_within_threshold = df.loc[(df['npxGxA/90'] > 1.1) & (df['time'] > 1500)]
    data_within_threshold.sort_values(by=['npxGxA/90', 'xA/90', 'time'], axis=0, ascending=True, inplace=True)
    data_within_threshold.to_csv('understattopxgxadata.csv')
    return data_within_threshold


def get_player_and_season(df):
    player_and_season = df['player_name'] + " " + df['season']
    return player_and_season


def get_graph_info(df):
    player_and_season = df['player_name'] + " " + df['season']
    npxg_per90 = df['npxG/90']
    xa_per90 = df['xA/90']

    return player_and_season, npxg_per90, xa_per90


def plot_elite_graph(df):
    y_labels, npxg_per90, xa_per90 = get_graph_info(df)
    idx = np.arange(len(elite_seasons))

    graph_npxg = plt.barh(y=idx, width=npxg_per90)

    graph_xa = plt.barh(y=idx, width=xa_per90, left=npxg_per90)

    plt.yticks(idx, y_labels, fontsize=8)

    plt.tight_layout()

    plt.legend((graph_npxg[0], graph_xa[0]), ('NPxG/90', 'xA/90'), fontsize='small')

    plt.savefig('NPxGxA.png')
    plt.show()


if __name__ == "__main__":

    data = load_data()
    elite_seasons = get_elite_seasons(data)
    plot_elite_graph(elite_seasons)



