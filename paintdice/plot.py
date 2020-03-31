import matplotlib.pyplot as plt
import numpy as np 
from sklearn import datasets, linear_model 
from sklearn.metrics import mean_squared_error, r2_score

xs = list()
ys = list()

with open('data.txt') as f:
    for line in f:
        s = str.split(line)
        xs.append(float(s[0]))
        ys.append(float(s[2]))

# X must be a column vector
X = np.array(xs).reshape(-1,1)
Y = np.array(ys)

regr = linear_model.LinearRegression()
regr.fit(X, Y)
Y_pred = regr.predict(X)

print("Regression: E = %f * N %+f" % (regr.coef_, regr.intercept_))
print("R^2: %f" % r2_score(Y, Y_pred))

plt.plot(X, Y, color='blue', linewidth=3)
plt.xlabel("Number of Dice") 
plt.ylabel("Expected Value")
plt.show()