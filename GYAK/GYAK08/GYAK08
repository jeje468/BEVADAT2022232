# %%
from LinearRegressionSkeleton import LinearRegression
import pandas as pd
from sklearn.datasets import load_iris
from matplotlib import pyplot as plt

# %%
model = LinearRegression()
iris = load_iris()
df = pd.DataFrame(iris.data, columns=iris.feature_names)
X = df['petal width (cm)'].values
y = df['sepal length (cm)'].values
model.fit(X, y)

# %%
y_pred = model.predict(model.X_test)

plt.scatter(model.X_test, model.y_test)
plt.plot([min(model.X_test), max(model.X_test)], [min(y_pred), max(y_pred)], color='red') # predicted
plt.show()


