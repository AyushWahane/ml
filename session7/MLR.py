import pandas
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import OneHotEncoder
import numpy
ds = pandas.read_csv('50_Startups.csv')
X = ds[ ["R&D Spend", "Administration", "Marketing Spend"] ]
y = ds["Profit"]
state = ds["State"]
le = LabelEncoder()
state_le = le.fit_transform(state)
state_le_2d = state_le.reshape(50,1)
ohe = OneHotEncoder()
state_ohe =ohe.fit_transform(state_le_2d)
state_ohe_final = state_ohe.toarray()
state_final_trap = state_ohe_final[:, 0:2]
x_final = numpy.hstack((X, state_final_trap))
model = LinearRegression()
model.fit(x_final, y)
model.coef_