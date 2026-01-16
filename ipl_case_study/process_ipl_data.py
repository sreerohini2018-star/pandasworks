#pandas.readcsv("file_path")
import pandas as pd
df=pd.read_csv("ipl_case_study\ipldata.csv")
print(df.shape)
print(df.columns)
print(df.info())
print(df.isnull().sum())
print(df["match_id"].fillna(549,inplace=True))
print(df["season"].fillna(df["season"].mode()[0],inplace=True))
round_score_mean=round(df["runs_scored"].mean())
print(df["runs_scored"].fillna(round_score_mean,inplace=True))
print(df["city"].fillna(df["city"].mode()[0],inplace=True))
print(df["team1"].fillna("unknown",inplace=True))
print(df["team2"].fillna("unknown",inplace=True))
print(df["winning_team"].fillna("unknown",inplace=True))
print(df["player_of_match"].fillna("unknown",inplace=True))
print(df["venue"].fillna(df["venue"].mode()[0],inplace=True))
print(df["wickets"].fillna(df["wickets"].median(),inplace=True))
print(df.isnull().sum())

#analysis
#matches per season
print("matches per season=",df["season"].value_counts())
#top match count season
print("top match count season=",df["season"].value_counts().idxmax())
#total match won by each team
print("total match won by each=",df["winning_team"].value_counts())
#avg runs per season
print("avg runs per season=",df.groupby("season")["runs_scored"].mean())
#venue wise match count
print("venuewise match count=",df["venue"].value_counts())
#venue wise avg runs
print("venuewise avg runs=",df.groupby("venue")["runs_scored"].mean())
#city wise match count
print("citywise match count=",df["city"].value_counts())
#city wise avg runs
print("citywise avg runs=",df.groupby("city")["runs_scored"].mean())
#which winning team has the highest avg run
print(df.groupby("winning_team")["runs_scored"].mean().idxmax())
#top3 venue
print(df["venue"].head(3))