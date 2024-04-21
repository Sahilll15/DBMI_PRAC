import pandas as pd
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

# Load the dataset
data = pd.read_csv('linear_data.csv')

# Split the data into independent variable (X) and dependent variable (Y)
X = data[['X']]
y = data['Y']

# Create and fit the linear regression model
model = LinearRegression()
model.fit(X, y)


# Print the coefficients
# print('Intercept:', model.intercept_)
print('Coefficient:', model.coef_[0])

# Predict the values
y_pred = model.predict(X)

# Plot the data and the regression line
plt.scatter(X, y, color='blue')
plt.plot(X, y_pred, color='red')
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Linear Regression')
plt.show()
