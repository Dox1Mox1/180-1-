# Import necessary libraries
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, confusion_matrix

# Read the spreadsheet
baseball_data = pd.read_excel(r'C:\Users\duongd11\Downloads\baseball.xlsx')

# Extract necessary columns
X = baseball_data[['RS', 'RA', 'W', 'OBP', 'SLG', 'BA']]  # Features
y = baseball_data['Playoffs']  # Target variable

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Choose the model (Random Forest Classifier)
model = RandomForestClassifier(n_estimators=100, random_state=42)

# Train the model
model.fit(X_train, y_train)

# Make predictions
y_pred = model.predict(X_test)

# Evaluate the model
print("Confusion Matrix:")
print(confusion_matrix(y_test, y_pred))
print("\nClassification Report:")
print(classification_report(y_test, y_pred))

# Example prediction
team_values = [[850, 750, 90, 0.350, 0.450, 0.270]]  # Example team values
prediction = model.predict(team_values)
print("\nPrediction for example team values:", "Made Playoffs" if prediction[0] == 1 else "Did not make Playoffs")
