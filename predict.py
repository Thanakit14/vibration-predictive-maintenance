
import pandas as pd
import joblib
from src.iso_zone_classifier import iso_zone

model=joblib.load("models/linear_regression_model.pkl")

data=pd.read_csv("data/processed/features.csv")

X=data[["Peak","Peak_to_Peak","Kurtosis","Skewness","Crest_Factor"]]

pred=model.predict(X)

data["Predicted_RMS"]=pred

data["ISO_Zone"]=data["Predicted_RMS"].apply(iso_zone)

data.to_csv("results/prediction_results.csv",index=False)

print(data)
