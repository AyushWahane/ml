import pandas
from sklearn.linear_model import LinearRegression
#reading database form xl file 
sal_db = pandas.read_csv("Salary_Data.csv")
exp = sal_db["YearsExperience"].values.reshape(30,1)
sal = sal_db["Salary"].values.reshape(30,1)
mind = LinearRegression()
mind.fit(exp, sal)
x = input("Enter number of year experience : ")
rslt = mind.predict([[int(x)]])
print(rslt)