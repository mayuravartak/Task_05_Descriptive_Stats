import pandas as pd

df = pd.read_csv("womens_lacrosse_stats.csv")

print("Syracuse Women’s Lacrosse – Descriptive Statistics Check\n")

# 1 Total Games
total_games = len(df)
print(f"Total Games Played: {total_games}")

# 2 Overall Win Percentage
if 'Result' in df.columns:
    wins = df[df['Result'].str.contains('W', case=False)].shape[0]
    print(f"Win Percentage", round(wins * 100 / total_games, 2),"%")

# 3 Syracuse score more goals in home games or away games
df[['Outcome', 'Score']] = df['Result'].str.split(' ', expand=True)
df[['goals_for', 'goals_against']] = df['Score'].str.split('-', expand=True)
df['goals_for'] = df['goals_for'].astype(int)
df['goals_against'] = df['goals_against'].astype(int)

home_avg = round(df['goals_for'].mean(),2)
away_avg = round(df['goals_against'].mean(),2)
print(home_avg)
print("Home Average:", home_avg,"\nAway Average:", away_avg)

if home_avg > away_avg:
    print("Syracuse scored more goals on average in HOME games.")
    verdict = "Syracuse scored more goals on average in HOME games."
elif away_avg > home_avg:
    print("Syracuse scored more goals on average in AWAY games.")
    verdict = "Syracuse scored more goals on average in AWAY games."
else:
    print("Syracuse scored equally on average in Home and Away games.")
    verdict = "Syracuse scored equally on average in Home and Away games."


# Summary Export
summary_data = {
    "Total_Games": total_games,
    "Win Percentage": str(round(wins * 100 / total_games, 2))+"%",
    "Syracuse score more goals in home games or away games": "Home Average:"+ str(home_avg) + "\nAway Average:" + str(away_avg),
    "Verdict": verdict
}

summary_df = pd.DataFrame([summary_data])
summary_df.to_csv("python_answers.csv", index=False)

print("\nValidation summary exported as 'python_answers.csv'")
