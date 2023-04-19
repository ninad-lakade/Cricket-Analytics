import pandas as pd
import warnings
warnings.filterwarnings('ignore')
pd.set_option("display.max_rows", None, "display.max_columns", None)
pd.set_option('display.width', 1000)
data = pd.read_csv(r'C:\Users\ninad\Desktop\Cricket Data\ipl_all_match.csv')
df = pd.DataFrame(data, columns = ['bowler', 'ball', 'runs_off_bat', 'wicket_type', 'wides', 'noballs', 'match_id', 'innings', 'extras', 'legbyes', 'byes', 'striker'])
df = df[(df['match_id']>=1100000) & (df['match_id']<=1500000)]
result = pd.DataFrame(columns = ['Bowler', 'Wickets', 'Runs', 'Overs', 'Average', 'Economy', 'Strike-rate'])
for i in df['bowler'].unique():
    df1 = (df[(df['bowler']== i) & (df['innings'] < 3)])
    #print(df1)
    df2 = (df1[(df1['ball'] > 16) & (df1['ball'] < 21)])
    #print(df2)
    index = df2.index
    balls = len(index)
    noofwides = df2[df2['wides']> 0]
    index = noofwides.index
    finalwides = len(index)
    runs = df2['runs_off_bat'].sum()
    runs_nb = df2['noballs'].sum()
    runs_wide = df2['wides'].sum()
    runs = runs + runs_nb + runs_wide
    #print(runs)
    #print(runs_nb)
    #print(runs_wide)
    balls = balls - finalwides - runs_nb
    #print(balls)
    df3 = df2[(df2['wicket_type']=='caught') | (df2['wicket_type'] == 'bowled') | (df2['wicket_type']=='lbw') | (df2['wicket_type'] == 'caught and bowled') | (df2['wicket_type'] == 'stumped') | (df2['wicket_type'] == 'hit wicket')]
    index = df3.index
    wickets = len(index)
    #print(wickets)
    economy = (runs/balls)*6
    strike_rate = balls/wickets
    average = runs/wickets
    if balls > 60 :
        df4 = pd.DataFrame({"Bowler":[i], "Wickets":[wickets], "Runs":[runs], "Overs":[int(balls/6)+(balls%6)/10], "Average":[average], "Economy":[economy], "Strike-rate":[strike_rate]})
        result = result.append(df4)
result.sort_values(by=['Economy'], inplace=True, ascending=True)
final = result.round(decimals=2)
print(final)
final.to_excel(r'C:\Users\ninad\Desktop\Cricket Data\BOWLERS 2018 to 2020 DEATH.xlsx', index = False)
