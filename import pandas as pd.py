import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

# Step 1: Load the data
data = pd.read_excel("C:\\Users\\duongd11\\Downloads\\Restaurant Revenue.xlsx")

# Step 2: No preprocessing needed for this example

# Step 3: Split the data into features and target variable
X = data[['Number_of_Customers', 'Menu_Price', 'Marketing_Spend', 'Average_Customer_Spending', 'Promotions', 'Reviews']]
y = data['Monthly_Revenue']

# Step 4: Split data into training and testing sets (80% train, 20% test)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Step 5: Train the multiple regression model
model = LinearRegression()
model.fit(X_train, y_train)

# Step 6: Make predictions
y_pred = model.predict(X_test)

# Step 7: Evaluate the model
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

# Step 8: Output the multiple regression statistics
print("Multiple Regression Model Results:")
print("Coefficients (Number_of_Customers, Menu_Price, Marketing_Spend, Average_Customer_Spending, Promotions, Reviews):", model.coef_)
print("Intercept:", model.intercept_)
print("Mean Squared Error:", mse)
print("R^2 Score:", r2)
print("Go PACKERS YEHAHAHAHAAH")
