"""
1. Definition:  
Training predictive models
2. Why Use:  
Find patterns in data 
"""


from sklearn.linear_model import LinearRegression

X = [[1], [2], [3]]  # Input
y = [2, 4, 6]        # outpur it gave

model = LinearRegression()
model.fit(X, y)
print(f"Prediction: {model.predict([[4]])[0]}")


"""
Output:
Prediction: 8.0
"""
