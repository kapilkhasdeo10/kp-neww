import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score

study = [1,2,3,4,5,6,7,8,9,10,2.5,4.5,6.5,8.5]
marks = [25,38,52,65,71,78,85,89,93,96,43,68,82,91]

X =np.array(study).reshape(-1,1)    #   Must for 2D for sklearn
Y = np.array(marks)

X_train,X_test, Y_train,Y_test = train_test_split(X, Y, test_size=0.2, random_state=42)

model = LinearRegression()
model.fit(X_train,Y_train)

print(f'Slope:      {model.coef_[0]:.2f} (marks incease per study hour)')
print(f'fIntercept: {model.intercept_:.2f} (marks at 0 study hour)')

Y_pred = model.predict(X_test)
print(f'R2 Score:   {r2_score(Y_test,Y_pred):.4f} (1.0 = perfect)')
print(f'RMSE:       {mean_squared_error(Y_test,Y_pred)**0.5:.2f} (marks average error)')

#   Predict new student
new_pred = model.predict([[7]])[0]
print(f'Student studying 7 hrs predicted marks: {new_pred:.1f}')

#   Plot
plt.figure(figsize=(9,5))
plt.scatter(X,Y,color='steelblue',s=100,alpha=0.8,label='Actual')
plt.plot(X,model.predict(X),color='red',linewidth=2,label='Predicted line')
plt.xlabel("Study Hours/Day")
plt.ylabel("Exam Marks")
plt.title("Linear Regression - Study Hours vs Marks")
plt.legend()
plt.grid(True,alpha=0.3)
plt.show()