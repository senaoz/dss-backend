# model.py
import seaborn as sns
import numpy as np
import sys
import pandas as pd
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings('ignore')
from sklearn.preprocessing import PolynomialFeatures
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score


data = pd.read_csv('/Users/senaoz/Documents/Projects/mis463/backend/src/api/model/services/kc_house_data.csv')
data['date'] = pd.to_datetime(data['date'].str.slice(0, 8), format='%Y%m%d')
data['year'] = data['date'].dt.year
data['month'] = data['date'].dt.month
data['day'] = data['date'].dt.day
data.drop(['id', 'date'], axis=1, inplace=True)

X = data.drop('price', axis=1)
y = data['price']

poly = PolynomialFeatures(degree=2, include_bias=False)
X_poly = poly.fit_transform(X)
X_train, X_test, y_train, y_test = train_test_split(X_poly, y, test_size=0.2, random_state=42)

def train_model():
    model = LinearRegression()
    model.fit(X_train, y_train)
    return model

def predict(input_data):
    input_data = np.array(input_data)
    input_data = input_data.reshape(1, -1)
    input_data = poly.transform(input_data)

    if len(input_data[0]) != len(X_train[0]):
        return 'Wrong input data'

    if model.predict(input_data)[0] < 0:
        return 0

    else:
        return model.predict(input_data)[0]

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python model.py <input_feature_1> <input_feature_2> <input_feature_3>")
        sys.exit(1)

    input_features = [float(arg) for arg in sys.argv[1:]]
    model = train_model()
    prediction = predict(input_features)
    print(f"{prediction}")
