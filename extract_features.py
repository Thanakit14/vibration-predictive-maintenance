
import os
import pandas as pd
from src.preprocess import load_waveform
from src.feature_engineering import extract_features

rows=[]

for file in os.listdir("data/raw"):
    if file.endswith(".txt"):
        path=os.path.join("data/raw",file)

        df=load_waveform(path)

        f=extract_features(df["amplitude"].values)

        f["File"]=file

        rows.append(f)

df=pd.DataFrame(rows)

df.to_csv("data/processed/features.csv",index=False)

print(df)
