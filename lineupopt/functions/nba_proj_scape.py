import requests
import pandas as pd
from bs4 import BeautifulSoup as soup

def nba_proj_scape():
    url = "https://www.numberfire.com/nba/daily-fantasy/daily-basketball-projections"
    html = requests.get(url).text
    page = soup(html, features='lxml')

    stats = []
    rows = page.findAll('tr')
    stat_rows = rows[5:-3]
    for row in range(len(stat_rows)):
        stats.append([i.getText().replace('\n','').strip() for i in stat_rows[row].findAll('td')])

    cols = ['P', 'FP', 'Salary', 'Value', 'Min', 'Pts', 'Reb', 'Ast', 'Stl', 'Blk', 'Tot']
    stats_df = pd.DataFrame(stats, columns=cols)
    stats_df[['X', 'X1', 'FirstName', 'LastName', 'Pos', 'Team', '@', 'Opp']] \
        = stats_df.P.str.split(n=7, expand=True)

    stats_df['Nickname'] = stats_df.FirstName + ' ' + stats_df.LastName
    stats_df.drop(['P','X','X1'], axis=1, inplace=True)

    idx = [1,3,4]
    new_cols = [cols[i] for i in idx]
    ordered_cols = ['Nickname'] + new_cols

    stats_df = stats_df[ordered_cols]
    return stats_df
