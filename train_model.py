
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import joblib

data=pd.read_csv("data/processed/features.csv")

X=data[["Peak","Peak_to_Peak","Kurtosis","Skewness","Crest_Factor"]]
y=data["RMS"]

X_train,X_test,y_train,y_test=train_test_split(
X,y,test_size=0.2,random_state=42
)

model=LinearRegression()

model.fit(X_train,y_train)

score=model.score(X_test,y_test)

print("R2 score:",score)

joblib.dump(model,"models/linear_regression_model.pkl")
