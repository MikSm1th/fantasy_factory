cols = ['P', 'FP', 'Salary', 'Value', 'C/A', 'Yds', 'Tds', 'Ints', 'Att', 'Yds', 'Tds', 'Rec', 'Yds', 'Tds', 'Tgts']
stats = pd.read_csv('data/nfl/week-12-daily-football-projections.csv')#, usecols=cols)
stats.rename(columns={"Player": "Nickname"}, errors="raise", inplace=True)
stats_df = stats[['Nickname', 'FP']]
stats_df['FP'] = stats_df.FP.astype(object)
# cols = ['P', 'FP', 'Salary', 'Value', 'C/A', 'Yds', 'Tds', 'Ints', 'Att', 'Yds', 'Tds', 'Rec', 'Yds', 'Tds', 'Tgts']
# stats_df = pd.DataFrame(stats, columns=cols) = 
#stats_df[['X', 'X1', 'FirstName', 'LastName', 'Pos', 'Team', '@', 'Opp']] \
#    = stats_df.P.str.split(n=7, expand=True)
stats_df.info()
