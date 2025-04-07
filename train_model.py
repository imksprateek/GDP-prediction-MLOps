import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
import pickle

# Sample dummy data: You should replace this with real-world data
data = {
    'investment': [100, 150, 200, 250, 300],
    'consumption': [400, 500, 600, 700, 800],
    'exports': [50, 60, 70, 80, 90],
    'gdp': [550, 710, 870, 1030, 1190]
}

df = pd.DataFrame(data)

X = df[['investment', 'consumption', 'exports']]
y = df['gdp']

model = LinearRegression()
model.fit(X, y)

# Save model using pickle
with open('gdp_model.pkl', 'wb') as f:
    pickle.dump(model, f)

print("Model trained and saved as gdp_model.pkl")
