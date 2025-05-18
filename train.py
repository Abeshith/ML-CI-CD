from sklearn.datasets import load_wine
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import pickle, os

## Load the dataset
wine = load_wine()
X, y = wine.data, wine.target

## Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

## Create a Random Forest Classifier
model = RandomForestClassifier(n_estimators=100, random_state=42)

## train the model
model.fit(X_train, y_train)

## Save the model to a file
os.makedirs('model', exist_ok=True)

## Save the model using pickle
with open('model/wine_model.pkl', 'wb') as f:
    pickle.dump(model, f)

print("Model trained and saved to 'model/wine_model.pkl'")
