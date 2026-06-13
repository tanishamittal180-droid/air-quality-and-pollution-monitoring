import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression

def predict_next_aqi(df):

    if len(df) < 5:
        return None

    data = df.copy()

    data["index"] = np.arange(len(data))

    X = data[["index"]]
    y = data["aqi"]

    model = LinearRegression()
    model.fit(X, y)

    future = [[len(data)]]

    prediction = model.predict(future)

    return round(float(prediction[0]), 2)