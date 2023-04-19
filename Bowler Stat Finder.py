import pandas as pd
import warnings
warnings.filterwarnings('ignore')
pd.set_option("display.max_rows", None, "display.max_columns", None)
pd.set_option('display.width', 1000)
data = pd.read_csv(r'C:\Users\ninad\Desktop\Cricket Data\ipl_all_match.csv')
df = pd.DataFrame(data, columns = ['bowler', 'ball', 'runs_off_bat', 'wicket_type', 'wides', 'noballs', 'match_id', 'innings', 'extras', 'legbyes', 'byes', 'striker'])
df = df[(df['match_id']>=1250000) & (df['match_id']<=1500000)]
name = ("JO Holder")
df1 = (df[(df['bowler']== name) & (df['innings'] < 3)])
#print(df1)
df2 = (df1[(df1['ball'] > 0) & (df1['ball'] < 21)])

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
print("Bowler:", name)
print("Runs Conceded: ", runs)
print("Wickets: ", wickets)
print("Overs Bowled: ", int(balls/6)+(balls%6)/10)
print("Average: ", round(average,2))
print("Economy: ", round(economy,2))
print("Strike-rate: ", round(strike_rate,2))