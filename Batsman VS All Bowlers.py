import pandas as pd
import warnings
#import matplotlib.pyplot as plt
warnings.filterwarnings('ignore')
pd.set_option("display.max_rows", None, "display.max_columns", None)
pd.set_option('display.width', 1000)
data = pd.read_csv(r'C:\Users\ninad\Desktop\Cricket Data\ipl_all_matches.csv')
df = pd.DataFrame(data, columns = ['bowler', 'ball', 'runs_off_bat', 'wicket_type', 'wides','non_striker', 'player_dismissed','noballs', 'match_id', 'innings', 'extras', 'legbyes', 'byes', 'striker'])
df = df[(df['match_id']>=1100000) & (df['match_id']<=1500000)]
result = pd.DataFrame(columns = ['Bowler', 'Runs', 'Balls', 'Wickets', 'Average', 'Economy', 'Strike-rate', 'DBP'])
name = ("V Kohli")
df1 = (df[(df['striker']== name)  & (df['innings'] < 3)])
for i in df1['bowler'].unique():
    df2 = (df1[(df1['bowler']== i) & (df1['innings'] < 3)])
    #print(df1)
    df6 = (df2[(df2['ball'] > 15) & (df2['ball'] < 21)])
    #print(df2)
    index = df6.index
    balls = len(index)
    noofwides = df6[df6['wides']> 0]
    index = noofwides.index
    finalwides = len(index)
    runs = df6['runs_off_bat'].sum()
    runs_nb = df6['noballs'].sum()
    runs_wide = df6['wides'].sum()
    #print(runs)
    #print(runs_nb)
    #print(runs_wide)
    balls = balls - finalwides
    #print(balls)
    df3 = df6[(df6['wicket_type']=='caught') | (df6['wicket_type'] == 'bowled') | (df6['wicket_type']=='lbw') | (df6['wicket_type'] == 'caught and bowled') | (df6['wicket_type'] == 'stumped') | (df6['wicket_type'] == 'hit wicket')]
    index = df3.index
    wickets = len(index)
    #print(wickets)
    economy = (runs/balls)*6
    strike_rate = (runs/balls)*100
    average = runs/wickets
    df4 = df6[df6["runs_off_bat"] == 0]
    index = df4.index
    count_dot= len(index) - finalwides
    if balls > 0 : 
        dbp = (count_dot/balls)*100
        df5 = pd.DataFrame({"Bowler":[i], "Wickets":[wickets], "Runs":[runs], "Balls":[balls], "Average":[average], "Economy":[economy], "Strike-rate":[strike_rate], "DBP": [dbp]})
        result = result.append(df5)
result.sort_values(by=['Strike-rate'], inplace=True, ascending=False)
final = result.round(decimals=2)
print(final)