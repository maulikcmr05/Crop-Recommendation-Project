import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import joblib

# Load dataset
crop = pd.read_csv('Crop_recommendation.csv')

# Input data
x = crop.drop('label', axis=1)

# Output data
y = crop['label']

# Split data
x_train, x_test, y_train, y_test = train_test_split(
    x, y, test_size=0.2, random_state=42
)

# Model
model = RandomForestClassifier()
model.fit(x_train, y_train)

# Save model
joblib.dump(model, 'crop_model.pkl')

print('Model Trained Successfully')