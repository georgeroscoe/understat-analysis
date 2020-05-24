#!python3

import asyncio
import json
import aiohttp
import pandas as pd
from understat import Understat

async def main():
    async with aiohttp.ClientSession() as session:
        understat = Understat(session)
        lst = []
        leagues = ["epl","La liga", "Bundesliga", "Serie A", "Ligue 1"]
        seasons = [2014,2015,2016,2017,2018,2019]
        for j in leagues:
            for i in seasons:
                players = await understat.get_league_players(j,i)
                df = pd.DataFrame.from_dict(players)
                df['season'] = str(i)[-2:] + "/" + str(i+1)[-2:]
                lst.append(df)

        final_df = pd.concat(lst,ignore_index=True)

        final_df['xA/90'] = final_df.apply(lambda row: float(row['xA'])/(int(row['time'])/90),axis=1)
        final_df['npxG/90'] = final_df.apply(lambda row: float(row['npxG'])/(int(row['time'])/90),axis=1)
        final_df['npxGxA/90'] = final_df['xA/90'] + final_df['npxG/90']



        final_df.to_csv('understatdata.csv')


loop = asyncio.get_event_loop()
loop.run_until_complete(main())
