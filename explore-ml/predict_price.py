import pandas
from sklearn.linear_model import LinearRegression
data = pandas.read_csv('iphone_price.csv')
model = LinearRegression()
model.fit(data[["version"]], data[["price"]])
predicted_price = model.predict([[22]])
print(predicted_price)


s = pandas.Series([1, 2, 3, 4, 5], index=['a', 'b', 'c', 'd', 'e'])
print(s['a'])
