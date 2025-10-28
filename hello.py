import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
np.random.seed(42)
n = 200
study_hours = np.random.uniform(0, 10, n)
attendance = np.random.uniform(50, 100, n)
prob_pass = 1 / (1 + np.exp(-0.5 * (study_hours - 5) - 0.05 * (attendance - 75)))
pass_fail = np.random.binomial(1, prob_pass)
X = np.column_stack((study_hours, attendance))
y = pass_fail
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)
model = LogisticRegression()
model.fit(X_train, y_train)
h = 0.2 
x_min, x_max = study_hours.min() - 1, study_hours.max() + 1
y_min, y_max = attendance.min() - 5, attendance.max() + 5
xx, yy = np.meshgrid(np.arange(x_min, x_max, h),np.arange(y_min, y_max, h))
Z = model.predict(np.c_[xx.ravel(), yy.ravel()])
Z = Z.reshape(xx.shape)
plt.figure(figsize=(10, 6))
plt.contourf(xx, yy, Z, cmap=plt.cm.Paired, alpha=0.3)
scatter = plt.scatter(X_train[:, 0], X_train[:, 1], c=y_train, cmap=plt.cm.bwr, edgecolors='k')
plt.xlabel("Study Hours")
plt.ylabel("Attendance (%)")
plt.title("Logistic Regression Decision Boundary: Pass vs Fail")
plt.legend(*scatter.legend_elements(), title="Pass (1) / Fail (0)")
plt.grid(True)
plt.show()
