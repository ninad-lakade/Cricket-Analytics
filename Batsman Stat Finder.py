import pandas as pd
import warnings
import matplotlib.pyplot as plt
warnings.filterwarnings('ignore')
pd.set_option("display.max_rows", None, "display.max_columns", None)
pd.set_option('display.width', 1000)
data = pd.read_csv(r'C:\Users\ninad\Desktop\Cricket Data\ipl_all_matches.csv')
df = pd.DataFrame(data, columns = ['bowler', 'ball', 'runs_off_bat', 'wicket_type', 'wides','non_striker', 'player_dismissed','noballs', 'match_id', 'innings', 'extras', 'legbyes', 'byes', 'striker'])
df = df[(df['match_id']>=1100000) & (df['match_id']<=1300000)]
name = ("HH Pandya")
df1 = (df[(df['ball'] > 15) & (df['ball'] < 21) & (df['innings'] < 3)])
df2 = df1[(((df1['wicket_type']=='caught') | (df1['wicket_type'] == 'bowled') | (df1['wicket_type'] == 'run out') | (df1['wicket_type']=='lbw') | (df1['wicket_type'] == 'caught and bowled') | (df1['wicket_type'] == 'stumped') | (df1['wicket_type'] == 'hit wicket')) & (df1['player_dismissed'] == name))]
index = df2.index
wickets = len(index)
df3 = (df1[(df1['striker']== name) ])
index = df3.index
balls = len(index)
noofwides = df3[df3['wides']> 0]
index = noofwides.index
finalwides = len(index)
runs = df3['runs_off_bat'].sum()
balls_nb = df3['noballs'].sum()
balls = balls - finalwides
strike_rate = (runs/balls)*100
average = runs/wickets
df4 = df3[df3['runs_off_bat'] == 4]
index = df4.index
count_four = len(index)
df5 = df3[df3["runs_off_bat"] == 6]
index = df5.index
count_six = len(index)
df6 = df3[df3["runs_off_bat"] == 0]
index = df6.index
count_dot= len(index) - finalwides
print("Batsman:", name)
print("Runs Scored: ", runs)
print("Balls Faced: ", balls)
print("Average: ", round(average,2))
print("Strike-rate: ", round(strike_rate,2))
print("BPF: ", round((balls/count_four),2))
print("BPS: ", round((balls/count_six),2))
print("DBP: ", round((count_dot/balls)*100,2))
#plt.scatter(name, strike_rate)
