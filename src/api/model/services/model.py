# model.py
import sys
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import warnings
warnings.filterwarnings('ignore')

def train_model():
    raw_data = pd.read_csv('/Users/senaoz/Documents/Projects/mis463/backend/src/api/model/services/kc_house_data.csv')

    drop_cols = ['id']
    data = raw_data.drop(drop_cols, axis=1)
    target = data['price']
    data = data.drop(['price'], axis=1)

    data['date'] = pd.to_datetime(data['date'])
    data['year'] = data['date'].dt.year
    data['month'] = data['date'].dt.month
    data['day'] = data['date'].dt.day

    data = data.drop("date", axis=1)

    X_train, X_test, y_train, y_test = \
        train_test_split(data, target, random_state=42, train_size=0.60, shuffle=True)

    model = LinearRegression()
    model.fit(X_train, y_train)

    return model

def predict(input_data):
    user_data = pd.DataFrame([input_data])
    user_pred = model.predict(user_data)
    return user_pred[0]

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python model.py <input_feature_1> <input_feature_2> <input_feature_3>")
        sys.exit(1)

    input_features = [float(arg) for arg in sys.argv[1:]]
    model = train_model()
    prediction = predict(input_features)
    print(f"{prediction}")
