import pandas as pd
import warnings
warnings.filterwarnings('ignore')
pd.set_option("display.max_rows", None, "display.max_columns", None)
pd.set_option('display.width', 1000)
data = pd.read_csv(r'C:\Users\ninad\Desktop\Cricket Data\ipl_all_matches.csv')
df = pd.DataFrame(data, columns = ['bowler', 'ball', 'runs_off_bat', 'wicket_type', 'wides', 'noballs', 'match_id', 'innings', 'extras', 'legbyes', 'byes', 'striker'])
df = df[df['match_id']>=300000]
df1 = (df[(df['bowler']=="KH Pandya") & (df['striker']=="V Kohli")])
index = df1.index
rows = len(index)
runs = df1['runs_off_bat'].sum()
df2 = df1[(df1['wicket_type']=='caught') | (df1['wicket_type'] == 'bowled') | (df1['wicket_type']=='lbw') | (df1['wicket_type'] == 'caught and bowled') | (df1['wicket_type'] == 'stumped') | (df1['wicket_type'] == 'hit wicket')]
index = df2.index
wickets = len(index)
#print(df2)
runs3 = df1['noballs'].sum() 
noofwides = df1[df1['wides']> 0]
index = noofwides.index
finalwides = len(index)
finalrows = rows - finalwides - runs3
average = runs/wickets
strikerate = (runs/finalrows)*100
economy = (runs/finalrows)*6
name = df1['bowler'].iloc[1]
name2 = df1['striker'].iloc[1]
bpd = finalrows/wickets
df3 = df1[df1["runs_off_bat"] == 0]
index = df3.index
count_dot= len(index) - finalwides
print("Bowler:", name , "vs ","Batsman:", name2)
print("Runs: ", runs)
print("Outs: ", wickets)
print("Overs: ", int(finalrows/6)+(finalrows%6)/10)
print("Average: ", round(average,2))
print("Economy: ", round(economy,2))
print("Strike-rate: ", round(strikerate,2))
print("Balls Per Dismissal: ",round(bpd,2))
print("DBP: ", round((count_dot/finalrows)*100,2))