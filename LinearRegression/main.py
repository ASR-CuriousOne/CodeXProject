import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn import preprocessing,svm
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

df = pd.read_csv("massForce.csv")
df_binary = df[['accerlation','force']]


df_binary.columns = ['accerlation','force']

x = np.array(df_binary['accerlation']).reshape(-1,1)
y = np.array(df_binary['force']).reshape(-1,1)

X_train, X_test, Y_train, Y_test = train_test_split(x,y,test_size=0.25)

regr = LinearRegression()

regr.fit(X_train,Y_train)
print(regr.score(X_test,Y_test))
print(regr.coef_)
print(regr.intercept_)

y_pred = regr.predict(X_test)
plt.scatter(X_test,Y_test,color = 'b')
plt.plot(X_test,y_pred,color = 'k')

plt.show()
